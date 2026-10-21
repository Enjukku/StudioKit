# Icons and thumbnails: from brief to owner review

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `marketing-craft`. Sources: owner J012-D4 (ChatGPT through `reference-images`), J012-D5/D6 (`thumb_check.py`), `knowledge/reference/marketing/03-...md` §5 PR-05..PR-06, §6.2-6.3; fact-check FD-19..FD-28, FD-74; `art-review` R-14.

## 1. The route (every step has a check)
| # | Step | Check before the next step |
| --- | --- | --- |
| 1 | **Message first.** Fill `templates/marketing/thumbnail-brief.md` §A: build, destination, audience, the player fantasy, the single message, truth references, the promise-ledger claim id | the claim id points to a feature that is `playable` in the build you will ship (`game-concept/references/hook-promise.md` §2). No claim id = no image |
| 2 | **Art lock.** Read the game's art bible (`knowledge/design/art-bible.md`; for a kit test, `templates/skill/art-bible.md`). Families: `thumbnail` (16:9 key art of one real moment) and `game-icon` (square). Hero anchors from `content/art/anchors/character/` go in the manifest `inputs` | the bible has both families; if not, ask the art director (ticket), never write locks yourself |
| 3 | **Manifest.** One row per concept, `identity` = subject, action, consequence, camera, must-keep details, subject-specific "no" items. Style words stay in the locks. Distinct concepts, not palette swaps: core action / social moment / progression payoff, each only if the game has it (FD O, IM-19) | `python tools/art/art_refs.py print <manifest>`: read the full prompt and the attached anchors |
| 4 | **Generate.** `python tools/art/art_refs.py run <manifest> --limit N`. It stops at the first failure (often the image quota): report it; no retry loop | each file exists with its `.json` record |
| 5 | **Your own look first** (`reference-images` §5): hands, object count, identity vs anchors, scale, fake UI, invented rewards, stray text, anything the game does not have. Max 2 regenerations per image with a fixed identity, then report | every reject has a one-line reason |
| 6 | **Format.** Thumbnail: crop the wide image to 16:9 with the subject in the central area and nothing essential near the lower edge; never stretch (Roblox stretches non-16:9 uploads, FD-25); record the final px size and whether it reaches the ideal 1920×1080 (an upscale is recorded as one). Icon: square master ≥ 512×512 (FD-19) | sizes recorded in the checklist §A |
| 7 | **Title text** (only if the owner approved wording): added after generation in an editor (Figma through the ui-ux-designer, or an image editor), never drawn by the image model. Check spelling at full size and at small size | text layer kept separate; a text-free version kept |
| 8 | **Measure** (§2) | contact sheet + JSON saved next to the image |
| 9 | **Checklist** `templates/marketing/thumbnail-icon-checklist.md`, icon and thumbnail separately | every item PASS with evidence, or FAIL with the reason |
| 10 | **Art director review** (ticket, brief in `rules/messages.md` format): icon at its real small size and thumbnail at its real crop, each next to an in-game capture of the promise (`art-review` R-14) | the art director's note is in the checklist (I6) |
| 11 | **Owner package** (`marketing-craft` §3 step 8): the candidates, the rejected ones and why, the sheets, the claim ids, what each tests | the owner's decision id, recorded with the owner's words |

**Final assets (owner J012-D7).** The uploaded icon or thumbnail can come from three routes: (a) the ChatGPT image as generated, (b) a ChatGPT image touched up by hand (paint-over, fixes, title text), or (c) a staged render in Blender with the game's real models and set, made by the environment designer or modeler on a ticket (the ChatGPT image then serves as the composition target). Pick the route per image and say why: (c) is closest to the real game when the models exist; (a) and (b) when they do not yet. Every route goes through the same `thumb_check.py` run, checklist, art director review and the owner's approval of that one image. The asset record names the route and keeps the source files (prompt record, edit file, .blend and camera); it says **key art**, never "gameplay capture". For every other craft, reference images stay inputs (`reference-images`).

## 2. `thumb_check.py`: what to run and how to read it
```text
python tools/art/thumb_check.py icon <icon.png> --title "<title>" [--mask M | --box X0,Y0,X1,Y1 | --key auto]
python tools/art/thumb_check.py thumbnail <thumb.png> --size WxH --size-source "<capture id, device>" --bottom-band N --title "<title>" --box <hero and action>
```
| You need | How |
| --- | --- |
| **The small size** | Icon: default 150×150 (the size the Roblox icon docs name, FD-20). Thumbnail: no Roblox doc gives the phone tile size (searched 2026-10-21, T04). Measure it: a phone screenshot of Roblox Home with a game tile (owner, or studio-operator on a device), the tile's width × height in screenshot pixels, the device named. Store it as `knowledge/design/marketing/surfaces.md` (one row per device and surface, with the capture file). Re-measure when Roblox changes the Home layout |
| **The subject** | Without a subject the one-moment and contrast fields say "not measured". Full-scene thumbnails: give `--box` around the hero plus its action (one box per element you claim is "the moment"). Cut-out icons: `--key auto` on a flat background, or the alpha channel |
| **Bottom band** | `--bottom-band N` with N measured from the same capture (how much of the tile the metadata covers), never a guessed percent |
| **Tolerances** | none by default. A tolerance (`--min-ratio`, `--max-components`, `--max-bottom-share`) needs `--tolerance-source` = an owner or art-director decision id. Without one the verdict stays "measured": you read the numbers |

**Reading the numbers (diagnostics, not grades):**
| Field | Read as |
| --- | --- |
| `master.*.meets` | the docs' own format rules (square, ≥ 512, 16:9, size, 3 MB). A `false` is a format FAIL: fix it before anyone looks |
| `one_clear_moment.small.component_count` and `largest_share_of_subject` | how many separate things you boxed survive at the small size, and whether one dominates. Several equal parts at small size = the moment may split; check the sheet |
| `contrast.small.subject_ring_ratio` | the hero vs its surroundings, by luminance, at the small size. Low = the hero merges with the background in grey; look at the grey panel |
| `contrast.small.whole_p95_p5_ratio` | overall value range of the image; low = flat, everything mid-grey |
| `bottom_band.subject_share_in_band` | how much of the boxed subject sits where metadata can cover it |

Then look at the sheet yourself: can you say the action from the small preview with the title under it, in one sentence, without the full-size image? If not, the image fails I1 whatever the numbers say. The tool never says "good"; it shows where to look.

## 3. Variants and personalization
- 2-5 active thumbnails, each a different, honest concept (FD-26). Each concept states the one player expectation it changes (checklist I12).
- Uploads: under 3 MB and up to 1920×1080 per image (FD-27, read as per image).
- Before activating: tell the analyst the hypothesis, the metric label as the dashboard shows it (qPTR today, FD-43), the guardrails (first-play bounce, playtime of the arriving cohort) and the earliest read date. Uploading and activating is an **owner action** in Creator Hub.
- Do not restart within 7 days unless something is broken (FD-39). Change the set with substantial content updates (FD-40).
- Keep every image's asset id, version, the date it went live and the image it replaced (checklist I13).
