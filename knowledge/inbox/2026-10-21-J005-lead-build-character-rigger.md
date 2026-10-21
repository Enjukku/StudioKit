---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J005 (build character-rigger), owner chat 2026-10-21
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J005 lessons: rig workflow + character-rigger

## What worked
- The S0-S8 loop with one exact fix note per round worked end to end on a hard merged Tripo mesh (298 parts, 1,301 open edges): S1 → K2 → S2 → S3 → S4 note → fixes → S5, all in headless Blender 5.1.2.
- Option renders put real choices in front of the owner (A rigid vs B skinned shoulders) instead of text.
- Fact-checks changed rules: Blender's FBX defaults are wrong for Roblox → tools/rig/roblox_fbx.py sets every option.
- Weight-recipe changes (surface-measured zones, rigid bandage band) removed most folds before more geometry was asked for.

## What failed or cost too much
- Checks were far too heavy (64-79 poses × 6 views, rendered and inspected by both sender and receiver). Owner: "this takes way too much usage, way too much time" → J005-D8 light checks.
- Rigid ball roots cannot hide elongated cut rings at big moves (shoulders 1.8:1, hips 2:1); the S2 plan did not say so up front.
- First S3 caps used a flat swatch and a knife-edge rim; a stand-in wrote files outside the repo.

## Owner corrections (word for word)
- "Always be light check. And then, you know, if there is a issue, then it gets brought up with images or whatever." (J005-D8)
- "there's a use case for both, and you don't have to pick one or the other." (J005-D9: route per joint)
- "I think B is better." (J005-D7: skinned shoulders and hips on the teddy)
- "For now, the agent is just done ... we'll pick up mistakes and this kit should continue to keep updating and getting better." (J005-D10)

## Open gaps for /improve (from knowledge/jobs/J005-character-rigger/g2-gaps.md)
GP01 animator priority/fallback keys in the rig sheet · GP02 root record in the template · GP03 texture-only parts and loose decorations · GP04 CRLF/LF in sheet copies · GP05 existing model as look target at K0 · GP06 headless Blender route as default in blender-mcp.md · GP07 exposed caps must carry skin texture and rounded rims (modeler-handoff) · GP08 state the visible-joint consequence of elongated rings at S2 · GP09 scripts and renders only inside the asset folder.

## Not yet proven
- Roblox Studio import and playback of the rig (G2 Studio step not run; owner chose to test in real games).
