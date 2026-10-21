#!/usr/bin/env python3
"""Generate reference images with ChatGPT's image model, through Codex on the owner's ChatGPT subscription.

Kit tool (universal). Ported 2026-10-20 from DestructionSimulator tools/art/art_refs.py; the families and
locks now come from the game's art bible instead of being written in this file.

Every prompt = IDENTITY (the manifest row) + the family's lock + the world lock (unless the family skips it).
The locks and the family table live in knowledge/design/art-bible.md, so each lock has exactly one copy.
Up to three approved anchors from content/art/anchors/<folder>/ are attached to every call; `approve`
grows that library.

  python tools/art/art_refs.py print   <manifest.csv>             # assembled prompts, no generation
  python tools/art/art_refs.py run     <manifest.csv> [--limit N]  # generate missing rows
  python tools/art/art_refs.py approve <family> <id>               # copy a ref into the anchors
  --bible <path> (before the command) uses another art bible, e.g. the kit template for a quick test

Manifest columns: id, family, identity, inputs (optional; ';'-separated extra image paths attached before
the anchors), anchors (optional; ';'-separated file names in the family's anchor folder, or `none` for no anchors at all).
Every row runs in its own new Codex session (one image = one chat), so images never edit or copy each other.

Art bible format (machine-read):
  - a markdown table with the header `| family | lock | world lock | anchors |`; `world lock` is yes or no;
    `anchors` is the anchor folder name (empty = the family name);
  - fenced ```text blocks whose first words are `<NAME> LOCK:`; the world lock is `WORLD STYLE LOCK:`.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
BIBLE = ROOT / "knowledge" / "design" / "art-bible.md"
ANCHORS = ROOT / "content" / "art" / "anchors"
REFS = ROOT / "content" / "art" / "refs"
CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
MAX_ANCHORS = 3
GENERATED = "gen-"  # approve() prefixes our own generations; everything else is the owner's
WORLD = "WORLD STYLE LOCK"
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}
INSTRUCTION = (
    "Use your built-in image generation tool to create exactly one image from the prompt below."
    " {inputs}Do not edit any files, do not run shell commands and do not write code."
    " After generating, reply with only the word DONE.\n\nPROMPT:\n"
)


@dataclass(frozen=True)
class Family:
    name: str
    lock: str
    world: bool
    anchors: str


def locks(text: str) -> dict[str, str]:
    """Lock name (the words before the first colon) -> the whole block."""
    found = {}
    for block in re.findall(r"```text\n(.*?)\n```", text, re.S):
        found[block.split(":", 1)[0].strip()] = block
    return found


def families(text: str) -> dict[str, Family]:
    rows = {}
    in_table = False
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not line.strip().startswith("|"):
            in_table = False
            continue
        if [c.lower() for c in cells[:4]] == ["family", "lock", "world lock", "anchors"]:
            in_table = True
            continue
        if not in_table or set(cells[0]) <= {"-", ":", " "}:
            continue
        name, lock, world, anchor = (cells + ["", "", "", ""])[:4]
        name = name.strip("`")
        if world.lower() not in ("yes", "no"):
            raise ValueError(f"family {name}: world lock must be yes or no, got {world!r}")
        rows[name] = Family(name, lock.strip("`"), world.lower() == "yes", anchor.strip("`") or name)
    return rows


def load_bible(path: Path = BIBLE) -> tuple[dict[str, Family], dict[str, str]]:
    if not path.is_file():
        sys.exit(f"no art bible at {path}: copy the kit template and fill it in")
    text = path.read_text(encoding="utf-8")
    fams, lks = families(text), locks(text)
    for fam in fams.values():
        if fam.lock not in lks:
            sys.exit(f"family {fam.name}: lock block {fam.lock!r} not found in {path.name}")
        if fam.world and WORLD not in lks:
            sys.exit(f"family {fam.name} uses the world lock, but {WORLD!r} is not in {path.name}")
    return fams, lks


def anchors_for(fam: Family, ident: str, named: str = "", root: Path = ANCHORS) -> list[Path]:
    """Up to MAX_ANCHORS style references; anchors guide the whole look, the lock wins on conflicts (owner J009-D11). The owner's references (files without the gen- prefix) come
    first; a row may name them, else they are picked by the row id so different assets see different ones.
    The last slot is our newest approved generation, which keeps a batch consistent."""
    if named.strip().lower() == "none":
        return []  # exploration: no anchors, so styles from other directions cannot blend in
    folder = root / fam.anchors
    if not folder.is_dir():
        return []
    files = sorted(p for p in folder.iterdir() if p.suffix.lower() in IMAGE_EXT)
    owner = [p for p in files if not p.name.startswith(GENERATED)]
    ours = sorted((p for p in files if p.name.startswith(GENERATED)), key=lambda p: p.stat().st_mtime, reverse=True)
    if named:
        chosen = []
        for name in named.split(";"):
            path = folder / name.strip()
            if not path.is_file():
                sys.exit(f"{ident}: anchor {path} not found")
            chosen.append(path)
    else:
        start = sum(map(ord, ident)) % len(owner) if owner else 0
        chosen = (owner[start:] + owner[:start])[: MAX_ANCHORS - 1]
    picks = chosen[: MAX_ANCHORS - 1] + ours[:1] if ours else chosen[:MAX_ANCHORS]
    return picks[:MAX_ANCHORS]


def read_manifest(path: Path, fams: dict[str, Family]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        rows = [{k.strip(): (v or "").strip() for k, v in row.items()} for row in csv.DictReader(f)]
    for row in rows:
        if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", row.get("id", "")):
            sys.exit(f"bad id {row.get('id')!r}: lowercase letters, digits, - and _ only")
        if row.get("family") not in fams:
            sys.exit(f"{row['id']}: family must be one of {', '.join(sorted(fams))}")
        if not row.get("identity"):
            sys.exit(f"{row['id']}: identity is empty")
    return rows


def build(row: dict[str, str], fams: dict[str, Family], lks: dict[str, str], anchor_root: Path = ANCHORS) -> tuple[str, list[Path]]:
    fam = fams[row["family"]]
    world = lks[WORLD] if fam.world else ""
    inputs = [Path(p) for p in row.get("inputs", "").split(";") if p]
    for p in inputs:
        if not p.is_file():
            sys.exit(f"{row['id']}: input image not found: {p}")
    images = inputs + anchors_for(fam, row["id"], row.get("anchors", ""), anchor_root)
    note = ""
    if images:
        n_in, n_anchor = len(inputs), len(images) - len(inputs)
        parts = []
        if n_in:
            parts.append(f"the first {n_in} attached image(s) are inputs the prompt refers to")
        if n_anchor:
            parts.append(
                f"the last {n_anchor} are approved style anchors: match their whole look (shapes, proportions,"
                " colours, lighting, materials and rendering) but not their subjects or exact composition;"
                " where an anchor and the style lock below disagree, follow the lock"
            )
        note = "; ".join(parts).capitalize() + ". "
    prompt = INSTRUCTION.format(inputs=note) + f"{row['identity']}\n\n{lks[fam.lock]}"
    if world:
        prompt += f"\n\n{world}"
    return prompt, images


def codex_exe() -> Path:
    # The desktop app's binary sits beside codex-code-mode-host.exe, which the built-in image tool needs;
    # a standalone copy without it cannot generate images. The <hash> folder changes on update.
    base = Path(os.environ.get("LOCALAPPDATA", "")) / "OpenAI" / "Codex" / "bin"
    found = [p for p in base.glob("*/codex.exe") if (p.parent / "codex-code-mode-host.exe").is_file()]
    if not found:
        sys.exit(f"no Codex app binary with codex-code-mode-host.exe under {base}")
    return max(found, key=lambda p: p.stat().st_mtime)


def generated() -> set[Path]:
    return set((CODEX_HOME / "generated_images").glob("*/*.png"))


def run(rows: list[dict[str, str]], fams: dict[str, Family], lks: dict[str, str], limit: int) -> int:
    exe = codex_exe()
    scratch = ROOT / ".tools" / "art-scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    done = 0
    for row in rows:
        out = REFS / row["family"] / f"{row['id']}.png"
        if out.exists():
            continue
        if done >= limit:
            print(f"limit {limit} reached; rerun to continue")
            break
        prompt, images = build(row, fams, lks)
        before = generated()
        cmd = [str(exe), "exec", "-C", str(scratch), "--skip-git-repo-check", "-s", "read-only"]
        for img in images:
            cmd += ["-i", str(img)]
        cmd.append("-")
        started = time.time()
        print(f"[{row['id']}] generating with {len(images)} image(s) attached ...", flush=True)
        proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", errors="replace")
        # Codex writes each session's images to generated_images/<session id>/. Take only this session's
        # folder: diffing the shared folder once picked up an image from a concurrent batch.
        session = re.search(r"session id:\s*(\S+)", proc.stdout + proc.stderr)
        own = CODEX_HOME / "generated_images" / session.group(1) if session else None
        if own is not None and own.is_dir():
            new = sorted(own.glob("*.png"), key=lambda p: p.stat().st_mtime)
        else:
            new = sorted(generated() - before, key=lambda p: p.stat().st_mtime)
            if len(new) > 1:
                print(f"[{row['id']}] FAILED: session folder not found and {len(new)} new images are ambiguous; stopping")
                return 1
        if not new:
            tail = (proc.stdout + proc.stderr).strip().splitlines()[-6:]
            print(f"[{row['id']}] FAILED, stopping (quota or tool error?):\n  " + "\n  ".join(tail))
            return 1
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(new[-1], out)
        sidecar = {
            "id": row["id"],
            "family": row["family"],
            "prompt": prompt,
            "images": [str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p) for p in images],
            "codex_session": session.group(1) if session else None,
            "source": str(new[-1]),
            "seconds": round(time.time() - started),
        }
        out.with_suffix(".json").write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
        print(f"[{row['id']}] saved {out.relative_to(ROOT)} ({sidecar['seconds']} s)")
        done += 1
    return 0


def approve(fam: Family, ident: str) -> None:
    src = REFS / fam.name / f"{ident}.png"
    if not src.is_file():
        sys.exit(f"not found: {src}")
    dest_dir = ANCHORS / fam.anchors
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{GENERATED}{ident}.png"
    shutil.copy2(src, dest)
    os.utime(dest)  # newest anchors are attached first
    print(f"anchor added: {dest.relative_to(ROOT)}")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bible", type=Path, default=BIBLE, help="art bible to read (default: knowledge/design/art-bible.md)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_print = sub.add_parser("print")
    p_print.add_argument("manifest", type=Path)
    p_run = sub.add_parser("run")
    p_run.add_argument("manifest", type=Path)
    p_run.add_argument("--limit", type=int, default=10)
    p_app = sub.add_parser("approve")
    p_app.add_argument("family")
    p_app.add_argument("id")
    args = ap.parse_args()
    fams, lks = load_bible(args.bible)
    if args.cmd == "approve":
        if args.family not in fams:
            sys.exit(f"family must be one of {', '.join(sorted(fams))}")
        approve(fams[args.family], args.id)
        return 0
    rows = read_manifest(args.manifest, fams)
    if args.cmd == "print":
        for i, row in enumerate(rows, 1):
            prompt, images = build(row, fams, lks)
            print(f"===== {i}. {row['family']}/{row['id']}: attach {', '.join(map(str, images)) or 'nothing'}")
            print(prompt, end="\n\n")
        return 0
    return run(rows, fams, lks, args.limit)


if __name__ == "__main__":
    sys.exit(main())
