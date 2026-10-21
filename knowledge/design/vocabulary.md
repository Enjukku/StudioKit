---
type: reference
scope: game
status: active
updated: 2026-10-21
source: "J016 (context design: vault growth)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21; revised by feature-builder · claude-opus-5-5 · high · 2026-10-21, J016 G3 (audit D B6)

# Vocabulary: one name per thing

Filed at every job close. Every craft and every system uses these exact names: game states, events (the hooks sound, VFX and UI attach to), cue ids, asset ids, beat ids that outlive one job. A new name is added here before it is used in a second job. The context packet's `--role` block and the `SubagentStart` hook name this file for every role; `/integrate` copies names a craft must use into its overlay.

| Name | Kind (state / event / cue / asset / other) | Meaning | Owner | Used by | Source |
| --- | --- | --- | --- | --- | --- |
