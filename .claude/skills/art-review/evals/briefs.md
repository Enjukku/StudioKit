# Eval briefs: art-director (art-direction + art-review)

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Built in J009. Run each brief with the `art-director` role in a fresh context; a separate grader (Sonnet, high) scores the must-pass checks from the files, not the hand-back. Hidden cases (not in the skills) live in `knowledge/jobs/J009-art-director/evals-hidden.md` and are given only to the grader.

## E1 — Direction from a concept (exploration)
Brief: the game designer sends a concept ("you play a small courier spirit carrying lanterns through a flooded night city; the light you carry is your health and the city's hope"), camera third person, phones first. Ask: 2-3 visual directions and a first art-bible draft. Image generation allowed (max 9 images).
| ID | Must pass |
| --- | --- |
| E1-1 | Moment and read-first items stated before any image (the lantern / player light reads first) |
| E1-2 | 2-3 directions that differ in proportion, material, density, light, camera reading or emotion — not palette swaps; each states what it changes |
| E1-3 | Same subjects and cameras across directions; any kinder camera or light is called out |
| E1-4 | Each packet has grayscale and phone-thumbnail evidence from `look_check.py` (JSON path cited) |
| E1-5 | World rule written as one causal premise and shown in at least 3 crafts (place, character, UI or effect) |
| E1-6 | Bible draft: locks as relationships with purpose, test and allowed variation; color roles with non-color backups; everything marked PROPOSAL; no lock content outside lock blocks and no direction text inside them |
| E1-7 | No franchise looks named as the target; any precedent cited carries its provenance |
| E1-8 | One recommendation and a digest item with a default; nothing called approved |

## E2 — Cross-craft review of a busy scene
Brief: 4 captures of one encounter (quiet, busiest, lowest quality, phone-size thumbnail) with a manifest missing the quality tier on one row, plus a VFX spec and an animation clip list without the clip files. Bible rev 2 with a "danger = warm core, hard edge" lock.
| ID | Must pass |
| --- | --- |
| E2-1 | Missing manifest field flagged; that capture's verdicts limited, not guessed |
| E2-2 | Motion items marked NOT REVIEWED with the exact clip requested |
| E2-3 | `look_check.py value` run with a mask on the threat; observation, interpretation and decision kept separate |
| E2-4 | No pass from a number without a tolerance source; diagnostics labelled |
| E2-5 | Findings ranked by consequence and dependency; each has an owner role and acceptance evidence; what works is listed |
| E2-6 | Briefs to VFX and environment designer in `rules/messages.md` §2 form; no recipe (no emitter counts, no light values) in `fixed` without a source |
| E2-7 | Cohesion table filled (color, shape, motion, sound, material meaning) |

## E3 — Is this still our game? (anchor drift)
Brief: three new character images from the modeler's references, the bible's CHARACTER LOCK, two approved anchors, and an owner decision two weeks newer than the lock that changed eye style.
| ID | Must pass |
| --- | --- |
| E3-1 | Drift check finds lock vs newest decision mismatch and proposes one edit to lock, anchor note and decision reference together |
| E3-2 | Per-image review against generated-image checks (views, counts, light, substitution, proportion drift) |
| E3-3 | `look_check.py silhouette --compare` against the anchor with alignment recorded; IoU reported as change, not quality |
| E3-4 | Anchors not approved or replaced by the agent; proposal + owner digest item |
| E3-5 | Brief to the modeler names identity features to keep and leaves the build method open |

## E4 — Thumbnail and icon truthfulness
Brief: marketing's draft icon (1024x1024) and thumbnail (1920x1080) plus three gameplay captures. The thumbnail shows a feature that is not in the game.
| ID | Must pass |
| --- | --- |
| E4-1 | Icon checked at 150x150 and thumbnail at its real crop with `look_check.py thumb`; resampling recorded |
| E4-2 | The missing feature flagged as a truthfulness failure against the in-game captures |
| E4-3 | Recognition anchors named (what must survive a refresh) |
| E4-4 | No click-through or conversion claim; the fix is a brief to marketing with the craft left open |

## E5 — UI contrast with the right standard
Brief: a HUD mock with three text roles over a moving world background and a translucent panel.
| ID | Must pass |
| --- | --- |
| E5-1 | One named standard per UI role (WCAG or Xbox), not mixed silently |
| E5-2 | `look_check.py contrast` ratios unrounded; measured against the lowest-contrast background sample, not the easiest |
| E5-3 | World art is not held to the UI text ratio |
| E5-4 | Fix routed to the UI designer as an outcome (backing, weight, color or layout is their choice) |
