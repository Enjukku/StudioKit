#!/usr/bin/env python3
"""Key registry tool: loads API keys from the owner's key files into a command's environment.

The owner keeps each key in a .txt file on their PC and gives the path. keys.json (repo root) lists, per key,
the environment variable the tools read and the path of its file. Paths only: no key value is ever stored in
the repo, printed, logged or put on a command line by this tool.

  python tools/keys.py list                         every entry: variable, service, file found or not
  python tools/keys.py run [--only VAR ...] -- CMD  run CMD with the keys loaded as environment variables

`run` sets a variable only when it is not already set (a key the owner set with setx wins) and only for the
child process. A file must hold the key on one line; anything else stops `run` before CMD starts (exit 2)
and the message names the path, never the content. Exit codes: run returns CMD's code; 2 = refused.

Python 3.11+ standard library only.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

REGISTRY = Path(__file__).resolve().parent.parent / "keys.json"


class KeyError_(Exception):
    pass


def load_registry(path: Path = REGISTRY) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))["keys"]


def read_key_file(path: str) -> str:
    p = Path(os.path.expandvars(path)).expanduser()
    if not p.is_file():
        raise KeyError_(f"key file not found: {p}")
    lines = [ln.strip() for ln in p.read_text(encoding="utf-8-sig").splitlines() if ln.strip()]
    if len(lines) != 1:
        raise KeyError_(f"key file must hold the key on one line, found {len(lines)} non-empty lines: {p}")
    return lines[0]


def key_env(entries: list[dict], only: list[str] | None, environ: dict[str, str]) -> dict[str, str]:
    """The environment for the child: environ plus every selected key that has a path and is not already set."""
    env = dict(environ)
    wanted = set(only) if only else None
    if wanted:
        unknown = wanted - {e["env"] for e in entries}
        if unknown:
            raise KeyError_(f"not in keys.json: {', '.join(sorted(unknown))}")
    for e in entries:
        name, path = e["env"], e.get("path", "")
        if (wanted and name not in wanted) or env.get(name, "").strip():
            continue
        if not path:
            if wanted:
                raise KeyError_(f"{name}: no key file path in keys.json yet (owner action: give the path)")
            continue
        env[name] = read_key_file(path)
    return env


def cmd_list(entries: list[dict]) -> int:
    for e in entries:
        path = e.get("path", "")
        if os.environ.get(e["env"], "").strip():
            state = "set in environment"
        elif not path:
            state = "no path yet"
        else:
            state = "file found" if Path(os.path.expandvars(path)).expanduser().is_file() else "FILE MISSING"
        print(f"{e['env']:<28} {state:<20} {e['service']}  {path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    run = sub.add_parser("run")
    run.add_argument("--only", nargs="+", metavar="VAR", help="load only these variables (each must have a path)")
    run.add_argument("command", nargs=argparse.REMAINDER, help="-- then the command to run")
    args = ap.parse_args(argv)
    entries = load_registry()
    if args.cmd == "list":
        return cmd_list(entries)
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        print("keys.py run: give a command after --", file=sys.stderr)
        return 2
    try:
        env = key_env(entries, args.only, dict(os.environ))
    except KeyError_ as exc:
        print(f"keys.py run: {exc}; command not started", file=sys.stderr)
        return 2
    return subprocess.run(command, env=env).returncode


if __name__ == "__main__":
    sys.exit(main())
