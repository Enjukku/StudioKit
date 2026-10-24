"""J024 flow cuts (knowledge/jobs/J024-flow-cuts-r2/design.md §1-7, §6 feature, UI screen and marketing rows) in three job workflows.

Kit test (universal). Author: J024 builder C · claude-opus-5-5 · default · 2026-10-24. Drives tools/workflows/wf_harness.mjs with fake
agents through the helpers of test_job_workflows; skipped when Node.js is not installed. Every test failed on the J023 scripts.
§1: no proof stage and no G2 (stage proof is refused before any agent). §2: no roughs (no prototype, value, light, temp, target,
plan-check or skeleton runs; each craft builds once). §3: direction = D1 plan, N1 needs and limits in parallel against the plan alone
(capped tables), one merge, N2 only on a conflict the merge reports. §4: one capture-and-scripts run on the studio-operator per round
(visual_flags, cue_log), the reviewer table per type, selective recheck. §5a: capped repair and recheck briefs. §7: risk token
performance. §6: the minimum run counts.
"""

from __future__ import annotations

import re
import unittest

from tools.tests.test_job_workflows import NODE, full, index, run

FEAT, UI, MKT = "job-feature.js", "job-ui-screen.js", "job-marketing-art.js"
TYPES = (FEAT, UI, MKT)
LEAD = {FEAT: "game-designer", UI: "ui-ux-designer", MKT: "marketing"}
PLAN = {FEAT: "knowledge/jobs/J099-test/contract-test.md", UI: "content/ui/test/spec.md", MKT: "knowledge/jobs/J099-test/marketing/asset-kit-plan.md"}
# The cheapest flags of each type (design §6 "min") and the typical ones (UI shop; feature money and numbers).
MIN = {FEAT: {"money": False, "numbers": False}, UI: {"shop": False, "newLook": False}, MKT: {"launch": False}}
TYP = {FEAT: {"money": True, "numbers": True}, UI: {"shop": True, "newLook": False}, MKT: {"launch": False}}
ALL_FEAT = ["ui-ux-designer", "vfx-designer", "sound-designer", "animator"]
# Labels of removed rough, proof and pre-code check passes (design §2, brief rules).
ROUGH = re.compile(r"proof|proto|temp|rough|value|light|green|board|animatic|blockout|greybox|proxy|plan-check|plan-fix|skeleton|target|keyframe|probes|B1-plan$", re.I)


def labels_of(out: dict, pattern: str) -> list[str]:
    return [x for x in out["labels"] if re.search(pattern, x)]


def roles_of(out: dict, pattern: str) -> set[str]:
    return {x.split(":")[0] for x in labels_of(out, pattern)}


def brief(out: dict, pattern: str) -> str:
    hits = [d["prompt"] for d in out["dumps"] if re.search(pattern, d["label"])]
    if not hits:
        raise AssertionError(f"no dumped brief matches {pattern}: {out['labels']}")
    return hits[0]


def block(text: str, key: str) -> list[str]:
    """The `- item` lines under a top-level brief key (inputs, refs, ...)."""
    out, on = [], False
    for line in text.split("\n"):
        if line == f"{key}:":
            on = True
            continue
        if on:
            if line.startswith("  - "):
                out.append(line[4:])
            else:
                break
    return out


def findings(maker: str, n: int) -> list[dict]:
    return [{"id": f"F{i}", "class": "blocking", "maker_role": maker, "where": "w", "expected": "e", "observed": "o", "evidence": "captures/x.png", "smallest_fix": "f"}
            for i in range(1, n + 1)]


def args(name: str, **changes) -> dict:
    return full(name, **dict(MIN[name], **changes))


