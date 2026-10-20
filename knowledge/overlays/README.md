# Overlays: game additions to kit skills

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20

An overlay adjusts one kit skill or role for this game without editing the kit file.

| Rule | Detail |
| --- | --- |
| Who writes here | `/integrate` (`.agents/workflows/integrate.md`). The owner approves each overlay. |
| File | `knowledge/overlays/<skill-or-role>.md`, one per skill or role. |
| Frontmatter | `type: overlay`, `scope: game`, `status: active`. See `rules/knowledge.md` §3. |
| Size | At most 60 lines. |
| Content | Only additions and overrides to the kit file, each with its reason and source (decision ID or lesson link). Never copy kit text. |
| Loading | An agent loads its skill, then the matching overlay. The overlay wins on conflict. |
| Kit update | After a kit update, `/integrate` re-checks each overlay and removes lines the kit now covers. |
