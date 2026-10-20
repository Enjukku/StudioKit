#!/usr/bin/env python3
"""Refresh the local Roblox Creator Docs mirror from Roblox/creator-docs.

The mirror at ``knowledge/external/roblox-creator-docs/`` is a text-only, pruned copy of the
official Creator Docs source (https://github.com/Roblox/creator-docs, published at
https://create.roblox.com/docs). This tool rebuilds it reproducibly from a pinned upstream
revision, so a refresh is one command instead of an afternoon.

Origin: ported into the Studio Kit from the DestructionSimulator game repo (2026-10-20).
Author of the port: orchestrator · claude-opus-5-5 · high. The mirror is universal engine
truth, so it ships with the kit and every game cloned from it.

Honest scope notes:

* **Text only.** Upstream ``assets/`` (images, video) is never fetched, so image links inside
  mirrored pages stay broken. The written content is complete.
* **Never deletes.** Pages that upstream removed are kept and given a ``[!warning]`` banner
  with a pointer to their successor, because notes across ``knowledge/`` link to them.
* **Generated navigation is ours, not upstream's.** Each page carries a callout naming its
  upstream source and a ``## Related Files`` list built by the stated rule in
  ``related_targets``. ``README.md``, ``_link-map.md`` and ``manifest.json`` are generated.

Usage::

    python tools/sync_roblox_docs.py --check                 # report drift, write nothing
    python tools/sync_roblox_docs.py --revision <full sha>   # refresh from a reviewed revision
    python tools/sync_roblox_docs.py                         # refresh from current upstream HEAD
    python tools/sync_roblox_docs.py --self-test             # verify chrome round-trip + links
"""

from __future__ import annotations

import argparse
import hashlib
import json
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MIRROR = REPO_ROOT / "knowledge" / "external" / "roblox-creator-docs"
UPSTREAM_URL = "https://github.com/Roblox/creator-docs"
CONTENT_ROOT = "content/en-us"
WIKI_PREFIX = "[[external/roblox-creator-docs/"
CALLOUT_FIRST_LINE = "> [!info] Local Roblox Creator Docs mirror"
BANNER_FIRST_LINE = "> [!warning] Not in the current upstream docs"
TAG_PREFIX = "tags: [roblox, documentation, external-reference, priority-reference"
RELATED_HEADING = "## Related Files"
READMES = {"README.md", "_link-map.md"}

# Prune policy, kept from the original mirror (see the mirror README): education curricula,
# creator-program and marketing pages are not development documentation.
PRUNE_PREFIXES = ("education/", "creator-programs/")
PRUNE_FILES = ("affiliates.md", "unity.md", "unreal.md")

# Two non-page upstream trees are copied verbatim, into underscore-prefixed folders so they never
# pollute the page list, the link graph or the README inventory:
#   content/en-us/includes/                MDX fragments that pages import; real prose lives there
#   content/en-us/reference/engine/**/*.yaml   the generated Engine API reference the published
#                                          site is built from (methods, properties, enums, signals)
INCLUDES_PREFIX = "includes/"
API_REFERENCE_PREFIX = "reference/engine/"
INCLUDES_DIR = "_includes"
API_REFERENCE_DIR = "_api-reference"
NON_PAGE_DIRS = (INCLUDES_DIR, API_REFERENCE_DIR)

RELATED_MAX = 16