@unittest.skipIf(NODE is None, "Node.js not installed")
class J024FlowTests(unittest.TestCase):
    def done(self, out: dict) -> dict:
        self.assertEqual(out["violation"], "")
        self.assertEqual(out["status"], "done", out["outcome"])
        return out

    def round0(self, out: dict, label: str = "candidate") -> set[str]:
        return roles_of(out, rf": RV-{label}-r0-") - {"studio-operator"}

    # ------------------------------------------------------------------ §1: no proof stage, no G2
    def test_proof_stage_is_refused_before_any_agent(self):
        for name in TYPES:
            for size in ("L", "M"):
                with self.subTest(script=name, size=size):
                    out = run(name, args(name, stage="proof", size=size))
                    self.assertEqual(out["status"], "blocked")
                    self.assertEqual(out["agents"], 0)
                    self.assertIn("no proof stage (J024): direction → G1 → build → G3", out["outcome"])
                    self.assertNotIn("proof", out["meta"]["description"])
                    self.assertFalse(any(re.search(r"proof|prototype|green light|plan check", p["title"] + p["detail"], re.I) for p in out["meta"]["phases"]), out["meta"]["phases"])

    # ------------------------------------------------------------------ §2: no roughs; every craft builds the real thing once
    def test_no_rough_proof_or_pre_code_check_runs_in_any_stage(self):
        on = {FEAT: dict(money=True, numbers=True, risks=["saves", "paid-random", "rewards"]), UI: dict(shop=True, newLook=True, risks=["paid-random"]), MKT: dict(launch=True, trends=True)}
        sets = {FEAT: {"presentation": ALL_FEAT}, UI: {"ui_effects": True}, MKT: {"hero_is_character": True}}
        for name in TYPES:
            for stage in ("direction", "build", "repair"):
                with self.subTest(script=name, stage=stage):
                    out = self.done(run(name, full(name, stage=stage, **on[name]), {"set": sets[name]}))
                    bad = [x for x in out["labels"] if ROUGH.search(x.split(": ", 1)[1])]
                    self.assertEqual(bad, [], "a rough, proof or plan-check run is still in the flow")

    def test_each_craft_runs_once_in_build_in_dependency_order(self):
        feat = self.done(run(FEAT, args(FEAT, stage="build", numbers=True), {"set": {"presentation": ALL_FEAT}}))
        makers = [x for x in feat["labels"] if not re.search(r": (RV|FIX)-", x)]
        self.assertEqual(makers[0], "qa-lead: B1-acceptance", "the protected acceptance tests come first")
        for role in ALL_FEAT + ["progression-designer", "feature-builder"]:
            with self.subTest(script=FEAT, role=role):
                self.assertEqual(len([x for x in makers if x.startswith(f"{role}:")]), 1)
        order = [index(feat["labels"], rf"^{r}: B") for r in ("animator", "vfx-designer", "sound-designer", "feature-builder")]
        self.assertEqual(order, sorted(order), "animator → VFX → sound, then the builder integrates")
        self.assertEqual(index(feat["labels"], r"^architect: "), -1, "no architect plan run: its limits table holds the plan")
        ui = self.done(run(UI, args(UI, stage="build", shop=True, risks=["paid-random"]), {"set": {"ui_effects": True}}))
        makers = [x for x in ui["labels"] if not re.search(r": (RV|FIX)-", x)]
        self.assertEqual(makers, ["ui-ux-designer: B1-figma", "vfx-designer: B2-ui-effects", "sound-designer: B3-ui-sounds", "feature-builder: B4-build"],
                         "Figma, effects, sounds, then one implement-and-integrate run; no plan check")
        mkt = self.done(run(MKT, args(MKT, stage="build", size="L")))
        self.assertEqual([x for x in mkt["labels"] if x.startswith("marketing: B")], ["marketing: B1-final"], "the final piece once: render to crops in one run")
        staged = self.done(run(MKT, args(MKT, stage="build"), {"set": {"render_route": "staged-render", "render_maker": "modeler"}}))
        self.assertEqual([x for x in staged["labels"] if ": B" in x], ["marketing: B1-final", "modeler: B1-staged-modeler", "marketing: B2-final-staged"])

    def test_conditional_build_crafts_switch_on_and_off(self):
        cases = [
            (UI, {}, {"ui_effects": True}, "vfx-designer: B2-ui-effects"),
            (MKT, {}, {"render_route": "staged-render", "render_maker": "environment-designer"}, "environment-designer: B1-staged-environment-designer"),
        ] + [(FEAT, {}, {"presentation": [r]}, f"{r}: B") for r in ALL_FEAT] + [(FEAT, {"numbers": True}, None, "progression-designer: B2-tables")]
        for name, extra, on, label in cases:
            with self.subTest(script=name, craft=label):
                off = self.done(run(name, args(name, stage="build")))
                self.assertEqual(index(off["labels"], re.escape(label)), -1, "off by default (fakes: false / [])")
                lit = self.done(run(name, args(name, stage="build", **extra), {"set": on} if on else {}))
                self.assertGreaterEqual(index(lit["labels"], re.escape(label)), 0)

    def test_feature_images_are_needed_only_when_the_presentation_list_names_ui_or_vfx(self):
        clean = self.done(run(FEAT, args(FEAT, stage="build", images=None)))
        self.assertGreaterEqual(index(clean["labels"], r"^feature-builder: B7-build$"), 0)
        for role in ("ui-ux-designer", "vfx-designer"):
            with self.subTest(role=role):
                out = run(FEAT, args(FEAT, stage="build", images=None), {"set": {"presentation": [role]}})
                self.assertEqual(out["status"], "blocked")
                self.assertEqual(out["labels"], ["qa-lead: B1-acceptance"])

    # ------------------------------------------------------------------ §3: direction = plan, needs and limits, merge
    def test_direction_is_one_plan_run_then_parallel_tables_then_one_merge(self):
        expect = {FEAT: {"architect: N1-limits-architect"}, UI: {"feature-builder: N1-needs-feature-builder", "sound-designer: N1-needs-sound-designer", "architect: N1-limits-architect"}}
        for name in (FEAT, UI):
            with self.subTest(script=name):
                out = self.done(run(name, args(name, stage="direction"), {"timeline": True, "uniform": True, "dump": r": N1-"}))
                self.assertEqual(out["labels"][0], f"{LEAD[name]}: D1-plan")
                self.assertEqual(out["labels"][-1], f"{LEAD[name]}: D3-merge")
                self.assertEqual(set(out["labels"][1:-1]), expect[name])
                n1 = [t for t in out["timeline"] if ": N1-" in t["label"]]
                self.assertLess(max(t["start"] for t in n1), min(t["end"] for t in n1), "the tables are written in parallel")
                for d in out["dumps"]:
                    inputs = block(d["prompt"], "inputs")
                    self.assertEqual(len(inputs), 1, f"{d['label']} reads only the plan: {inputs}")
                    self.assertIn(PLAN[name] + "@rev", inputs[0])
                    self.assertIn("templates/jobs/needs-table.md", d["prompt"])
                    self.assertIn("at most 12 rows", d["prompt"])
                    self.assertIn('"omitted: <ids>"', d["prompt"])
        mkt = self.done(run(MKT, args(MKT, stage="direction")))
        self.assertEqual(mkt["labels"], ["marketing: D1-plan"], "no table: D1 writes direction.md, no merge")
        launch = self.done(run(MKT, args(MKT, stage="direction", launch=True), {"dump": r": N1-"}))
        self.assertEqual(launch["labels"], ["marketing: D1-plan", "art-director: N1-limits-art-director", "marketing: D3-merge"])
        self.assertEqual(len(block(brief(launch, r"N1-"), "inputs")), 1)
        money = self.done(run(FEAT, args(FEAT, stage="direction", money=True), {"dump": r"N1-limits-architect"}))
        self.assertIn("data-saving", brief(money, r"N1-limits-architect"), "money keeps its skills and rules")
        self.assertIn("Money (platform-policy)", brief(money, r"N1-limits-architect"))

    def test_conditional_direction_tables_switch_on_and_off(self):
        cases = [(UI, {}, {"ui_effects": True}, "vfx-designer: N1-needs"), (UI, {"shop": True}, None, "progression-designer: N1-limits"),
                 (UI, {"newLook": True}, None, "art-director: N1-limits"), (FEAT, {"numbers": True}, None, "progression-designer: N1-limits"),
                 (FEAT, {"risks": ["rewards"]}, None, "progression-designer: N1-limits"), (MKT, {"trends": True}, None, "trend-scout: N1-limits"),
                 (MKT, {}, {"hero_is_character": True}, "animator: N1-needs")] + [(FEAT, {}, {"presentation": [r]}, f"{r}: N1-needs") for r in ALL_FEAT]
        for name, extra, on, label in cases:
            with self.subTest(script=name, table=label):
                self.assertEqual(index(self.done(run(name, args(name, stage="direction")))["labels"], label), -1)
                self.assertGreaterEqual(index(self.done(run(name, args(name, stage="direction", **extra), {"set": on} if on else {}))["labels"], label), 0)

    def test_second_needs_round_runs_only_on_a_conflict_the_merge_reports(self):
        cases = {FEAT: ({}, "architect"), UI: ({}, "sound-designer"), MKT: ({"launch": True}, "art-director")}
        for name, (extra, role) in cases.items():
            with self.subTest(script=name):
                clean = self.done(run(name, args(name, stage="direction", **extra)))
                self.assertEqual(index(clean["labels"], r": N2-|D3-merge-n2"), -1)
                conflict = run(name, args(name, stage="direction", **extra), {"set": {"open_conflicts": [{"about": "N1-row-3", "roles": [role], "why": "w"}]}, "dump": r": N2-"})
                self.assertEqual(labels_of(conflict, r": N2-"), [f"{role}: N2-{role}"], "only the crafts in the conflict answer")
                self.assertEqual(conflict["labels"][-1], f"{LEAD[name]}: D3-merge-n2")
                self.assertEqual(len(labels_of(conflict, r"D3-merge")), 2, "never more than 2 needs rounds")
                self.assertEqual(conflict["status"], "needs-decision", "a conflict open after round 2 is an owner decision")
                self.assertIn("conflicting_rows:", brief(conflict, r": N2-"))

    def test_first_build_hand_back_of_each_craft_confirms_the_merged_plan(self):
        out = self.done(run(UI, args(UI, stage="build"), {"blockLabelOnce": r"^ui-ux-designer: RV-candidate-r0", "maker": "sound-designer", "dump": r"^(sound-designer|feature-builder): "}))
        for role in ("sound-designer", "feature-builder"):
            with self.subTest(role=role):
                mine = [d["prompt"] for d in out["dumps"] if d["label"].startswith(f"{role}: ")]
                self.assertIn("PLAN-CONFIRM", mine[0])
                self.assertTrue(all("PLAN-CONFIRM" not in p for p in mine[1:]), "asked once")
        stop = run(FEAT, args(FEAT, stage="build"), {"statusLabel": r"^qa-lead: B1-acceptance", "status": "needs-decision"})
        self.assertEqual(stop["status"], "needs-decision")
        self.assertEqual(index(stop["labels"], r"feature-builder: "), -1)

    def test_a_dead_table_or_capture_is_never_a_pass(self):
        cases = [(FEAT, {}, r"^architect: N1-"), (UI, {}, r"^sound-designer: N1-"), (MKT, {"launch": True}, r"^art-director: N1-")]
        for name, extra, label in cases:
            with self.subTest(script=name, label=label):
                out = run(name, args(name, stage="direction", **extra), {"nullLabel": label})
                self.assertEqual(out["status"], "failed")
                self.assertEqual(index(out["labels"], r"D3-merge"), -1)
        for name, label in ((FEAT, r"^studio-operator: RV-candidate-r0-capture"), (UI, r"^studio-operator: RV-candidate-r0-capture")):
            with self.subTest(script=name, label=label):
                out = run(name, args(name, stage="build"), {"nullLabel": label})
                self.assertEqual(out["status"], "failed")
                self.assertEqual(self.round0(out), set())

    # ------------------------------------------------------------------ §4: capture and scripts, the reviewer table
    def test_capture_and_scripts_is_one_sonnet_run_per_round_with_visual_flags_and_cue_log(self):
        for name in TYPES:
            with self.subTest(script=name):
                out = self.done(run(name, args(name, stage="build"), {"blockLabelOnce": rf"^{LEAD[name]}: RV-candidate-r0", "maker": LEAD[name] if name != FEAT else "vfx-designer", "dump": r"^studio-operator: "}))
                for rd in (0, 1):
                    self.assertEqual(len(labels_of(out, rf"^studio-operator: RV-candidate-r{rd}-")), 1)
                self.assertEqual(len(labels_of(out, r"^studio-operator: ")), 2, "no other capture or probe run")
                for d in out["dumps"]:
                    self.assertIn("model: sonnet", d["prompt"])
                    self.assertIn("visual_flags", d["returned"])
                    self.assertIn("cue_log", d["returned"])

    def test_a_scripts_fail_holds_back_every_review_until_it_is_fixed(self):
        for name, maker in ((FEAT, "feature-builder"), (UI, "feature-builder"), (MKT, "marketing")):
            with self.subTest(script=name):
                out = self.done(run(name, args(name, stage="build"), {"blockLabelOnce": r"^studio-operator: RV-candidate-r0-", "maker": maker}))
                self.assertEqual(self.round0(out), set())
                self.assertEqual(roles_of(out, r": RV-candidate-r1-") - {"studio-operator"}, self.round0(self.done(run(name, args(name, stage="build")))))

    def test_round_zero_reviewers_follow_the_table(self):
        never = {FEAT: {"architect", "progression-designer", "sound-designer", "animator", "vfx-designer", "ui-ux-designer", "feature-builder"},
                 UI: {"game-designer", "progression-designer", "sound-designer", "architect", "feature-builder", "vfx-designer"},
                 MKT: {"game-designer", "trend-scout", "animator"}}
        base = {FEAT: {"game-designer", "reviewer", "qa-lead"}, UI: {"ui-ux-designer", "reviewer"}, MKT: {"marketing"}}
        switches = {
            FEAT: [({"risks": ["performance"]}, None, "performance-engineer"), ({"risks": ["event"]}, None, "live-ops-designer"), ({}, {"visual_flags": ["x"]}, "art-director")],
            UI: [({"shop": True}, None, "qa-lead"), ({"risks": ["paid-random"]}, None, "qa-lead"), ({"risks": ["server-result"]}, None, "qa-lead"), ({"risks": ["shop-screen"]}, None, "qa-lead"),
                 ({"newLook": True}, None, "art-director"), ({}, {"visual_flags": ["x"]}, "art-director"), ({"risks": ["performance"]}, None, "performance-engineer"), ({"risks": ["event"]}, None, "live-ops-designer")],
            MKT: [({"launch": True}, None, "art-director"), ({}, {"visual_flags": ["x"]}, "art-director"), ({"risks": ["event"]}, None, "live-ops-designer")],
        }
        for name in TYPES:
            with self.subTest(script=name, case="cheapest"):
                self.assertEqual(self.round0(self.done(run(name, args(name, stage="build")))), base[name])
            for extra, on, role in switches[name]:
                with self.subTest(script=name, reviewer=role, extra=extra, on=on):
                    got = self.round0(self.done(run(name, args(name, stage="build", **extra), {"set": on} if on else {})))
                    self.assertEqual(got, base[name] | {role})
                    self.assertFalse(got & never[name], "a removed reviewer runs")

    def test_performance_is_a_universal_risk_token(self):
        for name in TYPES:
            with self.subTest(script=name):
                for stage in ("direction", "build"):
                    self.done(run(name, args(name, stage=stage, risks=["performance"])))
                bad = run(name, args(name, stage="build", risks=["performance", "speed"]))
                self.assertEqual((bad["status"], bad["agents"]), ("blocked", 0))
                self.assertIn("performance", bad["outcome"], "the refusal names the accepted tokens")

    # ------------------------------------------------------------------ §4.5: selective recheck
    def test_a_later_round_reruns_only_the_capture_the_qa_lead_the_failed_reviewer_and_dependents(self):
        cases = [
            (FEAT, {}, r"^game-designer: RV-candidate-r0", "vfx-designer", {"studio-operator", "qa-lead", "game-designer"}, ["reviewer"]),
            (FEAT, {}, r"^qa-lead: RV-candidate-r0", "feature-builder", {"studio-operator", "qa-lead", "reviewer"}, ["game-designer"]),
            (FEAT, {}, r"^reviewer: RV-candidate-r0", "progression-designer", {"studio-operator", "qa-lead", "reviewer"}, ["game-designer"]),
            (UI, {"shop": True}, r"^ui-ux-designer: RV-candidate-r0", "sound-designer", {"studio-operator", "qa-lead", "ui-ux-designer"}, ["reviewer"]),
            (UI, {"shop": True}, r"^reviewer: RV-candidate-r0", "feature-builder", {"studio-operator", "qa-lead", "reviewer"}, ["ui-ux-designer"]),
            (UI, {"newLook": True}, r"^reviewer: RV-candidate-r0", "ui-ux-designer", {"studio-operator", "reviewer", "ui-ux-designer", "art-director"}, []),
            (UI, {}, r"^ui-ux-designer: RV-candidate-r0", "ui-ux-designer", {"studio-operator", "ui-ux-designer"}, ["reviewer"]),
            (MKT, {"launch": True, "risks": ["event"]}, r"^marketing: RV-candidate-r0", "marketing", {"studio-operator", "marketing", "art-director"}, ["live-ops-designer"]),
            (MKT, {"risks": ["event"]}, r"^live-ops-designer: RV-candidate-r0", "marketing", {"studio-operator", "marketing", "live-ops-designer"}, []),
        ]
        for name, extra, block_on, maker, again, carried in cases:
            with self.subTest(script=name, block=block_on, maker=maker):
                out = self.done(run(name, args(name, stage="build", **extra), {"blockLabelOnce": block_on, "maker": maker}))
                self.assertEqual(roles_of(out, r": RV-candidate-r1-"), again)
                for role in carried:
                    self.assertTrue(any(c.startswith(f"carried: {role} (round 0, revision ") for c in out["result"]["carried"]), out["result"]["carried"])
                if name == UI and "newLook" not in extra:
                    self.assertFalse(any("art-director" in c for c in out["result"]["carried"]), "the art-director is not in this chain")

    # ------------------------------------------------------------------ §5a: capped repair and recheck briefs
    def test_repair_briefs_carry_only_own_findings_capped_with_changed_and_protected_lists(self):
        for name, maker in ((FEAT, "feature-builder"), (UI, "feature-builder"), (MKT, "marketing")):
            with self.subTest(script=name):
                out = run(name, args(name, stage="build"), {"set": {"findings": findings(maker, 12)}, "dump": rf"^{maker}: FIX-candidate-r0-"})
                text = brief(out, r"FIX-candidate-r0-")
                self.assertEqual(len(re.findall(r'^  - \{"id":', text, re.M)), 10, "at most 10 findings")
                self.assertRegex(text, r"(?m)^omitted: F11, F12 \(lower rank, sent next round if still open\)$")
                self.assertIn("\nchanged:   # the parts changed since you last worked", text)
                self.assertIn("\nprotected: [", text)
                self.assertNotIn("smallest_fix", text.split("findings:", 1)[1].split("\nowns:")[0], "only id, where, expected, observed, evidence")
                self.assertFalse(any("/reviews/" in x for x in block(text, "inputs")), "never the other reviewers' review files")
                self.assertLessEqual(len(text.split()), 1500)

    def test_a_rechecking_reviewer_gets_its_own_findings_and_the_changed_parts(self):
        for name, reviewer, maker in ((FEAT, "game-designer", "vfx-designer"), (UI, "ui-ux-designer", "sound-designer"), (MKT, "marketing", "marketing")):
            with self.subTest(script=name):
                out = self.done(run(name, args(name, stage="build"), {"blockLabelOnce": rf"^{reviewer}: RV-candidate-r0", "maker": maker, "dump": rf"^{reviewer}: RV-candidate-r1-"}))
                text = brief(out, r"RV-candidate-r1-")
                self.assertIn('{"id":"F1"', text)
                self.assertIn("\nchanged:   # the parts changed since you last worked", text)
                self.assertFalse(any("/reviews/" in x for x in block(text, "inputs")))
                self.assertIn("captures" if name != MKT else "checks/candidate-r1/", "\n".join(block(text, "inputs")), "the fresh capture")

    # ------------------------------------------------------------------ §6: the run counts
    def test_minimum_and_typical_run_counts_meet_the_targets(self):
        ceilings = {(FEAT, "min"): 9, (FEAT, "typ"): 11, (UI, "min"): 11, (UI, "typ"): 13, (MKT, "min"): 4, (MKT, "typ"): 4}
        for (name, kind), ceiling in ceilings.items():
            flags = MIN[name] if kind == "min" else TYP[name]
            totals = {}
            for size in ("L", "M"):
                totals[size] = sum(self.done(run(name, full(name, stage=st, size=size, **flags)))["agents"] for st in ("direction", "build"))
            with self.subTest(script=name, kind=kind):
                self.assertLessEqual(totals["L"], ceiling)
                self.assertLessEqual(totals["M"], totals["L"])


if __name__ == "__main__":
    unittest.main()
