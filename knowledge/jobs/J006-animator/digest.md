---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J006 G1
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J006 G1)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G1 for J006 (`job-card.md`) | approve / change | approve | waits for your answer |
| 2 | Which Riot material counts | (a) ep4 (already read line by line in J016) + the Riot core series animation part (Garen pose, Teemo ball bounce, state machines); (b) ep4 only | (a) | (a) |
| 3 | Skill names | `animation-design` (what and why; read by rigger, VFX, sound, film too) + `animation-craft` (how) | as stated (`rig-pipeline` §5 already names `animation-design`) | as stated |
| 4 | Small clip-check script `tools/anim/clip_check.py` for the light checks: loop seam (pose and speed at the join), foot slide while a foot is planted, clip length against the gameplay window, markers against the timing list. Pure parts tested offline | build / no script | build, small | build |
| 5 | G2 test | (a) the J005 teddy rig: rig acceptance, idle loop, walk loop, one action with a timing list, Roblox import (you click Import in Place2) and playback; (b) skip G2 and test in real games, as with the rigger | (a), because the rigger's Studio import was never proven and this test proves both | (a) |
| 6 | Effort for the Sonnet helpers | high (J005-D4) | high | high |