# Pages upstream renamed, moved, merged, or retired. ``None`` means "no successor page".
# ``--check`` reports any dropped page that is missing from this map.
REPLACEMENTS: dict[str, str | None] = {
    # art/{accessories,characters,emotes,classic-clothing} -> avatar/
    "art/accessories/index": "avatar/rigid-accessories/index",
    "art/accessories/importing": "avatar/rigid-accessories/import",
    "art/accessories/export-settings": "avatar/rigid-accessories/export",
    "art/accessories/specifications": "avatar/rigid-accessories/specifications",
    "art/accessories/accessory-fitting-tool": "avatar/accessory-fitting-tool",
    "art/accessories/automatic-skinning-transfer": "avatar/automatic-skinning-transfer",
    "art/accessories/layered-clothing": "avatar/layered-accessories/index",
    "art/accessories/clothing-specifications": "avatar/layered-accessories/specifications",
    "art/accessories/clothing-export-settings": "avatar/layered-accessories/export",
    "art/accessories/caging-best-practices": "avatar/layered-accessories/caging-best-practices",
    "art/accessories/project-files": "avatar/layered-accessories/project-files",
    "art/accessories/import-clothing": "avatar/layered-accessories/import",
    "art/accessories/body-scale": "avatar/character-bodies/specifications",
    "art/characters/index": "avatar/character-bodies/index",
    "art/characters/import": "avatar/character-bodies/import",
    "art/characters/export-settings": "avatar/character-bodies/export",
    "art/characters/specifications": "avatar/character-bodies/specifications",
    "art/characters/project-files": "avatar/character-bodies/project-files",
    "art/characters/testing/index": "avatar/character-bodies/test",
    "art/characters/testing/blender": "avatar/character-bodies/test-blender",
    "art/characters/testing/studio": "avatar/character-bodies/test-studio",
    "art/characters/head-specifications": "avatar/dynamic-heads/specifications",
    "art/characters/head-validation": "avatar/dynamic-heads/validate",
    "art/characters/face-caging-best-practices": "avatar/dynamic-heads/caging-best-practices",
    "art/characters/facial-animation/index": "avatar/dynamic-heads/index",
    "art/characters/facial-animation/facs-poses-reference": "avatar/dynamic-heads/facs-poses-reference",
    "art/characters/facial-animation/use-heads-in-studio": "avatar/dynamic-heads/test",
    "art/emotes/index": "avatar/emotes/index",
    "art/emotes/import": "avatar/emotes/import",
    "art/emotes/export-settings": "avatar/emotes/export",
    "art/emotes/specifications": "avatar/emotes/specifications",
    "art/classic-clothing": "avatar/classic-clothing",
    "art/test-classic-clothing": "avatar/classic-clothing",
    "art/upload-classic-clothing": "avatar/classic-clothing",
    "art/validation-errors": None,
    "makeup/index": "avatar/makeup/index",
    "makeup/import": "avatar/makeup/import",
    "makeup/reassign-textures": "avatar/makeup/reassign-textures",
    "makeup/specifications": "avatar/makeup/specifications",
    # avatar-setup/ folded into its own index page
    "avatar-setup/auto-setup": "avatar-setup/index",
    "avatar-setup/tools": "avatar-setup/index",
    # the character controller library was rewritten around the new controller model
    "characters/character-controller-library/abilities": "characters/character-controller-library/custom-abilities",
    "characters/character-controller-library/controllers": "characters/character-controller-library/quick-start",
    # renamed pages (upstream renamed "experiences" to "games")
    "projects/configure-experiences": "projects/configure-games",
    "projects/experience-ownership-transfer": "projects/game-ownership-transfer",
    "projects/update-experiences": "projects/update-games",
    "studio/experience-settings": "projects/configure-games",
    "production/publishing/publish-experiences-and-places": "production/publishing/publish-games-and-places",
    "production/promotion/sponsor-items": "marketplace/sponsor-items",
    "production/publishing/dmca-guidelines": "marketplace/intellectual-property",
    "characters/r6-to-r15-adapter": "characters/index",
    "production/publishing/about-GDPR-and-CCPA": "production/publishing/RTBF-and-creators",
    # moved into a directory
    "workspace/camera": "workspace/camera/index",
    # retired with no successor page
    "production/game-design/starter-pack-design": None,
    "production/monetization/virtual-items": None,
    "resources/city-people-cars": None,
    "resources/roblox-connect": None,
}

WIKI_RE = re.compile(r"\[\[external/roblox-creator-docs/([^\]|#]+)(?:#([^\]|]*))?(?:\|([^\]]*))?\]\]")
MD_LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+?)\)")
FENCE_RE = re.compile(r"^\s*(?:```|~~~)")
TITLE_RE = re.compile(r"^title:\s*(.+)$", re.M)
TAGS_RE = re.compile(r"^tags: \[[^\]]*\]$", re.M)


def log(message: str) -> None:
    print(message, flush=True)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def run(args: list[str]) -> str:
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"command failed ({result.returncode}): {' '.join(args)}\n{result.stderr.strip()}")
    return result.stdout


# --------------------------------------------------------------------- upstream


def resolve_revision(revision: str | None) -> str:
    if revision:
        if not re.fullmatch(r"[0-9a-f]{40}", revision):
            raise SystemExit("--revision needs a full 40-character upstream commit SHA")
        return revision
    out = run(["git", "ls-remote", UPSTREAM_URL, "HEAD"]).strip()
    if not out:
        raise SystemExit("could not resolve upstream HEAD")
    return out.split()[0]


def fetch_upstream(revision: str, stage: Path | None) -> tuple[Path, Path, bool]:
    """Sparse blobless checkout of ``content/**`` at ``revision``. Returns (checkout, content, owned)."""
    if stage is not None:
        content = stage / CONTENT_ROOT
        if not content.is_dir():
            raise SystemExit(f"--stage-dir has no {CONTENT_ROOT}: {stage}")
        return stage, content, False
    stage = Path(tempfile.mkdtemp(prefix="roblox-creator-docs-"))
    run(["git", "clone", "--depth=1", "--filter=blob:none", "--sparse", UPSTREAM_URL, str(stage)])
    run(["git", "-C", str(stage), "sparse-checkout", "set", "--no-cone", "/content/**/*.md", "/content/**/*.yaml"])
    run(["git", "-C", str(stage), "fetch", "--depth=1", "origin", revision])
    run(["git", "-C", str(stage), "checkout", "--detach", revision])
    actual = run(["git", "-C", str(stage), "rev-parse", "HEAD"]).strip()
    if actual != revision:
        raise SystemExit(f"upstream revision mismatch: wanted {revision}, got {actual}")
    return stage, stage / CONTENT_ROOT, True


def upstream_pages(content: Path) -> dict[str, Path]:
    pages: dict[str, Path] = {}
    for path in sorted(content.rglob("*.md")):
        rel = path.relative_to(content).as_posix()
        if rel.startswith(INCLUDES_PREFIX) or rel.startswith(PRUNE_PREFIXES) or rel in PRUNE_FILES:
            continue
        pages[rel] = path
    return pages


