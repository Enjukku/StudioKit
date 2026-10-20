# Role roster

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20

Roles move in from the first game in phase 3; canonical format: see tools/sync_harness.py header. Models per tier come from `kit.json` (lead and craft → Opus, research → Sonnet, mechanical → Haiku); each role file sets its own effort.

| Role | Tier → model | Effort (default; brief may raise it) | Status |
| --- | --- | --- | --- |
| orchestrator (lead, via orchestration skill) | lead → Opus | owner sets with `/effort`: medium; high for design or wiring | skill exists |
| game-designer | craft → Opus | high | planned |
| economy-designer | craft → Opus | high | new |
| art-director | craft → Opus | high | planned |
| cutscene-director | craft → Opus | high | new |
| animator | craft → Opus | high | planned |
| vfx-designer | craft → Opus | high for new or important effects; medium for small effects and fixes (trial, compare after 3 effects) | in kit |
| character-rigger | craft → Opus | high | new |
| modeler | craft → Opus | high; medium for simple models | new |
| ui-ux-designer | craft → Opus | medium | new |
| sound-designer | craft → Opus | medium | in kit |
| content-builder (levels and world assets) | craft → Opus | medium | planned |
| live-ops-designer | craft → Opus | medium | later |
| architect | lead → Opus | high | planned |
| reviewer | craft → Opus | medium; high for money, saves, remotes | planned |
| feature-builder | craft → Opus | medium; high for money, saves, remotes | planned |
| quick-builder | craft → Opus | medium (code is Opus medium at least) | planned |
| qa-lead | craft → Opus | medium | new |
| performance-engineer | craft → Opus | medium; high for big investigations | new |
| researcher | research → Sonnet | medium | planned |
| analyst | research → Sonnet | medium | planned |
| studio-operator | research → Sonnet | medium | planned |
| marketing-store | research → Sonnet | medium | later |
| doc-keeper | mechanical → Haiku | medium | planned |
| explore | mechanical → Haiku | low | planned |

xhigh and max: nobody by default; only after a measured gain. Owner decisions 2026-10-20 ("Opus for animating ... on high. For UI ... Opus on medium. For sound, Opus on medium"; modeler "for simple things, medium is fine ... models that we want to look really good ... high").

**How roles are added (owner 2026-10-20):** the kit ships only the orchestrator (the `orchestration` skill) and the system. Every other role is built with `/build-agent` from material the owner supplies, using `templates/role.md` and `templates/skill/SKILL.md`. No role is trained without owner material.
