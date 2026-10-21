---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J009 brief (hidden test set); notes 01:SC-HS, 02:RD5-RD6, 05:OR24
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J009 hidden eval cases (grader only; not in the skills — lead-notes N12)

The agent gets only the **symptom brief**. The grader scores the hand-back and files against **expected** and the general rubric. Expected answers are paraphrased from the cited notes; the agent need not match the real studio's fix, only reach a diagnosis and direction of the same quality.

## H1 — Attack indicator that helps the wrong side (from a Riot skin case, 2018)
Symptom brief: "A new cosmetic version of a champion's attack has a busier indicator. Testers say it is easier to dodge than the base version. On phones the thin edge lines look jagged. A color-blind tester could not see the red projectile on green ground. Review it and direct the fix." Inputs: none beyond the text (the agent must ask for or name the captures it needs).
| Expected | Points |
| --- | --- |
| Names the parity rule: a cosmetic must not change readability vs the base (C-06 clarity allowance) | 2 |
| Asks for same-camera base vs variant captures at phone size and the dodge clip; marks motion NOT REVIEWED until given | 2 |
| Thin lines: check real raster width at the device size; no invented universal minimum | 2 |
| Color: red-on-green fails for color-blind players; asks for a non-color channel (value, size, shape at the dangerous end) and a test with affected players; grayscale/simulation alone is not proof | 2 |
| Direction to VFX as outcome + acceptance evidence, no recipe | 2 |

## H2 — Beautiful effect that signals the wrong choice (from a card-game effects case, 2018)
Symptom brief: "A persistent board effect covers most of the screen; players say they miss a combo. A highlight on one card is so flashy that players assume playing it is always correct. Effects look great in isolation." Inputs: text only.
| Expected | Points |
| --- | --- |
| Diagnosis: attention does not match importance; spectacle implies urgency or "best move" the mechanic does not have | 3 |
| Persistent / recurring effects get less screen demand than short decisive events; the effect must not hide the next decision | 3 |
| Requests the combined-frame clip, not the isolated effect sheet | 2 |
| Brief to VFX (and UI where the highlight lives) with protected qualities and acceptance evidence | 2 |

## H3 — Collectibles that read as rubble (from the first game, owner rulings)
Symptom brief: "After an explosion, the pickups the player should collect look like the debris around them; players walk past them. Earlier, flat 2D pickup sprites in the 3D world were rejected by the owner after a play-test." Inputs: text only.
| Expected | Points |
| --- | --- |
| Diagnosis: collectible and debris share shape, color and value language; the collect state has no distinct role | 3 |
| Proposes a color role that never matches the surroundings plus a non-color channel (motion such as hover/spin, glint, shape); records it as a bible color role + lock proposal | 3 |
| Respects the owner's earlier rejection (no 2D sprites) as a locked decision | 2 |
| Asks for an in-game clip at phone size after the change; routes the build to VFX / modeler as outcome | 2 |

## General rubric (every case, pass/fail)
- Observation, interpretation and decision kept separate.
- No invented numeric threshold or studio rule.
- Owner decides; nothing called approved.
- Hand-back in `rules/messages.md` §3 form with coverage.