def all_page_count(content: Path) -> int:
    return sum(1 for p in content.rglob("*.md") if not p.relative_to(content).as_posix().startswith(INCLUDES_PREFIX))


def copy_verbatim_tree(content: Path, prefix: str, suffixes: tuple[str, ...]) -> dict[str, Path]:
    """Upstream files under ``prefix`` with one of ``suffixes``, keyed by path relative to prefix."""
    selected: dict[str, Path] = {}
    root = content / prefix.rstrip("/")
    if not root.is_dir():
        return selected
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix in suffixes:
            selected[path.relative_to(root).as_posix()] = path
    return selected


def tree_digest(files: dict[str, Path]) -> str:
    """One hash over a whole tree (path + content), so the manifest stays readable."""
    digest = hashlib.sha256()
    for rel, path in sorted(files.items()):
        digest.update(rel.encode("utf-8"))
        digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def write_tree(mirror_dir: Path, files: dict[str, Path]) -> None:
    """Copy a verbatim tree, skipping files whose bytes already match (keeps re-runs a no-op)."""
    for rel, path in files.items():
        target = mirror_dir / rel
        payload = path.read_bytes()
        if target.is_file() and target.read_bytes() == payload:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)


def non_page_readme(name: str, upstream_prefix: str, count: int, what: str, how: str) -> str:
    return (
        "---\n"
        f'title: "Roblox Creator Docs mirror — {name}"\n'
        "tags: [roblox, documentation, external-reference, priority-reference]\n"
        "---\n"
        "\n"
        f"# `{name}` — copied verbatim, not pages\n"
        "\n"
        f"{what}\n"
        "\n"
        "| | |\n"
        "| --- | --- |\n"
        f"| Upstream | `{CONTENT_ROOT}/{upstream_prefix}` |\n"
        f"| Files | {count} |\n"
        "| Where | this folder |\n"
        f"| Search | {how} |\n"
        "\n"
        "These files are refreshed by `tools/sync_roblox_docs.py` and are excluded from the mirror's\n"
        "page list, page count and link graph, because they are not standalone documentation pages.\n"
        "Nothing here is transformed: no frontmatter is added, no links are rewritten.\n"
    )


def readme_section(includes_count: int, api_count: int, api_sections: dict[str, int]) -> list[str]:
    """Explanatory block for the mirror README; the trees themselves stay byte-pure upstream copies."""
    sections = ", ".join(f"{name} {count}" for name, count in sorted(api_sections.items()))
    return [
        "## Not pages: `_includes/` and `_api-reference/`",
        "",
        "Both folders are verbatim upstream copies, refreshed by the same tool and excluded from the page",
        "list, the page count and the link graph. They contain no generated content of ours, so a grep",
        "inside them only ever matches upstream text.",
        "",
        "| Folder | Upstream | Files | What it is / how to search |",
        "| --- | --- | --- | --- |",
        f"| `_includes/` | `content/en-us/includes/` | {includes_count} | MDX fragments that pages import. Some page prose exists **only** here — default input bindings, screen insets, system requirements, camera controls, legacy notes. `grep -r \"default bindings\" _includes/` |",
        f"| `_api-reference/` | `content/en-us/reference/engine/` | {api_count} | The generated Engine API reference behind https://create.roblox.com/docs/reference/engine — one YAML per class, data type and enum with methods, properties, signals, callbacks, parameters, defaults and security notes. Sections: {sections}. `grep -r \"name: MarketplaceService:OpenShop\" _api-reference/` |",
        "",
    ]


