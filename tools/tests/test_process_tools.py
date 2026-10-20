"""Offline tests for tools/improve_scan.py, tools/agent_scorecard.py and tools/verify.py size checks.

Synthetic transcripts mirror Claude Code's JSONL line shapes. Run: python tools/tests/test_process_tools.py
"""

from __future__ import annotations

import contextlib
import datetime as dt
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import agent_scorecard as sc  # noqa: E402
import improve_scan as scan  # noqa: E402
import verify  # noqa: E402

NOW = dt.datetime(2026, 10, 20, 12, 0, tzinfo=dt.timezone.utc)


def ts(minutes: int) -> str:
    return (NOW - dt.timedelta(days=1) + dt.timedelta(minutes=minutes)).isoformat().replace("+00:00", "Z")


def owner(minute: int, text: str) -> dict:
    return {"type": "user", "isSidechain": False, "turnOrigin": "human", "origin": {"kind": "human"},
            "timestamp": ts(minute), "message": {"role": "user", "content": text}}


def assistant(minute: int, mid: str, content: list, model: str = "claude-opus-5-5", tokens: int = 100) -> dict:
    return {"type": "assistant", "timestamp": ts(minute),
            "message": {"id": mid, "model": model, "role": "assistant", "content": content,
                        "usage": {"input_tokens": tokens, "cache_creation_input_tokens": 0,
                                  "output_tokens": 10, "cache_read_input_tokens": 1000}}}


def tool_use(tid: str, name: str, **inp) -> dict:
    return {"type": "tool_use", "id": tid, "name": name, "input": inp}


def tool_result(minute: int, tid: str, body: str, error: bool = False) -> dict:
    block = {"type": "tool_result", "tool_use_id": tid, "content": body}
    if error:
        block["is_error"] = True
    return {"type": "user", "timestamp": ts(minute), "message": {"role": "user", "content": [block]}}


def text(t: str) -> dict:
    return {"type": "text", "text": t}


