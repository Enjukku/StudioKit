"""Control-flow tests for the saved job workflows (.agents/workflows/jobs/*.js) with fake agents (no tokens).

Kit test (universal). Author: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016); revised by workflow-fixer W3 ·
claude-opus-5-5 · high · 2026-10-21, J016 G3 (audit fixes: auditor B F1-F16 and R1-R13, auditor E TT-02..TT-12, lead decisions LD1-LD15).
Runs tools/workflows/wf_harness.mjs under Node; skipped when Node is not installed.
Every workflow must: refuse bad or missing args before any agent starts (no silent defaults); run each stage to `done` with clean
fakes; keep the harness contract on every agent() call (role, model on its tier, effort, the hand-back schema of
templates/jobs/handback.schema.json, a well-formed brief, at most 5 agents at once, one Studio driver, one Blender user and one browser
user at a time); stop with `needs-decision` when review findings never clear; never count a dead agent as a pass.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
JOBS = ROOT / ".agents" / "workflows" / "jobs"
HARNESS = ROOT / "tools" / "workflows" / "wf_harness.mjs"
TEMPLATE = ROOT / "templates" / "jobs" / "handback.schema.json"
NODE = shutil.which("node")
STAGES = ("direction", "proof", "build", "repair")
LATER = ("proof", "build", "repair")

# Complete args per workflow (the README args table); every test starts from these and changes one thing.
BASE = {"job": "J099-test", "studioId": "studio-1", "change": "make it slower", "images": ["content/art/refs/approved.png"], "size": "L",
        "risks": []}
EXTRA = {
    "job-cutscene.js": {},
    "job-character.js": {"variant": False, "playable": True, "base": "archer"},
    "job-stage.js": {},
    "job-ui-screen.js": {"shop": True, "newLook": False},
    "job-feature.js": {"money": True, "numbers": True},
    "job-effect.js": {"newLook": False, "animated": True},
    "job-marketing-art.js": {"piece": "thumbnails", "launch": False},
}
# Lead decision LD9: args that switch rules or gates, and the stages that need them (a missing one is `blocked`, 0 agents).
REQUIRED = {
    "job-cutscene.js": {"size": STAGES, "risks": STAGES, "studioId": LATER, "images": LATER, "change": ("repair",)},
    "job-character.js": {"size": STAGES, "risks": STAGES, "variant": STAGES, "playable": STAGES, "studioId": LATER, "images": LATER, "change": ("repair",)},
    "job-stage.js": {"size": STAGES, "risks": STAGES, "studioId": LATER, "images": ("build", "repair"), "change": ("repair",)},
    "job-ui-screen.js": {"size": STAGES, "risks": STAGES, "shop": STAGES, "newLook": STAGES, "images": LATER, "studioId": ("build", "repair"), "change": ("repair",)},
    "job-feature.js": {"size": STAGES, "risks": STAGES, "money": STAGES, "numbers": STAGES, "studioId": LATER, "change": ("repair",)},
    "job-effect.js": {"size": STAGES, "risks": STAGES, "newLook": STAGES, "animated": STAGES, "studioId": LATER, "images": LATER, "change": ("repair",)},
    "job-marketing-art.js": {"size": STAGES, "risks": STAGES, "piece": STAGES, "launch": STAGES, "images": LATER, "change": ("repair",)},
}
# A maker each workflow routes repairs to (for the bounded-rounds test).
MAKER = {"job-cutscene.js": "vfx-designer", "job-character.js": "modeler", "job-stage.js": "environment-designer",
         "job-ui-screen.js": "ui-ux-designer", "job-feature.js": "game-designer", "job-effect.js": "vfx-designer",
         "job-marketing-art.js": "marketing"}
# A creative review label pattern per workflow, used to kill one review (R1).
REVIEW = {"job-cutscene.js": r"art-director: RV-candidate-r0", "job-character.js": r"art-director: RV-candidate-r0",
          "job-stage.js": r"art-director: RV-candidate-r0", "job-ui-screen.js": r"art-director: RV-candidate-r0",
          "job-feature.js": r"game-designer: RV-candidate-r0", "job-effect.js": r"art-director: RV-candidate-r0",
          "job-marketing-art.js": r"art-director: RV-candidate-r0"}


def run(script: Path | str, args: dict, scenario: dict | None = None) -> dict:
    script = JOBS / script if isinstance(script, str) else script
    proc = subprocess.run(
        [NODE, str(HARNESS), str(script), json.dumps(args), json.dumps(scenario or {})],
        capture_output=True, text=True, timeout=120, encoding="utf-8",
    )
    if proc.returncode not in (0, 1) or not proc.stdout.strip():
        raise AssertionError(f"{script.name}: harness error {proc.returncode}: {proc.stderr.strip()}")
    return json.loads(proc.stdout.strip().splitlines()[-1])


def full(name: str, **changes) -> dict:
    a = dict(BASE, **EXTRA[name])
    a.update(changes)
    return {k: v for k, v in a.items() if v is not None}


def index(labels: list[str], pattern: str) -> int:
    for i, label in enumerate(labels):
        if re.search(pattern, label):
            return i
    return -1


def span(out: dict, pattern: str) -> dict:
    hits = [t for t in out["timeline"] if re.search(pattern, t["label"])]
    if not hits:
        raise AssertionError(f"no call matches {pattern}: {out['labels']}")
    return hits[0]


@unittest.skipIf(NODE is None, "Node.js not installed")
class JobWorkflowTests(unittest.TestCase):
    def scripts(self) -> list[Path]:
        found = sorted(JOBS.glob("*.js"))
        self.assertTrue(found, "no job workflows found")
        self.assertEqual({p.name for p in found}, set(EXTRA), "a workflow was added or removed: update EXTRA and REQUIRED")
        return found

    def runs(self, jobs: list[tuple]) -> list[dict]:
        with ThreadPoolExecutor(max_workers=8) as pool:
            return list(pool.map(lambda j: run(*j), jobs))

    # ------------------------------------------------------------------ args (LD9, R2, R7, F14)
    def test_bad_args_are_refused_before_any_agent(self):
        for script in self.scripts():
            with self.subTest(script=script.name):
                out = run(script, {"job": "J099-test"})
                self.assertEqual(out["status"], "blocked")
                self.assertEqual(out["agents"], 0)

    def test_required_args_are_never_silently_defaulted(self):
        jobs, keys = [], []
        for script in self.scripts():
            for arg, stages in REQUIRED[script.name].items():
                for stage in stages:
                    jobs.append((script, full(script.name, stage=stage, **{arg: None})))
                    keys.append((script.name, arg, stage))
        for (name, arg, stage), out in zip(keys, self.runs(jobs)):
            with self.subTest(script=name, arg=arg, stage=stage):
                self.assertEqual(out["status"], "blocked", out["outcome"])
                self.assertEqual(out["agents"], 0)
                self.assertIn(arg, out["outcome"])
                self.assertIn(arg, out["meta"]["whenToUse"], "whenToUse must name every required arg")

    def test_a_look_change_is_never_sized_m(self):
        for name in ("job-ui-screen.js", "job-effect.js"):
            with self.subTest(script=name):
                out = run(name, full(name, stage="build", size="M", newLook=True))
                self.assertEqual(out["status"], "blocked")
                self.assertEqual(out["agents"], 0)
                self.assertIn("sized L", out["outcome"])

    # ------------------------------------------------------------------ clean runs and the harness contract
    def test_every_stage_runs_clean_with_well_formed_briefs(self):
        jobs, keys = [], []
        for script in self.scripts():
            for stage in STAGES:
                for scen in ({}, {"uniform": True}, {"greybox": True, "conflicts": True, "refuseSign": True}):
                    jobs.append((script, full(script.name, stage=stage), scen))
                    keys.append((script.name, stage, json.dumps(scen)))
        for (name, stage, scen), out in zip(keys, self.runs(jobs)):
            with self.subTest(script=name, stage=stage, scenario=scen):
                self.assertEqual(out["violation"], "")
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertGreater(out["agents"], 0)
                self.assertLessEqual(out["maxConcurrent"], 5, "rules/company.md §9: at most 5 agents per stage")

    def test_medium_build_runs_the_proof_inside(self):
        for script in self.scripts():
            with self.subTest(script=script.name):
                large = run(script, full(script.name, stage="build", size="L"))
                medium = run(script, full(script.name, stage="build", size="M"))
                self.assertEqual(medium["violation"], "")
                self.assertEqual(medium["status"], "done", medium["outcome"])
                self.assertGreater(medium["agents"], large["agents"])

    def test_handback_schema_matches_the_template(self):
        template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
        props = list(template["properties"])
        self.assertIn("docs_read", template["required"])
        self.assertNotIn("lesson", template["required"], "the lesson draft is optional (LD11)")
        self.assertLess(props.index("docs_read"), props.index("status"))
        self.assertEqual(props[-2:], ["status", "outcome"], "evidence fields come before the answer fields")
        # The harness fails any agent() call whose schema differs from the template; the clean-run test covers every call.

    def test_a_blocked_step_stops_the_stage(self):
        # Smoke run 2026-10-21: every direction lead returned blocked and the stage still reported the direction sheet ready.
        for script in self.scripts():
            with self.subTest(script=script.name):
                out = run(script, full(script.name, stage="direction"), {"statusLabel": r": D1-", "status": "blocked"})
                self.assertNotEqual(out["status"], "done", "a blocked proposal never yields a direction sheet")
                self.assertEqual(index(out["labels"], r"D3-synthesis"), -1, "no synthesis on missing proposals")

    def test_harness_studio_check_matches_the_workflow_wording(self):
        # The harness's Studio exclusivity check keys on the driver sentence in each workflow's studioRule();
        # if either side drifts, the overlap check would go silent (J016 follow-up review F3).
        found = re.search(r"\['Studio', /(.+?)/\]", HARNESS.read_text(encoding="utf-8"))
        self.assertIsNotNone(found, "the harness has no Studio resource pattern")
        driver = re.compile(found.group(1))
        for name in ("job-cutscene.js", "job-character.js", "job-stage.js", "job-ui-screen.js", "job-feature.js", "job-effect.js"):
            with self.subTest(script=name):
                out = run(name, full(name, stage="build", size="L"), {"dump": ".*"})
                self.assertTrue(any(driver.search(d["prompt"]) for d in out["dumps"]), "no brief matches the harness's Studio driver pattern")

    def test_scripts_are_pure(self):
        banned = [r"Date\.now", r"Math\.random", r"new Date\(\s*\)", r"\brequire\(", r"^\s*import\s", r"\bfs\.", r"readFile", r"writeFile",
                  r"SendMessage", r"agentId", r"\bpeers\s*:"]
        for script in self.scripts():
            src = script.read_text(encoding="utf-8")
            for pat in banned:
                with self.subTest(script=script.name, pattern=pat):
                    self.assertIsNone(re.search(pat, src, re.M), f"{script.name} uses {pat}")

    def test_lesson_drafts_reach_the_lead(self):
        for script in self.scripts():
            with self.subTest(script=script.name):
                out = run(script, full(script.name, stage="direction"), {"lesson": True})
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(len(out["result"]["lessons"]), out["agents"], "every lesson draft is in the stage result (TT-10)")
                self.assertIn("cause", out["result"]["lessons"][0])
                empty = run(script, full(script.name, stage="direction"), {"lesson": "none"})
                self.assertEqual(empty["result"]["lessons"], [], "a lesson of type none is never filed")
                smoke = run(script, full(script.name, stage="direction", smoke=True), {"lesson": True})
                self.assertEqual(smoke["result"]["lessons"], [], "a smoke run files no lessons")

    # ------------------------------------------------------------------ bounded repairs and dead agents (LD5, R1)
    def test_repair_rounds_are_bounded(self):
        for script in self.scripts():
            with self.subTest(script=script.name):
                out = run(script, full(script.name, stage="build"), {"blockAlways": True, "maker": MAKER[script.name]})
                self.assertEqual(out["violation"], "")
                self.assertEqual(out["status"], "needs-decision", out["outcome"])

    def test_a_dead_review_or_signature_is_never_a_pass(self):
        for script in self.scripts():
            with self.subTest(script=script.name, step="review"):
                out = run(script, full(script.name, stage="build"), {"nullLabel": REVIEW[script.name]})
                self.assertNotEqual(out["status"], "done", out["outcome"])
            with self.subTest(script=script.name, step="signature"):
                out = run(script, full(script.name, stage="direction"), {"nullLabel": r"D3-sign-"})
                self.assertEqual(out["status"], "failed", out["outcome"])

    # ------------------------------------------------------------------ images (LD2, F11, F13, TT-02)
    def test_pending_images_are_listed_not_failed(self):
        for script in self.scripts():
            if script.name == "job-feature.js":
                continue   # feature G1 shows player words; its images are made in the proof (next test)
            with self.subTest(script=script.name):
                out = run(script, full(script.name, stage="direction"), {"images": "pending"})
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertTrue(out["result"]["images_pending"], "the stage result lists the pending batches")

    def test_feature_visible_parts_get_images_before_styling(self):
        name = "job-feature.js"
        proof = run(name, full(name, stage="proof"), {"images": "pending"})
        self.assertEqual(proof["status"], "done", proof["outcome"])
        self.assertGreaterEqual(index(proof["labels"], r"ui-ux-designer: P3-ui-target"), 0)
        self.assertGreaterEqual(index(proof["labels"], r"vfx-designer: P3-vfx-keyframes"), 0)
        self.assertEqual(len(proof["result"]["images_pending"]), 2)
        blocked = run(name, full(name, stage="build", images=None))
        self.assertEqual(blocked["status"], "blocked")
        self.assertEqual(index(blocked["labels"], r"B4-ui|B5-vfx"), -1, "no visual build without approved images")
        quiet = run(name, full(name, stage="build", images=None), {"set": {"no_visible_parts": True, "crafts_not_needed": [
            {"role": "ui-ux-designer", "why": "w"}, {"role": "vfx-designer", "why": "w"}, {"role": "sound-designer", "why": "w"}]}})
        self.assertEqual(quiet["status"], "done", quiet["outcome"])

    def test_visual_briefs_carry_the_approved_images(self):
        img = BASE["images"][0]
        out = run("job-cutscene.js", full("job-cutscene.js", stage="build"),
                  {"dump": r"B2-set-rough|B3-blocking|B4-ui|B5-vfx$|B5-vfx-proto"})
        self.assertEqual(len(out["dumps"]), 5)
        for d in out["dumps"]:
            with self.subTest(label=d["label"]):
                self.assertIn(img, d["prompt"])
                self.assertIn("No approved reference image path in refs means no visual build", d["prompt"])
        ui = next(d for d in out["dumps"] if "B4-ui" in d["label"])
        self.assertIn("ui-style-", ui["prompt"], "the cutscene UI loads the game's style book (F13)")
        feat = run("job-feature.js", full("job-feature.js", stage="build"), {"dump": r"B4-ui|B5-vfx"})
        for d in feat["dumps"]:
            with self.subTest(label=d["label"]):
                self.assertIn(img, d["prompt"])
        self.assertIn("ui-style-", next(d for d in feat["dumps"] if "B4-ui" in d["label"])["prompt"])

    def test_one_image_maker_writes_prompts_first(self):
        for script in self.scripts():
            with self.subTest(script=script.name):
                out = run(script, full(script.name, stage="direction"), {"dump": r": D1-"})
                makers = [d for d in out["dumps"] if "write every image prompt first" in d["prompt"]]
                # Marketing makes its roughs in the direction sheet step, the feature makes no G1 pictures; the others have one D1 image maker.
                expected = 0 if script.name in ("job-feature.js", "job-marketing-art.js") else 1
                self.assertEqual(len(makers), expected, "one browser user per step, prompts first")
                for d in makers:
                    self.assertIn("images_approved: false", d["prompt"], "no download without the owner's yes (LD2)")
                    self.assertIn("image-prompts.md", d["prompt"], "one prompts-file name, as reference-images §4 says (N-07)")

    # ------------------------------------------------------------------ repair round 1 (auditor B recheck F11, N1-N3; auditor E recheck N-03)
    def test_direction_completes_with_pending_pictures(self):
        for name in ("job-character.js", "job-stage.js", "job-ui-screen.js"):
            with self.subTest(script=name):
                out = run(name, full(name, stage="direction"), {"images": "pending", "dump": r"D3-synthesis|D3-sign-"})
                self.assertEqual(out["status"], "done", out["outcome"])
                synth = next(d for d in out["dumps"] if "D3-synthesis" in d["label"])["prompt"]
                self.assertIn("pictures on disk or rows in a pending prompts file", synth, "F11: a pending D1 batch must not fail the synthesis check")
                self.assertNotIn("pictures that exist on disk", synth)
                for d in out["dumps"]:
                    if "D3-sign-" in d["label"]:
                        self.assertIn("judge the prompt rows against the art bible", d["prompt"], "N2")

    def test_pending_art_that_later_steps_build_on_stops_the_stage(self):
        cases = [("job-ui-screen.js", dict(stage="build"), r"B1-figma", r"B2-implement"),
                 ("job-character.js", dict(stage="build", size="M"), r"P1-reference-set", r"S0-sheet|P2-blockout|S3-"),
                 ("job-character.js", dict(stage="proof"), r"P1-reference-set", r"S0-sheet|P2-blockout"),
                 ("job-cutscene.js", dict(stage="build", size="M"), r"P4-boards", r"P5-animatic|B1-"),
                 ("job-cutscene.js", dict(stage="proof"), r"P4-boards", r"P3-probes|P5-animatic"),
                 ("job-feature.js", dict(stage="build", size="M", images=["a.png"]), r"P3-ui-target", r"B1-acceptance|PR-r")]
        for name, changes, maker, later in cases:
            with self.subTest(script=name, changes=changes):
                out = run(name, full(name, **changes), {"images": "pending"})
                self.assertEqual(out["status"], "blocked", out["outcome"])
                self.assertGreaterEqual(index(out["labels"], maker), 0)
                self.assertEqual(index(out["labels"], later), -1, "nothing is built or reviewed on unapproved images")
                self.assertTrue(out["result"]["images_pending"])
        # only the kit model sheet is pending, so the run reaches the kit path (the paint-over check would stop it first)
        kit = run("job-stage.js", full("job-stage.js", stage="build"), {"images": "pending", "imagesLabel": r"B2-kit-", "set": {"kit_piece_ids": ["rock-a"]}})
        self.assertEqual(kit["status"], "blocked", kit["outcome"])
        self.assertIn("Kit pieces", kit["outcome"])
        self.assertGreaterEqual(index(kit["labels"], r"B2-kit-rock-a"), 0)
        self.assertEqual(index(kit["labels"], r"B3-light"), -1)

    # ------------------------------------------------------------------ cutscene: the pilot (auditor B F1-F13, auditor E TT-03, TT-04, TT-12)
    def test_cutscene_repair_recaptures_before_review(self):
        out = run("job-cutscene.js", full("job-cutscene.js", stage="repair"), {"affected": ["animator", "vfx-designer"], "timing": True})
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        last_fix = max(i for i, x in enumerate(labels) if ": FIX-repair-" in x)
        first_review = index(labels, r": RV-repair-r0-")
        for pat in (r"animator: IMP-repair", r"film-director: SCN-repair", r"film-director: CAP-repair"):
            with self.subTest(step=pat):
                i = index(labels, pat)
                self.assertTrue(last_fix < i < first_review, labels)
        self.assertGreaterEqual(index(labels, r"sound-designer: FIX-repair-sound-designer"), 0, "a moved beat makes sound recheck")

    def test_cutscene_scripts_run_first_every_round(self):
        out = run("job-cutscene.js", full("job-cutscene.js", stage="build"), {"blockLabelOnce": r"film-director: RV-candidate-r0", "maker": "environment-designer"})
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        for rnd in ("r0", "r1"):
            with self.subTest(round=rnd):
                first = index(labels, rf": RV-candidate-{rnd}-")
                self.assertRegex(labels[first], r"qa-lead: RV-candidate-%s-scripts" % rnd)
        recap = index(labels, r"film-director: CAP-candidate-r0-fix")
        self.assertTrue(index(labels, r"environment-designer: FIX-candidate-r0") < recap < index(labels, r"RV-candidate-r1-scripts"))
        blocked = run("job-cutscene.js", full("job-cutscene.js", stage="build"), {"blockLabelOnce": r"qa-lead: RV-candidate-r0-scripts", "maker": "feature-builder"})
        self.assertEqual(index(blocked["labels"], r"film-director: RV-candidate-r0-film-director"), -1, "creative reviews wait when scripts block")

    def test_cutscene_vfx_and_sound_work_in_sequence(self):
        for stage, pairs in (("proof", [("P2-needs-r1-vfx", "P2-needs-r1-sound"), ("P4-temp-vfx", "P4-temp-sound")]),
                             ("build", [("B1-envelope-vfx", "B1-envelope-sound"), ("B5-vfx-proto", "B5-sound-proto"), ("B5-vfx$", "B5-sound$")])):
            out = run("job-cutscene.js", full("job-cutscene.js", stage=stage), {"timeline": True, "conflicts": True})
            for vfx, sound in pairs:
                with self.subTest(stage=stage, pair=vfx):
                    self.assertGreater(span(out, sound)["start"], span(out, vfx)["end"], "sound reads the finished VFX note")

    def test_cutscene_combined_pass_before_polish(self):
        labels = run("job-cutscene.js", full("job-cutscene.js", stage="build"))["labels"]
        check = index(labels, r"film-director: B3-combined-checkin")
        self.assertGreater(check, index(labels, r"animator: B3-blocking"))
        self.assertGreater(check, index(labels, r"sound-designer: B5-sound-proto"))
        self.assertLess(check, index(labels, r"animator: B3-polish"))
        self.assertLess(index(labels, r"animator: B3-polish"), index(labels, r"vfx-designer: B5-vfx$"))

    def test_cutscene_new_cast_stops_before_the_animatic(self):
        out = run("job-cutscene.js", full("job-cutscene.js", stage="proof"), {"newCast": True})
        self.assertEqual(out["status"], "needs-decision")
        self.assertEqual(index(out["labels"], r"P5-animatic"), -1)
        self.assertEqual(out["agents"], 1)

    def test_cutscene_proof_fix_pins_the_new_beat_sheet(self):
        out = run("job-cutscene.js", full("job-cutscene.js", stage="proof"), {"blockLabelOnce": r"art-director: PR-r1", "maker": "film-director", "dump": r"PR-fix-r1|PR-r2-art"})
        self.assertEqual(out["status"], "done", out["outcome"])
        fix = next(d for d in out["dumps"] if "PR-fix-r1" in d["label"])
        review = next(d for d in out["dumps"] if "PR-r2-art" in d["label"])
        self.assertIn(f"beat-sheet.md@rev{fix['returned']['beat_sheet_revision']}", review["prompt"])
        self.assertIn(f"beat-sheet.md@rev{fix['returned']['beat_sheet_revision']}", out["result"]["beat_sheet"])

    def test_cutscene_player_brief_has_its_contract_spec_and_skills(self):
        out = run("job-cutscene.js", full("job-cutscene.js", stage="build"), {"dump": r"PLY-candidate|B1-player-contract"})
        player = next(d for d in out["dumps"] if "PLY-candidate" in d["label"])["prompt"]
        for text in ("content/ui/test-cutscene/spec.md", "contract-player.md", "Code file owners", "networking-security", "ui-basics",
                     "return blocked with the files you need", "direction.md   # the gameplay state sheet"):
            with self.subTest(text=text):
                self.assertIn(text, player)
        arch = next(d for d in out["dumps"] if "B1-player-contract" in d["label"])["prompt"]
        self.assertIn("Code file owners", arch)

    def test_cutscene_captures_name_what_studio_can_produce(self):
        out = run("job-cutscene.js", full("job-cutscene.js", stage="build"), {"dump": r"CAP-candidate|sound-designer: RV-"})
        for d in out["dumps"]:
            with self.subTest(label=d["label"]):
                self.assertIn("screen_capture gives still images only", d["prompt"])
                self.assertNotIn("capture with sound exists", d["prompt"])

    # ------------------------------------------------------------------ code review (F9, LD15, TT-03), file owners (LD10, TT-04)
    def test_code_review_runs_when_the_candidate_has_code(self):
        cases = [("job-cutscene.js", {}, True), ("job-character.js", {"playable": True}, True), ("job-character.js", {"playable": False}, False),
                 ("job-feature.js", {}, True), ("job-ui-screen.js", {}, True), ("job-effect.js", {}, True)]
        for name, extra, expect in cases:
            for stage in ("build", "repair"):
                with self.subTest(script=name, extra=extra, stage=stage):
                    out = run(name, full(name, stage=stage, **extra), {"affected": [MAKER[name]]})
                    self.assertEqual(out["status"], "done", out["outcome"])
                    has = index(out["labels"], r"^reviewer: (RV|CR)-") >= 0
                    self.assertEqual(has, expect, out["labels"])

    def test_a_blocked_builder_stops_the_stage_before_review(self):
        out = run("job-cutscene.js", full("job-cutscene.js", stage="build"), {"statusLabel": r"PLY-candidate", "status": "blocked"})
        self.assertEqual(out["status"], "blocked", out["outcome"])
        self.assertEqual(index(out["labels"], r": RV-"), -1, "no review runs on a candidate that was never built")

    def test_code_briefs_take_file_owners_from_the_contract(self):
        out = run("job-character.js", full("job-character.js", stage="build", size="M"), {"dump": r"P1-wiring-contract|S7-wiring"})
        wire = next(d for d in out["dumps"] if "S7-wiring" in d["label"])["prompt"]
        self.assertIn("contract-wiring.md@rev", wire)
        self.assertIn("Code file owners", wire)
        self.assertNotIn("the job card names", wire)
        self.assertGreaterEqual(index(out["labels"], r"architect: P1-wiring-contract"), 0)
        ui = run("job-ui-screen.js", full("job-ui-screen.js", stage="build", size="M"), {"dump": r"feature-builder: B2-implement"})
        self.assertEqual(ui["status"], "done", ui["outcome"])
        self.assertLess(index(ui["labels"], r"architect: C3-code-owners"), index(ui["labels"], r"feature-builder: B2-implement"))
        self.assertGreaterEqual(index(ui["labels"], r"architect: C3-code-owners"), 0)
        impl = ui["dumps"][0]["prompt"]
        self.assertIn("contract-code.md", impl)
        self.assertNotIn('listed under "File owners" in', impl)

    # ------------------------------------------------------------------ feature (F15, TT-06, TT-11)
    def test_feature_code_briefs_load_networking_security_without_money(self):
        out = run("job-feature.js", full("job-feature.js", stage="build", money=False), {"dump": r"architect: B1-plan|feature-builder: B2-build|reviewer: RV-"})
        self.assertEqual(len(out["dumps"]), 3)
        for d in out["dumps"]:
            with self.subTest(label=d["label"]):
                self.assertRegex(d["prompt"], r"skills: \[[^\]]*networking-security")

    def test_feature_vfx_and_sound_work_in_sequence(self):
        for stage, pairs in (("proof", [("P2-needs-r1-vfx", "P2-needs-r1-sound")]), ("build", [("B5-vfx", "B6-sound")])):
            out = run("job-feature.js", full("job-feature.js", stage=stage), {"timeline": True})
            for vfx, sound in pairs:
                with self.subTest(stage=stage, pair=vfx):
                    self.assertGreater(span(out, sound)["start"], span(out, vfx)["end"])

    def test_shared_cues_run_vfx_before_sound_in_every_workflow(self):
        cases = [("job-ui-screen.js", "proof", "C2-needs-r1-vfx", "C2-needs-r1-sound"), ("job-ui-screen.js", "build", "B4-ui-effects", "B3-ui-sounds"),
                 ("job-stage.js", "proof", "P3-needs-r1-vfx", "P3-needs-r1-sound"), ("job-stage.js", "build", "B4-ambience-vfx", "B4-ambience-sound"),
                 ("job-character.js", "build", "S7-vfx", "S7-sound"), ("job-effect.js", "proof", "E-r1-vfx", "E-r1-sound")]
        for name, stage, vfx, sound in cases:
            with self.subTest(script=name, stage=stage, pair=vfx):
                extra = {"playable": False} if name == "job-character.js" else {}
                out = run(name, full(name, stage=stage, **extra), {"timeline": True})
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertGreater(span(out, sound)["start"], span(out, vfx)["end"])

    def test_capture_briefs_carry_the_check_budget(self):
        for name, pat in (("job-feature.js", r"studio-operator: (P4-play|RV-.*-capture)"), ("job-cutscene.js", r"CAP-candidate"),
                          ("job-ui-screen.js", r"B6-capture"), ("job-effect.js", r"CAP-candidate"), ("job-stage.js", r"PT-")):
            with self.subTest(script=name):
                out = run(name, full(name, stage="build"), {"dump": pat})
                self.assertTrue(out["dumps"])
                for d in out["dumps"]:
                    self.assertIn("Check budget (owner J005-D8)", d["prompt"])

    # ------------------------------------------------------------------ others
    def test_stage_capture_findings_reach_the_next_playtest(self):
        out = run("job-stage.js", full("job-stage.js", stage="build"), {"blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "studio-operator", "dump": r"PT-candidate-r1-record"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(index(out["labels"], r"FIX-candidate-r0-studio-operator"), -1)
        self.assertIn("capture gaps", out["dumps"][0]["prompt"])

    def test_character_palette_only_variant_skips_the_rig_steps(self):
        name = "job-character.js"
        palette = run(name, full(name, stage="build", variant=True), {"set": {"geometry_changed": False}})
        self.assertEqual(palette["status"], "done", palette["outcome"])
        self.assertEqual(index(palette["labels"], r"S4-r0|S5-rig|S6-r0"), -1)
        reshaped = run(name, full(name, stage="build", variant=True), {"set": {"geometry_changed": True}})
        self.assertGreaterEqual(index(reshaped["labels"], r"S4-r0"), 0)

    def test_marketing_slot_size_rerun_is_fresh(self):
        out = run("job-marketing-art.js", full("job-marketing-art.js", stage="direction"), {"set": {"slot_sizes_missing": ["Home tile"]}})
        self.assertEqual(out["status"], "needs-decision")
        self.assertIn("fresh", out["outcome"])
        self.assertNotIn("resume from cache", out["outcome"])


if __name__ == "__main__":
    unittest.main()