# ---------------------------------------------------------------- mirror chrome


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter including its closing ``---`` line, remainder)."""
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", text
    return text[: end + 4], text[end + 4:]


def parse_page(text: str) -> dict[str, str]:
    """Split a mirror page into chrome and body. ``compose_page`` inverts this exactly."""
    frontmatter, rest = split_frontmatter(text)
    marker = rest.find(CALLOUT_FIRST_LINE)
    if marker == -1:
        raise ValueError("page has no mirror callout")
    published = rest.find("Published page:", marker)
    callout_end = rest.find("\n", published)
    if callout_end == -1:
        raise ValueError("mirror callout is not terminated")
    body_start = callout_end + 1
    if rest[body_start:body_start + 1] == "\n":
        body_start += 1
    return {
        "frontmatter": frontmatter,
        "pre": rest[:marker],
        "callout": rest[marker:callout_end + 1],
        "mid": rest[callout_end + 1:body_start],
        "body": rest[body_start:],
    }


def compose_page(parts: dict[str, str]) -> str:
    return parts["frontmatter"] + parts["pre"] + parts["callout"] + parts["mid"] + parts["body"]


def strip_related(body: str) -> str:
    match = re.search(r"\n+" + re.escape(RELATED_HEADING) + r"\n", body)
    return body if match is None else body[: match.start() + 1]


def strip_banner(body: str) -> str:
    if not body.startswith(BANNER_FIRST_LINE):
        return body
    end = body.find("\n\n")
    return "" if end == -1 else body[end + 2:]


def display_title(text: str, rel: str) -> str:
    frontmatter, _ = split_frontmatter(text)
    match = TITLE_RE.search(frontmatter)
    if match:
        return match.group(1).strip().strip('"')
    for line in text.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return Path(rel).stem.replace("-", " ").replace("_", " ").capitalize()


def build_frontmatter(upstream_text: str, rel: str, existing_tags: str | None) -> str:
    """Upstream frontmatter verbatim, with the mirror's tag line added if it is absent.

    The tag line sits after ``description`` when that key exists, else after ``title`` —
    matching the layout of the original mirror.
    """
    frontmatter, _ = split_frontmatter(upstream_text)
    if not frontmatter:
        return ""
    tags = existing_tags or f"{TAG_PREFIX}, {rel.split('/')[0] if '/' in rel else 'root'}]"
    lines = [line for line in frontmatter.rstrip("\n").split("\n") if line != "---"]
    if any(line.startswith("tags: [") for line in lines):
        out = lines
    else:
        anchor = next((i for i, line in enumerate(lines) if line.startswith("description:")), None)
        if anchor is None:
            anchor = next((i for i, line in enumerate(lines) if line.startswith("title:")), None)
        out = list(lines)
        out.insert(anchor + 1 if anchor is not None else 0, tags)
    return "---\n" + "\n".join(out) + "\n---\n"


def published_url(rel: str) -> str:
    page = rel[:-3] if rel.endswith(".md") else rel
    if page.endswith("/index"):
        page = page[: -len("/index")]
    return f"https://create.roblox.com/docs/{page}"


def build_callout(rel: str) -> str:
    url = published_url(rel)
    return (
        f"{CALLOUT_FIRST_LINE}\n"
        f"> Mirrored from [{rel}]({UPSTREAM_URL}/blob/main/{CONTENT_ROOT}/{rel}). "
        f"Published page: [{url}]({url}).\n"
    )


# ---------------------------------------------------------------- transformation


def rewrite_links(body: str, rel: str, mirror_set: set[str], successions: dict[str, str]) -> tuple[str, list[str]]:
    """Relative ``.md`` links that resolve inside the mirror become wikilinks.

    Links to a retired page are pointed at that page's successor when one is known.
    """
    base = Path(rel).parent
    unresolved: list[str] = []
    out_lines: list[str] = []
    in_fence = False
    for line in body.split("\n"):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue

        def replace(match: re.Match[str]) -> str:
            text, target = match.group(1), match.group(2)
            path_part, _, anchor = target.partition("#")
            if not path_part.endswith(".md"):
                return match.group(0)
            if path_part.startswith("/"):
                resolved = path_part.lstrip("/")
                if resolved.startswith("docs/"):
                    resolved = resolved[len("docs/"):]
            else:
                resolved = posixpath.normpath(posixpath.join(base.as_posix(), path_part))
            while resolved.startswith("../"):
                resolved = resolved[3:]
            if resolved not in mirror_set:
                unresolved.append(f"{rel} -> {target}")
                return match.group(0)
            stem = successions.get(resolved[:-3], resolved[:-3])
            suffix = f"#{anchor}" if anchor else ""
            alias = f"|{text}" if text else ""
            return f"{WIKI_PREFIX}{stem}{suffix}{alias}]]"

        out_lines.append(MD_LINK_RE.sub(replace, line))
    return "\n".join(out_lines), unresolved


def related_targets(rel: str, body: str, mirror_set: set[str], titles: dict[str, str]) -> tuple[list[str], int]:
    """Everything the page links to, plus its section index pages, plus its directory peers.

    The original mirror generated this list with a link-similarity heuristic that cannot be
    reproduced from the source tree, so this tool states a simpler rule instead: outbound
    links and section indexes first, then title-sorted peers, capped at ``RELATED_MAX``.
    Retired pages are never suggested. Returns (targets, hidden_count).
    """
    stem = rel[:-3]
    directory = "/".join(stem.split("/")[:-1])
    outbound = {m.group(1) for m in WIKI_RE.finditer(body)}
    parts = stem.split("/")[:-1]
    ancestors = ["/".join(parts[:i]) for i in range(1, len(parts) + 1)]
    pool: list[str] = []
    for target in sorted(outbound | set(ancestors), key=lambda r: titles.get(r, r).casefold()):
        if target in mirror_set and target != stem and target not in pool:
            pool.append(target)
    for target in sorted(
        (r[:-3] for r in mirror_set
         if "/".join(r[:-3].split("/")[:-1]) == directory and r[:-3] != stem),
        key=lambda r: titles.get(r, r).casefold(),
    ):
        if target not in pool:
            pool.append(target)
    if not pool:
        # Section index pages with no peers: fall back to the pages they introduce.
        section = stem[: -len("/index")] if stem.endswith("/index") else stem
        for target in sorted(
            (r[:-3] for r in mirror_set if r[:-3].startswith(section + "/") and r[:-3] != stem),
            key=lambda r: titles.get(r, r).casefold(),
        ):
            if target not in pool:
                pool.append(target)
    chosen = sorted(pool[:RELATED_MAX], key=lambda r: titles.get(r, r).casefold())
    return chosen, max(0, len(pool) - RELATED_MAX)


def related_section(targets: list[str], hidden: int, titles: dict[str, str], body_present: bool) -> str:
    """``\\n\\n\\n## Related Files\\n\\n`` + entries, matching the original mirror's spacing."""
    if not targets:
        return ""
    prefix = "\n\n\n" if body_present else "\n"
    out = prefix + RELATED_HEADING + "\n\n"
    for target in targets:
        out += f"- {WIKI_PREFIX}{target}]] - {titles.get(target, target)}.\n"
    if hidden:
        out += f"- ...and {hidden} more local docs.\n"
    return out


