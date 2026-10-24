"""Offline tests for tools/usage_report.py (J022). Synthetic transcripts mirror Claude Code's JSONL line shapes.

Run: python tools/tests/test_usage_report.py
"""

from __future__ import annotations

import datetime as dt
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import usage_report as ur  # noqa: E402

NOW = dt.datetime(2026, 10, 20, 12, 0, tzinfo=dt.timezone.utc)
SINCE = NOW - dt.timedelta(days=7)
LIMITS = {"median": 200_000, "peak": 400_000, "images": 2, "calls": 400}


def ts(minutes: int) -> str:
    return (NOW - dt.timedelta(days=1) + dt.timedelta(minutes=minutes)).isoformat().replace("+00:00", "Z")


def call(minute: int, mid: str, context: int, model: str = "claude-opus-5-5", out: int = 10) -> dict:
    usage = {"input_tokens": 5, "cache_creation_input_tokens": 0, "cache_read_input_tokens": context - 5,
             "output_tokens": out}
    return {"type": "assistant", "timestamp": ts(minute),
            "message": {"id": mid, "model": model, "role": "assistant", "usage": usage,
                        "content": [{"type": "text", "text": "ok"}]}}


def image_result(minute: int, n: int) -> dict:
    content = [{"type": "tool_result", "tool_use_id": "t1",
                "content": [{"type": "image", "source": {}}] * n + [{"type": "text", "text": "x"}]}]
    return {"type": "user", "timestamp": ts(minute), "message": {"role": "user", "content": content}}


def compact(minute: int, trigger: str) -> dict:
    return {"type": "system", "subtype": "compact_boundary", "timestamp": ts(minute),
            "compactMetadata": {"trigger": trigger, "preTokens": 900_000}}


def write(path: Path, lines: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(x) for x in lines) + "\n", encoding="utf-8")


class UsageReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.repo = self.tmp / "repo"
        self.repo.mkdir()
        self.projects = self.tmp / "projects"
        base = ur.project_dir(self.repo, self.projects)
        # Main checkout: one session; the same message id twice (streamed blocks share usage), 3 images.
        write(base / "s1.jsonl", [
            {"type": "custom-title", "customTitle": "Core loop"},
            call(0, "m1", 90_000), call(0, "m1", 90_000), image_result(1, 3),
            call(2, "m2", 300_000), call(3, "m3", 500_000), compact(4, "manual"),
        ])
        # A subagent inside a workflow folder: a built-in helper on Opus.
        sub = base / "s1" / "subagents" / "workflows" / "wf_1" / "agent-a1.jsonl"
        write(sub, [call(5, "a1", 80_000), call(6, "a2", 120_000)])
        sub.with_suffix(".meta.json").write_text(json.dumps({"agentType": "general-purpose"}), encoding="utf-8")
        # A worktree folder of the same repository, with an automatic compaction.
        wt = base.parent / (base.name + "--claude-worktrees-j1-ui-abc123")
        write(wt / "s2.jsonl", [call(0, "w1", 450_000), compact(1, "auto"), call(2, "w2", 460_000)])
        # Activity before the window is ignored.
        write(base / "old.jsonl", [{"type": "assistant", "timestamp": "2026-09-01T00:00:00Z",
                                    "message": {"id": "o1", "model": "x", "usage": {"input_tokens": 9}}}])

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def report(self) -> dict:
        return ur.scan(ur.project_dirs(self.repo, self.projects), SINCE, LIMITS)

    def test_counts_one_call_per_message_id(self) -> None:
        s1 = next(r for r in self.report()["sessions"] if r["session"] == "s1")
        self.assertEqual(s1["calls"], 3)
        self.assertEqual((s1["start"], s1["median"], s1["peak"]), (90_000, 300_000, 500_000))
        self.assertEqual(s1["read"], 890_000)
        self.assertEqual(s1["title"], "Core loop")

    def test_images_compactions_and_flags(self) -> None:
        s1 = next(r for r in self.report()["sessions"] if r["session"] == "s1")
        self.assertEqual(s1["images"], 3)
        self.assertEqual((s1["auto_compact"], s1["manual_compact"]), (0, 1))
        self.assertEqual(s1["flags"], ["big context", "no compaction", "many images"])

    def test_worktree_folders_are_included(self) -> None:
        s2 = next(r for r in self.report()["sessions"] if r["session"] == "s2")
        self.assertEqual(s2["place"], "j1-ui-abc123")
        self.assertNotIn("no compaction", s2["flags"], "an automatic compaction clears the flag")
        self.assertIn("big context", s2["flags"])

    def test_workflow_subagents_and_helper_on_opus(self) -> None:
        out = self.report()
        (agent,) = out["agents"]
        self.assertTrue(agent["workflow"])
        self.assertEqual(agent["type"], "general-purpose")
        self.assertEqual(agent["flags"], ["helper on Opus"])
        s1 = next(r for r in out["sessions"] if r["session"] == "s1")
        self.assertEqual((s1["subagents"], s1["sub_read"]), (1, 200_000))

    def test_old_activity_is_outside_the_window(self) -> None:
        self.assertNotIn("old", {r["session"] for r in self.report()["sessions"]})

    def test_render_and_missing_folder(self) -> None:
        text = ur.render(self.report(), SINCE, LIMITS, top=5)
        self.assertIn("| j1-ui-abc123 |", text)
        self.assertIn("- big context: 2", text)
        self.assertEqual(ur.main(["--root", str(self.tmp / "nowhere"), "--projects-dir", str(self.projects)]), 1)


if __name__ == "__main__":
    unittest.main()
