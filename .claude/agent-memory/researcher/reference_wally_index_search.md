---
name: wally-index-search
description: api.wally.run package-search works via WebFetch (wally.run pages do not); gives name/scope/version/description only, no downloads (J025 gaps)
metadata:
  type: reference
---

- `https://api.wally.run/v1/package-search?query=<word>` returns a readable list (name, scope, version, description) through WebFetch. No download counts, no dates; many results are forks and re-uploads.
- `api.github.com/repos/UpliftGames/wally-index/contents/<scope>` lists a scope's packages (root listing is truncated).
- Raw `src/*.lua` guesses for `t` and Cmdr returned 404; strictness checks need the real file path first.
- Why: J025 gaps research 2026-10-24. How to apply: use for "what packages exist"; for "widely used" fall back on upstream stars and push dates and say it is an inference.