def build_page(
    rel: str,
    upstream_text: str,
    existing: str,
    mirror_set: set[str],
    successions: dict[str, str],
    titles: dict[str, str],
) -> tuple[str, list[str]]:
    existing_tags = None
    chrome = None
    if existing:
        match = TAGS_RE.search(split_frontmatter(existing)[0])
        existing_tags = match.group(0) if match else None
        chrome = parse_page(existing)
    frontmatter = build_frontmatter(upstream_text, rel, existing_tags)
    keep_chrome = bool(chrome) and chrome["callout"].startswith(f"{CALLOUT_FIRST_LINE}\n> Mirrored from [{rel}]")
    callout = chrome["callout"] if keep_chrome else build_callout(rel)
    body = split_frontmatter(upstream_text)[1]
    body, unresolved = rewrite_links(body, rel, mirror_set, successions)
    body = strip_related(body).strip("\n")
    targets, hidden = related_targets(rel, body, mirror_set, titles)
    trailer = body + related_section(targets, hidden, titles, bool(body))
    if not trailer.endswith("\n"):
        trailer += "\n"
    parts = {
        "frontmatter": frontmatter,
        # Original mirror layout: two newlines after the frontmatter (or at the start of a page
        # with no frontmatter), one newline after the callout.
        "pre": "\n\n",
        "callout": callout,
        "mid": "\n",
        "body": trailer,
    }
    return compose_page(parts), unresolved


def retired_banner(revision: str, successor: str | None, date: str) -> str:
    if successor:
        tail = (
            f"The closest current page is [[external/roblox-creator-docs/{successor}]]. "
            "Kept locally so existing links keep working; read that page for current information."
        )
    else:
        tail = "It has no successor page. Kept locally for reference only; treat it as possibly outdated."
    return (
        f"{BANNER_FIRST_LINE}\n"
        f"> Not published in [{UPSTREAM_URL.split('//')[1]}]({UPSTREAM_URL}) as of {date} "
        f"(revision `{revision[:8]}`). {tail}\n\n"
    )


# ------------------------------------------------------------------- generators


def read_mirror() -> dict[str, str]:
    pages: dict[str, str] = {}
    for path in sorted(MIRROR.rglob("*.md")):
        rel = path.relative_to(MIRROR).as_posix()
        if rel in READMES or rel.startswith(NON_PAGE_DIRS):
            continue
        pages[rel] = path.read_text(encoding="utf-8", errors="replace")
    return pages


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="")


def title_map(upstream_texts: dict[str, str], mirror_pages: dict[str, str]) -> dict[str, str]:
    """Path-without-extension -> display title (upstream wins, mirror fills retired pages)."""
    titles: dict[str, str] = {}
    for rel, text in mirror_pages.items():
        titles[rel[:-3]] = display_title(text, rel)
    for rel, text in upstream_texts.items():
        titles[rel[:-3]] = display_title(text, rel)
    return titles


