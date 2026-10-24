---
name: books-vs-tool-code
description: When writing sound books from the soundbench README, read the code paths too and check the working tree for uncommitted tool changes; the README can miss gaps (e.g. rank ignores layer takes)
metadata:
  type: feedback
---

When the books are rewritten from `tools/audio/soundbench/README.md`, also read the code behind each command (`rank.find_takes`, `generate.plan`, `render.family_*`) and run `git diff --stat tools/audio/soundbench/`.

**Why:** 2026-10-24 (J020 step 8 follow-up): the README did not say that `rank` reads only `<cue>.r<k>.t<n>` (layer takes `<cue>.<layer>.r<k>.t<n>` are never ranked), and an uncommitted review repair was changing `generate`'s round count to per cue, layers included, while the README at HEAD still said "own rounds".

**How to apply:** for every command fact in a book, cite README and confirm in code; word facts that a parallel change is moving so the reader trusts the tool's `--dry-run` output over the book, and name the gap as an open item in the hand-back.
