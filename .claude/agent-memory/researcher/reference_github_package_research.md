---
name: github-package-research-access
description: How to check Roblox package maintenance dates via WebFetch (GitHub API limits, Wally unreadable, raw files work) - J025
metadata:
  type: reference
---

- WebFetch of `api.github.com/repos/<o>/<r>` and `/releases/latest` returns pushed_at, stars, issues, licence; it starts returning 403 after about 20 calls in one session. Do the most important repos first.
- `wally.run/package/...` renders empty ("Loading..."): Wally publish dates are not obtainable; take versions from `wally.toml` via raw.githubusercontent.com.
- `raw.githubusercontent.com/.../init.luau` works and answers "does it start with --!strict" questions.
- Library docs sites (Blink, Zap) often 404 on guessed paths; Zap's docs live at `raw.githubusercontent.com/red-blox/zap/0.6.x/docs/config/*.md`. Blink's docs are Next.js (`docs/pages`), raw paths guessed 404.
- Blink's own benchmark file: `raw.githubusercontent.com/1Axen/blink/main/benchmark/Benchmarks.md` (vendor data, 2025-04-30).
- Why: J025 net/signals/cleanup research (2026-10-24). How to apply: plan fetches in priority order; mark undated repos "not verified".
