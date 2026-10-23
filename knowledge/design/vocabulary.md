---
type: reference
scope: game
status: active
updated: 2026-10-22
source: "J016 (context design: vault growth)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21; revised by feature-builder · claude-opus-5-5 · high · 2026-10-21, J016 G3 (audit D B6); revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6)

# Vocabulary: one name per thing

Filed at every job close. Every craft and every system uses these exact names: game states, events (the hooks sound, VFX and UI attach to), cue ids, asset ids, beat ids that outlive one job. A new name is added here before it is used in a second job. The context packet's `--role` block and the `SubagentStart` hook name this file for every role; `/integrate` copies names a craft must use into its overlay.

Kit names the books already use across crafts: the lead files each as a row at the first game job that uses it, with that game's meaning. Events: `contact_candidate` (forecast, from the pose) vs `contact_confirmed` (gameplay outcome), `cleanup` (`animation-design/references/game-timing.md` §4); denial reason codes as `<cause>` names such as `need_<resource>`, `level_locked`, `sold_out` (`architecture/references/worked-examples.md` D). The presentation contract, the timing list, the frame script and the cue card use the row's name.

| Name | Kind (state / event / cue / asset / other) | Meaning | Owner | Used by | Source |
| --- | --- | --- | --- | --- | --- |
