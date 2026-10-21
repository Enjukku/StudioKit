"""Control-flow tests for the saved job workflows (.agents/workflows/jobs/*.js) with fake agents (no tokens).

Kit test (universal). Author: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016).
Runs tools/workflows/wf_harness.mjs under Node; skipped when Node is not installed.
Every workflow must: refuse bad args before any agent starts; run each stage to `done` with clean fakes;
stop with `needs-decision` when review findings never clear (bounded repair rounds); and give every
agent() call a role, model, effort, schema and a brief with <intent>, <spec> and checks.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
JOBS = ROOT / ".agents" / "workflows" / "jobs"
HARNESS = ROOT / "tools" / "workflows" / "wf_harness.mjs"
NODE = shutil.which("node")


def run(script: Path, args: dict, scenario: dict | None = None) -> dict:
    proc = subprocess.run(
        [NODE, str(HARNESS), str(script), json.dumps(args), json.dumps(scenario or {})],
        capture_output=True, text=True, timeout=60,
    )
    if proc.returncode not in (0, 1) or not proc.stdout.strip():
        raise AssertionError(f"{script.name}: harness error {proc.returncode}: {proc.stderr.strip()}")
    return json.loads(proc.stdout.strip().splitlines()[-1])


@unittest.skipIf(NODE is None, "Node.js not installed")
class JobWorkflowTests(unittest.TestCase):
    def scripts(self) -> list[Path]:
        found = sorted(JOBS.glob("*.js"))
        self.assertTrue(found, "no job workflows found")
        return found

    def test_bad_args_are_refused_before_any_agent(self):
        for script in self.scripts():
            with self.subTest(script=script.name):
                out = run(script, {"job": "J099-test"})
                self.assertEqual(out["status"], "blocked")
                self.assertEqual(out["agents"], 0)

    def test_every_stage_runs_clean_with_well_formed_briefs(self):
        base = {"job": "J099-test", "studioId": "studio-1", "change": "make it slower"}
        for script in self.scripts():
            for stage in ("direction", "proof", "build", "repair"):
                with self.subTest(script=script.name, stage=stage):
                    out = run(script, dict(base, stage=stage), {"affected": []})
                    self.assertEqual(out["violation"], "")
                    self.assertEqual(out["status"], "done", out["outcome"])
                    self.assertGreater(out["agents"], 0)

    def test_medium_build_runs_the_proof_inside(self):
        for script in self.scripts():
            with self.subTest(script=script.name):
                large = run(script, {"job": "J099-test", "studioId": "studio-1", "stage": "build", "size": "L"})
                medium = run(script, {"job": "J099-test", "studioId": "studio-1", "stage": "build", "size": "M"})
                self.assertEqual(medium["violation"], "")
                self.assertEqual(medium["status"], "done", medium["outcome"])
                self.assertGreater(medium["agents"], large["agents"])

    def test_repair_rounds_are_bounded(self):
        for script in self.scripts():
            with self.subTest(script=script.name):
                out = run(script, {"job": "J099-test", "studioId": "studio-1", "stage": "build"}, {"blockAlways": True})
                self.assertEqual(out["status"], "needs-decision")


if __name__ == "__main__":
    unittest.main()