def generate_readme(mirror_pages: dict[str, str], titles: dict[str, str], retired: set[str],
                    project_pages: set[str], revision: str, pruned: int, upstream_total: int,
                    includes_count: int = 0, api_count: int = 0,
                    api_sections: dict[str, int] | None = None) -> str:
    sections: dict[str, list[str]] = {}
    for rel in mirror_pages:
        section = rel.split("/")[0] if "/" in rel else "root"
        sections.setdefault(section, []).append(rel)
    lines = [
        "---",
        'title: "Roblox Creator Docs Local Mirror"',
        "source: Roblox Creator Docs",
        f"upstream: {UPSTREAM_URL}",
        "published: https://create.roblox.com/docs",
        f"revision: {revision}",
        f"refreshed: {datetime.now(timezone.utc).date().isoformat()}",
        "tags: [roblox, documentation, external-reference, priority-reference, overview, index]",
        "---",
        "",
        "# Roblox Creator Docs Local Mirror",
        "",
        "Mirrors the focused markdown pages from Roblox Creator Docs. (Image/video assets were not copied into this project — image links are broken; text is complete.)",
        f"Pruned `{pruned}` of {upstream_total} upstream pages (education curricula, creator programs, marketing comparison pages).",
        "",
        f"Pinned upstream revision: `{revision}`. Refresh with `python tools/sync_roblox_docs.py`.",
        "Page inventory and per-file hashes: `manifest.json`.",
        "",
        "Two non-page upstream trees are copied verbatim into underscore-prefixed folders, so they are",
        "not part of the page list, page count or link graph:",
        "",
        "- `_includes/` — the MDX fragments that pages import (default input bindings, screen insets, system requirements, …). Page prose that lives in a fragment is only in this folder.",
        "- `_api-reference/` — the generated Engine API reference (`reference/engine/**/*.yaml`) behind https://create.roblox.com/docs/reference/engine. This is where exact methods, properties, signals, enum values and defaults live; search it with `grep -r \"name: MarketplaceService:OpenShop\" _api-reference/`.",
        "",
        "Use this area as local platform documentation. Game design decisions live in `knowledge/design/`.",
        "",
        "Pruning removes education challenges/curricula, creator-program/award pages,",
        "marketing comparison pages, non-coding beginner exercises, legacy",
        "superseded docs, and license/feedback material so the mirror stays focused on",
        "practical Roblox game development.",
        "",
        "Generated folder index pages are disabled; use the page list and link map instead of",
        "duplicate navigation-only notes.",
        "",
        "Pages that upstream removed are kept with a `[!warning]` banner naming their closest",
        "current page; `manifest.json` lists them under `dropped`. Hand-written project pages in",
        "this folder (`manifest.json` → `projectAuthored`) are never touched by the sync tool.",
        "",
        "Start with the generated relationship overview: [[external/roblox-creator-docs/_link-map|_link-map]].",
        "",
    ] + readme_section(includes_count, api_count, api_sections or {}) + [
        "## Sections",
        "",
    ]
    for section in sorted(sections):
        count = len(sections[section])
        index = f"{section}/index.md"
        if index in mirror_pages:
            lines.append(f"- [[external/roblox-creator-docs/{section}/index|{section}]] ({count} pages)")
        else:
            lines.append(f"- {section} ({count} pages)")
    lines += ["", "## All Pages", ""]
    for rel in sorted(mirror_pages):
        stem = rel[:-3]
        if rel in retired:
            marker = " *(no longer upstream)*"
        elif rel in project_pages:
            marker = " *(project-authored, not upstream)*"
        else:
            marker = ""
        lines.append(f"- [[external/roblox-creator-docs/{stem}|{titles.get(stem, stem)}]]{marker}")
    return "\n".join(lines) + "\n"


def generate_link_map(mirror_pages: dict[str, str], titles: dict[str, str], top: int = 50) -> str:
    incoming: dict[str, int] = {rel[:-3]: 0 for rel in mirror_pages}
    outgoing: dict[str, int] = {rel[:-3]: 0 for rel in mirror_pages}
    for rel, text in mirror_pages.items():
        body = strip_related(parse_page(text)["body"]) if CALLOUT_FIRST_LINE in text else text
        for match in WIKI_RE.finditer(body):
            outgoing[rel[:-3]] += 1
            if match.group(1) in incoming:
                incoming[match.group(1)] += 1
    lines = [
        "---",
        'title: "Roblox Creator Docs Link Map"',
        "source: Roblox Creator Docs local mirror",
        "tags: [roblox, documentation, external-reference, priority-reference, overview, link-map]",
        "---",
        "",
        "# Roblox Creator Docs Link Map",
        "",
        "Generated relationship overview from local internal documentation links",
        "(page-body links only; the generated `## Related Files` tails are excluded).",
        "",
        "## Most Referenced Pages",
        "",
    ]
    for target, count in sorted(incoming.items(), key=lambda kv: (-kv[1], titles.get(kv[0], kv[0]).casefold()))[:top]:
        lines.append(f"- {WIKI_PREFIX}{target}|{titles.get(target, target)}]] - {count} incoming links")
    lines += ["", "## Most Connected Pages", ""]
    total = {t: incoming[t] + outgoing[t] for t in incoming}
    for target, count in sorted(total.items(), key=lambda kv: (-kv[1], titles.get(kv[0], kv[0]).casefold()))[:top]:
        lines.append(f"- {WIKI_PREFIX}{target}|{titles.get(target, target)}]] - {count} total links")
    lines += ["", "## Pages With No Resolved Local Links", ""]
    orphans = sorted(
        (t for t in incoming if incoming[t] == 0 and outgoing[t] == 0),
        key=lambda t: titles.get(t, t).casefold(),
    )
    for target in orphans:
        lines.append(f"- {WIKI_PREFIX}{target}|{titles.get(target, target)}]]")
    return "\n".join(lines) + "\n"


# ----------------------------------------------------------------------- checks


def check_wikilinks(mirror_pages: dict[str, str]) -> list[str]:
    stems = {rel[:-3] for rel in mirror_pages}
    broken: list[str] = []
    for rel, text in mirror_pages.items():
        for match in WIKI_RE.finditer(text):
            if match.group(1) not in stems:
                broken.append(f"{rel}: {WIKI_PREFIX}{match.group(1)}]]")
    return sorted(set(broken))


