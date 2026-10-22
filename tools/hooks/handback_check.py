#!/usr/bin/env python3
"""SubagentStop hook: send a kit-role subagent back once when its hand-back lacks STATUS or coverage.

Kit tool (universal). Python 3 standard library only, no network. Spec: J016-T01; format: rules/messages.md §3;
revised by feature-builder · claude-opus-5-5 · high · 2026-10-21, J016 G3 (audit D R4).

Reads the SubagentStop JSON on stdin (fields used: `agent_type`, `stop_hook_active`,
`last_assistant_message`). Only kit roles (stems of .agents/roles/*.md) are checked. The stop is
allowed (no output) when `stop_hook_active` is true (the agent was already sent back once), when the
message has no text to judge (for example a hand-back sent through a tool), or when the first
non-empty line starts with `STATUS:` (after markdown marks such as `**` or `##`) and a line holds a
`coverage:` field (YAML, a list item, bold or a JSON key; the word in a sentence does not count).
Otherwise it prints
    {"decision": "block", "reason": "<REASON>"}
which keeps the subagent running and gives it REASON as its next instruction.

Never fails: on any error it exits 0 with no stdout (the stop goes ahead) and one line on stderr.

Usage (settings.json runs it; see tools/hooks/README.md):
    python tools/hooks/handback_check.py [--root DIR]  < hook-input.json
Exit codes: always 0.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEAD_MARKS = "*_#> " + chr(9)  # markdown bold, heading or quote marks before the first line's STATUS
COVERAGE_RE = re.compile(r'^[\s>*#{-]*["*_]*coverage["*_]*\s*:', re.IGNORECASE | re.MULTILINE)  # a field, not the word in prose
REASON = "Hand-back must start with 'STATUS: done | blocked | needs-decision | failed.' and include coverage (rules/messages.md §3)."
FENCE_RE = re.compile(r"^[ \t]*(`{3,}|~{3,}).*?^[ \t]*\1[ \t]*$", re.MULTILINE | re.DOTALL)


def without_example_blocks(message: str) -> str:
    """The message without fenced code blocks that hold no <spec>: a `coverage:` line inside an example is not the
    hand-back's coverage (J018 orchestration review). A fenced <spec> block is the hand-back format of
    rules/messages.md section 3 and is kept."""
    return FENCE_RE.sub(lambda m: m.group(0) if "<spec>" in m.group(0) else "", message)


def decision_for(payload: dict, root: Path) -> dict | None:
    if payload.get("stop_hook_active") is True:
        return None
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    import context_packet as cp

    role = payload.get("agent_type")
    if not isinstance(role, str) or role not in cp.role_names(root):
        return None
    message = payload.get("last_assistant_message")
    if not isinstance(message, str) or not message.strip():
        return None
    first = next(line.strip() for line in message.splitlines() if line.strip())
    if first.lstrip(LEAD_MARKS).startswith("STATUS:") and COVERAGE_RE.search(without_example_blocks(message)):
        return None
    return {"decision": "block", "reason": REASON}


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    try:
        root = Path(argv[argv.index("--root") + 1]) if "--root" in argv else ROOT
        raw = sys.stdin.buffer.read().decode("utf-8-sig")
        payload = json.loads(raw) if raw.strip() else None
        decision = decision_for(payload, root.resolve()) if isinstance(payload, dict) else None
        if decision:
            sys.stdout.write(json.dumps(decision, ensure_ascii=True) + "\n")
    except Exception as error:  # a hook must never fail; an error lets the stop go ahead
        try:
            sys.stderr.write(f"handback_check: {type(error).__name__}: {error}".replace("\n", " ")[:300] + "\n")
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
