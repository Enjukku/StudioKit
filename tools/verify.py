#!/usr/bin/env python3
"""The kit gate (cross-platform). Prints one line per check, then `RESULT: PASS` or `RESULT: FAIL`.

Kit tool: universal (Studio Kit). Python 3.11+ standard library only.

Checks, in order:
  a  python tools/sync_harness.py --check           generated harness files match their sources
  b  python tools/kb_index.py --lint, then --check   only if tools/kb_index.py exists, else "skip"
  c  every tools/tests/test_*.py (unittest discovery) skipped with --fast
  d  always-loaded size: lines of CLAUDE.md + every @import it pulls in (recursive, max depth 4,
     each file counted once) <= 200
  e  every SKILL.md under .agents/skills and .claude/skills <= 500 lines
  f  every .agents/skills/*/SKILL.md frontmatter `description` <= 400 characters (J016-D4: the
     skill list budget drops long descriptions); FAIL lists each skill and its length

Usage: python tools/verify.py [--fast] [--root DIR]
Exit codes: 0 PASS, 1 FAIL.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from context_packet import parse_frontmatter  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ALWAYS_LOADED_MAX = 200
SKILL_MAX = 500
DESCRIPTION_MAX = 400
IMPORT_DEPTH = 4
TIMEOUT = 600
# Claude Code memory imports: @path tokens outside code spans and fences.
IMPORT_RE = re.compile(r"(?<![\w`@/])@([~.\w][\w./\\~-]*)")
CODE_SPAN = re.compile(r"`[^`\n]*`")


def _lines(text: str) -> int:
    return len(text.splitlines())


def find_imports(text: str) -> list[str]:
    found: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for m in IMPORT_RE.finditer(CODE_SPAN.sub("", line)):
            ref = m.group(1).rstrip(".,;:")
            if "/" in ref or "\\" in ref or "." in ref:
                found.append(ref)
    return found


def always_loaded(root: Path, entry: str = "CLAUDE.md") -> tuple[int, list[tuple[str, int]], list[str]]:
    """Return (total lines, [(file, lines)], [missing imports]) for the entry file and its imports."""
    files: list[tuple[str, int]] = []
    missing: list[str] = []
    seen: set[Path] = set()

    def visit(path: Path, depth: int, label: str) -> None:
        resolved = path.resolve()
        if resolved in seen:
            return
        if not path.is_file():
            missing.append(label)
            return
        seen.add(resolved)
        text = path.read_text(encoding="utf-8", errors="replace")
        try:
            name = resolved.relative_to(root.resolve()).as_posix()
        except ValueError:
            name = str(resolved)
        files.append((name, _lines(text)))
        if depth >= IMPORT_DEPTH:
            return
        for ref in find_imports(text):
            target = Path(ref).expanduser() if ref.startswith("~") else path.parent / ref
            visit(target, depth + 1, ref)

    visit(root / entry, 0, entry)
    return sum(n for _, n in files), files, missing


def oversized_skills(root: Path, limit: int = SKILL_MAX) -> list[tuple[str, int]]:
    out = []
    for base in (root / ".agents" / "skills", root / ".claude" / "skills"):
        if base.is_dir():
            for path in sorted(base.rglob("SKILL.md")):
                n = _lines(path.read_text(encoding="utf-8", errors="replace"))
                if n > limit:
                    out.append((path.relative_to(root).as_posix(), n))
    return out


def long_descriptions(root: Path, limit: int = DESCRIPTION_MAX) -> list[tuple[str, int]]:
    """(skill name, description length) for every .agents/skills/*/SKILL.md description over the limit."""
    out = []
    base = root / ".agents" / "skills"
    if base.is_dir():
        for path in sorted(base.glob("*/SKILL.md")):
            meta, _, _ = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
            description = (meta or {}).get("description")
            if isinstance(description, list):
                description = ", ".join(description)
            if isinstance(description, str) and len(description) > limit:
                out.append((path.parent.name, len(description)))
    return out


def _run(root: Path, args: list[str]) -> tuple[int, str]:
    try:
        proc = subprocess.run([sys.executable, *args], cwd=root, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return 1, f"timed out after {TIMEOUT}s"
    text = (proc.stdout + "\n" + proc.stderr).strip()
    return proc.returncode, text


def _summary(text: str, ok: bool) -> str:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if not lines:
        return ""
    if ok:
        return lines[-1][:120]
    return " | ".join(lines[:4])[:300]


def run(root: Path, fast: bool, out=sys.stdout) -> int:
    failed = False

    def report(ok: bool | None, name: str, detail: str = "") -> None:
        nonlocal failed
        status = "skip" if ok is None else ("PASS" if ok else "FAIL")
        failed = failed or ok is False
        print(f"{status:<4} {name}{': ' + detail if detail else ''}", file=out)

    # a
    code, text = _run(root, ["tools/sync_harness.py", "--check"])
    report(code == 0, "sync_harness --check", _summary(text, code == 0))

    # b
    if (root / "tools" / "kb_index.py").is_file():
        for flag in ("--lint", "--check"):
            code, text = _run(root, ["tools/kb_index.py", flag])
            report(code == 0, f"kb_index {flag}", _summary(text, code == 0))
    else:
        report(None, "kb_index", "kb_index not present")

    # c
    if fast:
        report(None, "tests", "--fast")
    elif not any((root / "tools" / "tests").glob("test_*.py")):
        report(None, "tests", "no tools/tests/test_*.py")
    else:
        code, text = _run(root, ["-m", "unittest", "discover", "-s", "tools/tests", "-p", "test_*.py", "-t", "tools/tests"])
        ran = re.findall(r"Ran \d+ tests?", text)
        failures = [ln.strip() for ln in text.splitlines() if ln.startswith(("FAIL:", "ERROR:"))]
        detail = (ran[-1] if ran else "") + ("" if code == 0 else " | " + (" | ".join(failures[:5]) or _summary(text, False)))
        report(code == 0, "tests", detail.strip(" |"))

    # d
    if (root / "CLAUDE.md").is_file():
        total, files, missing = always_loaded(root)
        parts = ", ".join(f"{n} {name}" for name, n in files)
        detail = f"{total}/{ALWAYS_LOADED_MAX} lines ({parts})"
        if missing:
            detail += f"; missing imports: {', '.join(missing)}"
        report(total <= ALWAYS_LOADED_MAX and not missing, "always-loaded size", detail)
    else:
        report(None, "always-loaded size", "no CLAUDE.md")

    # e
    big = oversized_skills(root)
    report(not big, "SKILL.md size",
           f"all <= {SKILL_MAX} lines" if not big else "; ".join(f"{p} {n} lines" for p, n in big))

    # f
    long = long_descriptions(root)
    report(not long, "skill descriptions",
           f"all <= {DESCRIPTION_MAX} characters" if not long
           else f"{len(long)} over {DESCRIPTION_MAX} characters: " + "; ".join(f"{name} {n}" for name, n in long))

    print(f"RESULT: {'FAIL' if failed else 'PASS'}", file=out)
    return 1 if failed else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--fast", action="store_true", help="skip the unit tests (check c)")
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    return run(args.root.resolve(), args.fast)


if __name__ == "__main__":
    raise SystemExit(main())
