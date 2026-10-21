# Role roster

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20

Roles move in from the first game in phase 3; canonical format: see tools/sync_harness.py header. Models per tier come from `kit.json` (lead and craft → Opus, research → Sonnet, mechanical → Haiku); each role file sets its own effort.

| Role | Tier → model | Effort (default; brief may raise it) | Status |
| --- | --- | --- | --- |
| orchestrator (lead, via orchestration skill) | lead → Opus | owner sets with `/effort`: medium; high for design or wiring | skill exists |
| game-designer | craft → Opus | high, always (owner J003-D3) | in kit (J003, closed 2026-10-21) |
| progression-designer (feeling timeline → curves, data tables, simulation, live tuning; replaces economy-designer, J011-D3) | craft → Opus | high (owner J011-D1); its tools and scripts Opus medium or higher | building (J011) |
| art-director | craft → Opus | high (owner J009-D1) | building (J009; skills art-direction, art-review; G2 pending) |
| film-director (every cinematic moment: beat sheet, shot list + `tools/film/shotlist.py`, ChatGPT storyboards, Blender animatic, craft briefs, Roblox playback checks, capture review; replaces cutscene-director, J015-D2) | craft → Opus | high (owner J015-D1) | building (J015; skills film-direction, film-craft; G2 pending) |
| animator | craft → Opus | high | planned (J006, after J005) |
| vfx-designer | craft → Opus | high for new or important effects; medium for small effects and fixes (trial, compare after 3 effects) | in kit |
| character-rigger | craft → Opus | high | building (J005) |
| modeler | craft → Opus | high for hero models and new kinds of models; medium for simple models (J007-D1) | building (J007; G2 pending) |
| ui-ux-designer | craft → Opus | medium (high for a new look or a shop, brief-level) | in kit (J002, G3 pending) |
| sound-designer | craft → Opus | medium | in kit |
| environment-designer (stages, levels, worlds: space, terrain, dressing, light, atmosphere, ambience map; replaces content-builder, J008-D3) | craft → Opus | high for new stages and big environments; medium for small changes and fixes (owner 2026-10-21, J008-D1) | building (J008) |
| live-ops-designer (updates, events, seasons, limited-time content, fixes after launch; feedback sort and count; ranked update plan; update briefs; post-update review) | craft → Opus | medium; high for a season plan or a big update (owner J014-D1) | building (J014; skills live-ops-design, live-ops-craft; G2 pending) |
| architect | lead → Opus | high (owner J010) | in kit (J010, owner 2026-10-21) |
| reviewer | craft → Opus | medium; high for money, saves, remotes | in kit (J010, owner 2026-10-21) |
| feature-builder | craft → Opus | medium; high for money, saves, remotes (owner J010) | in kit (J010, owner 2026-10-21) |
| quick-builder | craft → Opus | medium (code is Opus medium at least) | in kit (J010, owner 2026-10-21) |
| qa-lead | craft → Opus | medium | in kit (J010, owner 2026-10-21) |
| performance-engineer | craft → Opus | high (owner J010) | building (J010) |
| researcher | research → Sonnet | medium | in kit |
| analyst (own-game player data: diagnosis, A/B tests, event planning, weekly page; tool `tools/analytics/`) | research → Sonnet | medium; Opus high for a deep investigation (owner J013-D1) | building (J013; skills analysis-design, analysis-craft; G2 pending) |
| studio-operator | research → Sonnet | medium | in kit |
| trend-scout (market and loop trends with data) | research → Sonnet | medium (J004-D2: high inside J004 only) | in kit, legal-only mode (J004-D12) |
| marketing (title, icon, thumbnails, game page, video, updates, social, creators, Roblox ads, community; replaces marketing-store, J012-D2) | craft → Opus | medium; high for a new game's title, icon and launch plan (owner J012-D1) | in kit, not yet tested (J012 closed, J012-D9; skills marketing-design, marketing-craft) |
| doc-keeper | mechanical → Haiku | medium | in kit |
| explore | mechanical → Haiku | low | in kit |

xhigh and max: nobody by default; only after a measured gain. Owner decisions 2026-10-20 ("Opus for animating ... on high. For UI ... Opus on medium. For sound, Opus on medium"; modeler "for simple things, medium is fine ... models that we want to look really good ... high").

**How roles are added (owner 2026-10-20):** the kit ships only the orchestrator (the `orchestration` skill) and the system. Every other role is built with `/build-agent` from material the owner supplies, using `templates/role.md` and `templates/skill/SKILL.md`. No role is trained without owner material.
