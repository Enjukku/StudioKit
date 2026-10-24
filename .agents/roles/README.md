# Role roster

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20; revised by role-fixer W4 · claude-opus-5-5 · high · 2026-10-21, J016 G3 (roster wording, tools lines)

Canonical format: see tools/sync_harness.py header. Models per tier come from `kit.json` (lead and craft → Opus, research → Sonnet, mechanical → Haiku); each role file sets its own effort.

| Role | Tier → model | Effort (default; brief may raise it) | Status |
| --- | --- | --- | --- |
| orchestrator (lead, via orchestration skill) | lead → Opus | owner sets with `/effort`: medium; high for design or wiring | skill exists |
| game-designer | craft → Opus | high, always (owner J003-D3) | in kit (J003, closed 2026-10-21) |
| progression-designer (feeling timeline → curves, data tables, simulation, live tuning; replaces economy-designer, J011-D3) | craft → Opus | high (owner J011-D1); its tools and scripts Opus medium or higher | in kit (J011, G3 approved 2026-10-21) |
| art-director | craft → Opus | medium (owner 2026-10-23, was high J009-D1) | in kit (J009 closed 2026-10-21) |
| film-director (every cinematic moment: beat sheet, shot list + `tools/film/shotlist.py` with every shot's camera, length and markers (no boards or animatic, J024), craft briefs, Roblox playback checks, capture review; replaces cutscene-director, J015-D2) | craft → Opus | medium (owner 2026-10-23, was high J015-D1) | in kit (J015, owner 2026-10-21: done; tested in real game work) |
| animator (everything that moves: characters, creatures, held items, props and mechanisms, vehicles, buildings, ambient loops; rig-pipeline S1, K2, S6, S7; timing list; motion specs for builders) | craft → Opus | medium or high: high for character animations, animations that must be perfect and animations players see all the time; medium for the rest (owner 2026-10-23, was high 2026-10-20) | in kit (J006, 2026-10-21; skills animation-design, animation-craft) |
| vfx-designer | craft → Opus | high for new or important effects; medium for small effects and fixes (trial, compare after 3 effects) | in kit |
| character-rigger | craft → Opus | medium (owner 2026-10-23, was high) | in kit (J005, closed 2026-10-21; Studio import untested) |
| modeler | craft → Opus | high for hero models and new kinds of models; medium for simple models (J007-D1) | building (J007; G2 pending) |
| ui-ux-designer | craft → Opus | medium (high for a new look or a shop, brief-level) | in kit (J002, owner-approved 2026-10-21) |
| sound-designer | craft → Opus | medium | in kit |
| environment-designer (stages, levels, worlds: space, terrain, dressing, light, atmosphere, ambience map; replaces content-builder, J008-D3) | craft → Opus | high for new stages and big environments; medium for small changes and fixes (owner 2026-10-21, J008-D1) | building (J008) |
| live-ops-designer (updates, events, seasons, limited-time content, fixes after launch; feedback sort and count; ranked update plan; update briefs; post-update review) | craft → Opus | medium; high for a season plan or a big update (owner J014-D1) | in kit (J014, closed 2026-10-21; skills live-ops-design, live-ops-craft) |
| architect | lead → Opus | high (owner J010) | in kit (J010, owner 2026-10-21) |
| reviewer | craft → Opus | medium; high for money, saves, remotes | in kit (J010, owner 2026-10-21) |
| feature-builder | craft → Opus | medium; high for money, saves, remotes (owner J010) | in kit (J010, owner 2026-10-21) |
| quick-builder | craft → Opus | medium (code is Opus medium at least) | in kit (J010, owner 2026-10-21) |
| qa-lead | craft → Opus | medium | in kit (J010, owner 2026-10-21) |
| performance-engineer | craft → Opus | high (owner J010) | building (J010) |
| researcher | research → Sonnet | medium | in kit |
| analyst (own-game player data: diagnosis, A/B tests, event planning, weekly page; tool `tools/analytics/`) | research → Sonnet | medium; Opus high for a deep investigation (owner J013-D1) | in kit (J013 done 2026-10-21; skills analysis-design, analysis-craft; real-data run with the first game) |
| studio-operator | research → Sonnet | medium | in kit |
| trend-scout (market and loop trends with data) | research → Sonnet | medium (J004-D2: high inside J004 only) | in kit, legal-only mode (J004-D12) |
| marketing (title, icon, thumbnails, game page, video, updates, social, creators, Roblox ads, community; replaces marketing-store, J012-D2) | craft → Opus | medium; high for a new game's title, icon and launch plan (owner J012-D1) | in kit, not yet tested (J012 closed, J012-D9; skills marketing-design, marketing-craft) |
| doc-keeper | mechanical → Haiku | medium | in kit |
| explore | mechanical → Haiku | medium (owner 2026-10-23, was low) | in kit |

**Place in the job flow** (J016, owner approval J016-D4): each role file's "Your place in the job flow" section says where the role is job lead, direction lead, contract owner, integrator or reviewer; the seven recipes are in the `orchestration` skill (`references/job-types.md`) and run as saved workflows (`.agents/workflows/jobs/`). A role's `tools:` line is its permission list and the owner's decision: a role whose list has no SendMessage does its sideways work through exchange notes, and a role without Claude in Chrome writes image prompts and returns `images: pending`.

xhigh and max: nobody by default; only after a measured gain. Owner decisions 2026-10-20 ("Opus for animating ... on high. For UI ... Opus on medium. For sound, Opus on medium"; modeler "for simple things, medium is fine ... models that we want to look really good ... high").

**Usage revision (owner 2026-10-23):** to lower usage, film-director, art-director, character-rigger and animator go from high to medium, and explore goes from Haiku low to Haiku medium. Owner's words: "I think the film director should be medium. I think the art director should also be medium. I think the architect I'm not really sure. And the game designer stays on high. I think progression designer stays on high. I think the character rigger and animation should be on medium. And then I think the explorer should be on Haiku medium rather than low." This replaces the high settings from J015-D1, J009-D1 and the 2026-10-20 animator and rigger decisions. The architect stays high until the owner decides. A brief may still raise effort for one task. Revisit when: owner-found defects or repair rounds rise in a job that uses these roles. **Animator, same day:** medium or high. Owner's words: "I would change the animator to medium-high, though. Medium or high, rather. For more complex animations, we could set it to high. And this could be things like character animations, animations that need to be perfect that the player constantly sees." The role file default stays medium; `job-character` runs the animator at high (character animation players see all the time); other job workflows run it at medium, and a brief raises it to high for an animation of that kind.

**How roles are added (owner 2026-10-20):** new roles are built with `/build-agent` from material the owner supplies, using `templates/role.md` and `templates/skill/SKILL.md`. No role is trained without owner material.