def check_markdown_links(mirror_pages: dict[str, str]) -> list[str]:
    """Relative ``.md`` links we could not convert (target pruned or gone). Reported, not fatal."""
    targets = {rel[:-3] for rel in mirror_pages} | set(mirror_pages)
    unresolved: list[str] = []
    for rel, text in mirror_pages.items():
        if CALLOUT_FIRST_LINE not in text:
            continue
        body = strip_related(parse_page(text)["body"])
        base = Path(rel).parent
        for match in MD_LINK_RE.finditer(body):
            target = match.group(2)
            path_part = target.partition("#")[0]
            if not path_part.endswith(".md"):
                continue
            if path_part.startswith("/"):
                resolved = path_part.lstrip("/")
            else:
                resolved = posixpath.normpath(posixpath.join(base.as_posix(), path_part))
            while resolved.startswith("../"):
                resolved = resolved[3:]
            if resolved[:-3] not in targets and resolved not in targets:
                unresolved.append(f"{rel} -> {target}")
    return sorted(set(unresolved))


def self_test(mirror_pages: dict[str, str], project_pages: set[str]) -> int:
    """Round-trip chrome parsing, then confirm every wikilink resolves."""
    failures = 0
    checked = 0
    for rel, text in mirror_pages.items():
        if rel in project_pages:
            continue
        try:
            parts = parse_page(text)
        except ValueError as error:
            log(f"  FAIL parse {rel}: {error}")
            failures += 1
            continue
        checked += 1
        if compose_page(parts) != text:
            log(f"  FAIL round-trip {rel}")
            failures += 1
    broken = check_wikilinks(mirror_pages)
    for entry in broken:
        log(f"  broken wikilink {entry}")
    log(f"self-test: {checked} mirrored pages ({len(project_pages)} project-authored skipped), "
        f"{len(broken)} broken wikilinks, {failures} chrome failures")
    return failures + len(broken)