class Fixture(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="process_tools_"))
        self.repo = self.tmp / "My Game"
        self.repo.mkdir()
        self.projects = self.tmp / "projects"
        self.proj = scan.project_dir(self.repo, self.projects)
        self.proj.mkdir(parents=True)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write_jsonl(self, path: Path, rows: list[dict]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        lines = [json.dumps(r) for r in rows] + ["not json {"]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def subagent(self, session: str, agent_id: str, agent_type: str, rows: list[dict]) -> None:
        base = self.proj / session / "subagents"
        self.write_jsonl(base / f"{agent_id}.jsonl", rows)
        (base / f"{agent_id}.meta.json").write_text(
            json.dumps({"agentType": agent_type, "description": f"brief {agent_id}", "model": "sonnet"}), encoding="utf-8")

    def build_week(self) -> None:
        old = owner(0, "too old to count")
        old["timestamp"] = "2026-09-01T00:00:00Z"
        self.write_jsonl(self.proj / "s1.jsonl", [
            {"type": "custom-title", "customTitle": "Build the shop"},
            old,
            owner(1, "build the shop screen"),
            assistant(2, "m1", [tool_use("t1", "Bash", command="cd /repo && python tools/verify.py --fast")]),
            assistant(2, "m1", [text("Running the gate.")]),  # one message split over lines: count tokens once
            tool_result(3, "t1", "Exit code 1\nFile C:\\x\\y.py line 12 failed", error=True),
            assistant(4, "m2", [tool_use("t2", "Bash", command="python tools/verify.py --fast")]),
            tool_result(5, "t2", "Exit code 1\nFile C:\\a\\b.py line 99 failed", error=True),
            assistant(6, "m3", [tool_use("t3", "AskUserQuestion", questions=[])]),
            tool_result(7, "t3", "User dismissed the question"),
            assistant(8, "m4", [tool_use("t4", "Edit", file_path="x")]),
            tool_result(9, "t4", "The user doesn't want to proceed with this tool use. The tool use was rejected"),
            assistant(10, "m5", [tool_use("t5", "Write", file_path="x")]),
            tool_result(11, "t5", "PreToolUse:Write hook blocking error: write outside scope", error=True),
            {"type": "user", "timestamp": ts(12), "message": {"role": "user", "content": [text("[Request interrupted by user]")]}},
            owner(40, "no, that is wrong, redo the layout"),
            owner(41, "/improve 14"),
            {"type": "user", "turnOrigin": "task_notification", "timestamp": ts(42), "message": {"role": "user", "content": "agent done"}},
        ])
        # builder: finishes with a hand-back, owner corrects within 30 min
        self.subagent("s1", "a1", "builder", [
            assistant(20, "b1", [tool_use("x1", "Read", file_path="a")], model="claude-sonnet-5-5", tokens=1000),
            tool_result(21, "x1", "ok"),
            assistant(30, "b2", [tool_use("x2", "SubagentHandback", message="Status: done. Built it.")], model="claude-sonnet-5-5", tokens=1000),
        ])
        # builder: blocked
        self.subagent("s1", "a2", "builder", [
            assistant(100, "c1", [text("**Status:** blocked. Missing brief.")], model="claude-sonnet-5-5", tokens=3000),
        ])
        # scout: ends on a tool call (failed), one error
        self.subagent("s1", "a3", "scout", [
            assistant(200, "d1", [tool_use("y1", "Grep", pattern="x")], model="claude-haiku-5-5", tokens=50),
            tool_result(201, "y1", "rg: bad regex", error=True),
            assistant(202, "d2", [tool_use("y2", "Grep", pattern="y")], model="claude-haiku-5-5", tokens=50),
        ])


class ImproveScanTests(Fixture):
    def test_project_dir_slug(self) -> None:
        self.assertEqual(scan.project_dir(Path("/home/a b/my.game"), Path("P")), Path("P") / "-home-a-b-my-game")

    def test_digest_counts(self) -> None:
        self.build_week()
        since = NOW - dt.timedelta(days=7)
        out = scan.scan(self.proj, since)
        self.assertEqual(out["interrupts"], 1)
        self.assertEqual(out["dismissed"], 1)
        self.assertEqual(out["rejected"], 1)
        self.assertEqual([x for _, _, x in out["owner"]],
                         ["build the shop screen", "no, that is wrong, redo the layout", "/improve 14"])
        self.assertEqual(out["slash"]["improve"], 1)
        # Two errors differing only in paths and numbers cluster together.
        self.assertEqual(out["tool_errors"]["Bash: Exit code N File <path> line N failed"], 2)
        self.assertEqual(out["tool_errors"]["Grep: rg: bad regex"], 1)  # subagent errors included
        self.assertEqual(len(out["tool_errors"]), 2)
        self.assertEqual(sum(out["denials"].values()), 1)
        self.assertIn("Write", next(iter(out["denials"])))
        self.assertEqual(out["commands"]["python tools/verify.py --fast"], 2)
        self.assertEqual(out["tokens"][("claude-opus-5-5", "new")], 5 * 110)  # m1 counted once
        self.assertEqual(out["agents"]["builder (sonnet)"], 2)
        self.assertEqual(out["agent_tokens"]["builder (sonnet)"], 1010 * 2 + 3010)
        self.assertEqual(out["sessions"][0][1], "Build the shop")

    def test_render_and_json_cli(self) -> None:
        self.build_week()
        md = scan.render(scan.scan(self.proj, NOW - dt.timedelta(days=7)), NOW - dt.timedelta(days=7), 40000)
        self.assertIn("## Owner messages flagged as correction (1)", md)
        self.assertIn("no, that is wrong, redo the layout", md)
        self.assertIn("## Tokens by agent type", md)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = scan.main(["--since", "2026-10-01", "--json", "--root", str(self.repo), "--projects-dir", str(self.projects)])
        self.assertEqual(code, 0)
        data = json.loads(buf.getvalue())
        self.assertEqual(data["interrupts"], 1)
        self.assertEqual(sum(m["correction"] for m in data["owner_messages"]), 1)
        self.assertEqual(data["dismissed_questions"], 1)

    def test_codex_stub_and_missing_dir(self) -> None:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertEqual(scan.main(["--codex"]), 0)
        self.assertIn("Codex transcript scan not implemented", buf.getvalue())
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(scan.main(["--root", str(self.tmp / "nope"), "--projects-dir", str(self.projects)]), 1)


class ScorecardTests(Fixture):
    def test_scores(self) -> None:
        self.build_week()
        roles = self.repo / ".agents" / "roles"
        roles.mkdir(parents=True)
        (roles / "builder.md").write_text("---\nname: builder\n---\nx\n", encoding="utf-8")
        (roles / "idle-one.md").write_text("---\nname: idle-one\n---\nx\n", encoding="utf-8")
        old = (NOW - dt.timedelta(days=60)).timestamp()
        os.utime(roles / "builder.md", (old, old))
        report = sc.build(self.repo, self.projects, 7, dt.date(2026, 10, 1), now=NOW)
        rows = {r["agent"]: r for r in report["agents"]}
        b = rows["builder"]
        self.assertEqual((b["runs"], b["failed"], b["blocked"], b["corrected"]), (2, 0, 1, 1))
        self.assertIs(b["fresh"], False)
        self.assertEqual(b["tokens_total"], 1010 * 2 + 3010)
        # ok 15 + owner 15 + errors 15 + tokens 10*min(1, ref/median) + fresh 0
        ref = report["reference_tokens_median"]
        self.assertEqual(b["score"], round(15 + 15 + 15 + 10 * min(1.0, ref / b["tokens_median"]) + 0))
        self.assertTrue(b["low_evidence"])
        s = rows["scout"]
        self.assertEqual((s["runs"], s["failed"], s["errors"]), (1, 1, 1))
        self.assertIsNone(s["fresh"])  # no role file
        # ok 0 + owner 30 + errors 15*max(0,1-0.5/0.15)=0 + tokens 10 + fresh 15
        self.assertEqual(s["score"], 55)
        self.assertIsNone(rows["idle-one"]["score"])
        self.assertTrue(any("prune" in f for f in rows["idle-one"]["flags"]))

    def test_cli_json(self) -> None:
        self.build_week()
        target = self.tmp / "score.json"
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = sc.main(["--days", "3650", "--root", str(self.repo), "--projects-dir", str(self.projects),
                            "--json", str(target)])
        self.assertEqual(code, 0)
        self.assertIn("# Agent scorecard", buf.getvalue())
        data = json.loads(target.read_text(encoding="utf-8"))
        self.assertEqual({r["agent"] for r in data["agents"]}, {"builder", "scout"})

    def test_score_formula_edges(self) -> None:
        perfect = {"runs": 5, "failed": 0, "blocked": 0, "corrected": 0, "error_rate": 0.0, "tokens_median": 10}
        self.assertEqual(sc.score(perfect, True, 10), 100)
        self.assertEqual(sc.score(perfect, None, 10), 100)
        self.assertEqual(sc.score(perfect, False, 10), 85)
        self.assertEqual(sc.score({**perfect, "tokens_median": 50}, True, 10), 92)
        self.assertIsNone(sc.score({"runs": 0}, True, 10))


class VerifySizeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="verify_"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write(self, rel: str, lines: int, extra: str = "") -> None:
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(extra + "".join(f"line {i}\n" for i in range(lines)), encoding="utf-8")

    def test_imports_recursive_and_ignored_in_code(self) -> None:
        self.write("CLAUDE.md", 3, "@AGENTS.md\n@rules/a.md\n`@rules/code.md`\n```\n@rules/fenced.md\n```\nmail me@x.com\n")
        self.write("AGENTS.md", 10, "@rules/a.md\n")  # duplicate import counted once
        self.write("rules/a.md", 5, "See @b.md.\n")  # relative to the importing file
        self.write("rules/b.md", 7)
        total, files, missing = verify.always_loaded(self.tmp)
        self.assertEqual(missing, [])
        self.assertEqual([f for f, _ in files], ["CLAUDE.md", "AGENTS.md", "rules/a.md", "rules/b.md"])
        self.assertEqual(total, 10 + 11 + 6 + 7)

    def test_depth_limit_and_missing(self) -> None:
        self.write("CLAUDE.md", 0, "@d1.md\n@gone.md\n")
        for i in range(1, 7):
            self.write(f"d{i}.md", 1, f"@d{i + 1}.md\n")
        total, files, missing = verify.always_loaded(self.tmp)
        self.assertEqual(missing, ["gone.md"])
        self.assertEqual([f for f, _ in files], ["CLAUDE.md", "d1.md", "d2.md", "d3.md", "d4.md"])

    def test_oversized_skill(self) -> None:
        self.write(".agents/skills/ok/SKILL.md", 500)
        self.write(".claude/skills/big/SKILL.md", 501)
        self.assertEqual(verify.oversized_skills(self.tmp), [(".claude/skills/big/SKILL.md", 501)])

    def test_gate_fails_on_size(self) -> None:
        self.write("CLAUDE.md", 201)
        self.write("kit.json", 0, json.dumps(json.loads((TOOLS.parent / "kit.json").read_text(encoding="utf-8"))))
        (self.tmp / "tools").mkdir()
        shutil.copy(TOOLS / "sync_harness.py", self.tmp / "tools" / "sync_harness.py")
        buf = io.StringIO()
        code = verify.run(self.tmp, fast=True, out=buf)
        out = buf.getvalue()
        self.assertEqual(code, 1)
        self.assertIn("PASS sync_harness --check", out)
        self.assertIn("skip kb_index: kb_index not present", out)
        self.assertIn("FAIL always-loaded size: 201/200", out)
        self.assertTrue(out.rstrip().endswith("RESULT: FAIL"))


if __name__ == "__main__":
    unittest.main(verbosity=1)