# ------------------------------------------------------------------------- main


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--revision", help="full upstream commit SHA to mirror (default: upstream HEAD)")
    parser.add_argument("--stage-dir", type=Path, help="reuse an existing creator-docs checkout")
    parser.add_argument("--check", action="store_true", help="report drift and write nothing")
    parser.add_argument("--self-test", action="store_true", help="verify chrome + links of the current mirror")
    parser.add_argument("--limit", type=int, default=0, help="debug: write only the first N changed pages")
    parser.add_argument("--no-includes", action="store_true", help=f"skip the {INCLUDES_DIR}/ fragment tree")
    parser.add_argument("--no-api-reference", action="store_true",
                        help=f"skip the {API_REFERENCE_DIR}/ Engine API YAML tree")
    args = parser.parse_args(argv)

    if not MIRROR.is_dir():
        raise SystemExit(f"mirror not found: {MIRROR}")

    current = read_mirror()
    # Hand-written project pages live in this folder too. They carry no mirror callout and are
    # never rewritten, never "retired", and never given a banner.
    project_pages = {rel for rel, text in current.items() if CALLOUT_FIRST_LINE not in text}
    if args.self_test:
        return 1 if self_test(current, project_pages) else 0

    revision = resolve_revision(args.revision)
    log(f"upstream revision: {revision}")
    stage, content, owned = fetch_upstream(revision, args.stage_dir)
    try:
        pages = upstream_pages(content)
        total_upstream = all_page_count(content)
        log(f"upstream pages in scope: {len(pages)} (of {total_upstream} excluding includes/)")

        upstream_text = {rel: path.read_text(encoding="utf-8", errors="replace") for rel, path in pages.items()}
        titles = title_map(upstream_text, current)
        retired = sorted(rel for rel in current if rel not in pages and rel not in project_pages)
        successor_of = {rel[:-3]: REPLACEMENTS[rel[:-3]] for rel in retired if REPLACEMENTS.get(rel[:-3])}
        successions = {old: new for old, new in successor_of.items() if new}

        # Live pages only: a retired page must never be suggested as "related".
        mirror_set = set(pages) | project_pages | {rel for rel in retired if rel[:-3] not in successor_of}
        log(f"project-authored pages kept untouched: {len(project_pages)}")
        log(f"retired pages: {len(retired)} ({len(successions)} with a known successor, "
            f"{len(retired) - len(successor_of)} retired without replacement)")

        planned: dict[str, tuple[str, list[str]]] = {}
        unresolved: list[str] = []
        for rel in sorted(pages):
            text, bad = build_page(rel, upstream_text[rel], current.get(rel, ""), mirror_set, successions, titles)
            planned[rel] = (text, bad)
            unresolved += bad

        new = sorted(rel for rel in pages if rel not in current)
        changed = sorted(rel for rel in pages if rel in current and current[rel] != planned[rel][0])
        unchanged = sorted(rel for rel in pages if rel in current and current[rel] == planned[rel][0])
        log(f"new: {len(new)}  changed: {len(changed)}  unchanged: {len(unchanged)}")

        todo = new + changed
        if args.limit:
            todo = todo[: args.limit]

        retired_only = [rel for rel in retired if rel[:-3] in REPLACEMENTS]
        if args.check:
            n_includes = len(copy_verbatim_tree(content, INCLUDES_PREFIX, (".md",))) if not args.no_includes else 0
            n_api = len(copy_verbatim_tree(content, API_REFERENCE_PREFIX, (".yaml", ".yml"))) if not args.no_api_reference else 0
            log("check mode: nothing written")
            log(f"would write {len(todo)} live pages and re-stamp {len(retired_only)} retired pages")
            log(f"would copy {n_includes} include fragment(s) and {n_api} API reference file(s)")
            for rel in todo[:20]:
                log(f"  write {rel}")
            if len(todo) > 20:
                log(f"  ... and {len(todo) - 20} more")
            return 0

        date = datetime.now(timezone.utc).date().isoformat()
        for rel in todo:
            write(MIRROR / rel, planned[rel][0])
        for rel in retired:
            path = MIRROR / rel
            chrome = parse_page(path.read_text(encoding="utf-8", errors="replace"))
            body = retired_banner(revision, REPLACEMENTS.get(rel[:-3]), date) + strip_banner(chrome["body"]).lstrip("\n")
            chrome["body"] = body
            write(path, compose_page(chrome))

        # Non-page trees, copied byte-for-byte.
        includes_files: dict[str, Path] = {}
        api_files: dict[str, Path] = {}
        api_trees: dict[str, dict[str, Path]] = {}
        if not args.no_includes:
            includes_files = copy_verbatim_tree(content, INCLUDES_PREFIX, (".md",))
            write_tree(MIRROR / INCLUDES_DIR, includes_files)
            log(f"includes copied: {len(includes_files)} file(s)")
        if not args.no_api_reference:
            api_files = copy_verbatim_tree(content, API_REFERENCE_PREFIX, (".yaml", ".yml"))
            for rel, path in api_files.items():
                api_trees.setdefault(rel.split("/")[0], {})[rel] = path
            write_tree(MIRROR / API_REFERENCE_DIR, api_files)
            log("api reference copied: " + ", ".join(
                f"{section} {len(files)}" for section, files in sorted(api_trees.items())))

        final = read_mirror()
        write(MIRROR / "README.md",
              generate_readme(final, titles, set(retired), project_pages, revision,
                              total_upstream - len(pages), total_upstream,
                              len(includes_files), len(api_files),
                              {s: len(f) for s, f in api_trees.items()}))
        write(MIRROR / "_link-map.md", generate_link_map(final, titles))
        manifest = {
            "source": UPSTREAM_URL,
            "revision": revision,
            "retrievedUtc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "contentRoot": CONTENT_ROOT,
            "selection": "content Markdown pages plus the non-page includes/ and reference/engine YAML trees, "
                         "text only; no media; education/ and creator-programs/ pruned",
            "prunePrefixes": list(PRUNE_PREFIXES),
            "pruneFiles": list(PRUNE_FILES),
            "generator": "tools/sync_roblox_docs.py",
            "counts": {
                "upstreamPagesExcludingIncludes": total_upstream,
                "mirrored": len(final),
                "dropped": len(retired),
                "projectAuthored": len(project_pages),
                "pruned": total_upstream - len(pages),
                "includes": len(includes_files),
                "apiReference": len(api_files),
            },
            # Run-scoped: what THIS invocation changed. The first refresh that brought the mirror
            # to this revision is recorded in git history and in the system note.
            "lastRun": {
                "new": len(new),
                "changed": len(changed),
                "unchanged": len(unchanged),
                "writtenLive": len(todo),
                "restampedRetired": len(retired),
            },
            "nonPageTrees": {
                INCLUDES_DIR: {
                    "upstream": INCLUDES_PREFIX,
                    "files": len(includes_files),
                    "bytes": sum(p.stat().st_size for p in includes_files.values()),
                    "sha256": tree_digest(includes_files),
                },
                API_REFERENCE_DIR: {
                    "upstream": API_REFERENCE_PREFIX,
                    "files": len(api_files),
                    "bytes": sum(p.stat().st_size for p in api_files.values()),
                    "sha256": tree_digest(api_files),
                    "sections": {s: len(f) for s, f in sorted(api_trees.items())},
                },
            },
            "dropped": {rel[:-3]: REPLACEMENTS.get(rel[:-3], None) for rel in retired},
            "projectAuthored": sorted(rel[:-3] for rel in project_pages),
            "files": {
                rel: {
                    "sha256": sha256_text(text),
                    "upstreamSha256": sha256_text(upstream_text[rel]) if rel in upstream_text else None,
                    "dropped": rel in set(retired),
                }
                for rel, text in sorted(final.items())
            },
        }
        write(MIRROR / "manifest.json", json.dumps(manifest, indent=1) + "\n")

        final_pages = read_mirror()
        broken = check_wikilinks(final_pages)
        log("")
        log(f"pages written: {len(todo)} live, {len(retired)} re-stamped retired")
        log(f"links left as markdown (target pruned or gone): {len(set(unresolved))}")
        log(f"broken wikilinks after refresh: {len(broken)}")
        for entry in broken[:20]:
            log(f"  {entry}")
        missing_map = [rel for rel in retired if rel[:-3] not in REPLACEMENTS]
        if missing_map:
            log(f"retired pages with no REPLACEMENTS entry ({len(missing_map)}):")
            for rel in missing_map:
                log(f"  {rel}")
        return 1 if broken else 0
    finally:
        if owned:
            shutil.rmtree(stage, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
