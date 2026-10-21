---
name: reference-images
description: Make reference images with ChatGPT's image model so every agent sees the same game before it builds - concept and key art, character and creature sheets, model references for Blender and Tripo, animation key-pose sheets, VFX key frames, UI moods and icons. One art bible holds the style locks, approved anchors keep batches consistent, and a tool assembles and runs the prompts. Use whenever visual work starts (a new game, character, model, animation, effect or screen), when "it doesn't look like our game", or when agents need a shared picture of the target. Images are inputs and targets, never the final asset.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. Owner request 2026-10-20: "reference images are really strong for giving context of the stylization and the game as a whole"; every model starts from a ChatGPT reference image. Ported from the DestructionSimulator art pipeline (`tools/art/art_refs.py`, art bible locks, anchors; 2026-09 to 2026-10), game details removed.

# Reference images: one picture of the target for every agent

## 1. When this skill starts
Before any visual work is built: a new game or stage, a character, creature, model, prop, animation, effect or screen. Also when work drifts from the style. The game needs `knowledge/design/art-bible.md` (copy `templates/skill/art-bible.md`); without it, the art director (or the lead) writes it first and the owner approves its locks.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The style locks and families for this game | `knowledge/design/art-bible.md` |
| How to write the `identity` for each family, edits, several images, text, refining, usage limits | `references/prompt-patterns.md` |
| UI images inside Figma, icon prompts, image credits | `ui-figma` skill, `references/image-generation.md` |
| How a model is built from the reference | `modeling-design`, `modeling-craft` (modeler) |
| Brief format for asking another agent for images | `rules/messages.md` |

## 3. Who uses it, for what
| Role | Family | What the image is for |
| --- | --- | --- |
| game-designer | `concept` | key art of the fantasy, key moments, places; the first picture every agent shares |
| art-director | all | writes and keeps the locks; proposes anchors (the owner approves each, J009-D3); checks that images from all roles look like one game (`art-direction`, `art-review` skills) |
| modeler | `model`, `prop`, `environment`, `character`, `creature` | the reference every model starts from (Blender by hand, or Tripo image-to-3D) |
| animator | `pose` | key poses and silhouettes before keying; how a body or tool should read in motion |
| vfx-designer | `vfx` | key frames of an effect (build-up, peak, dissipate) next to the frame script |
| ui-ux-designer | `ui`, `icon` | screen moods, item renders, icons (`ui-figma` routes) |
| marketing | `thumbnail`, `game-icon`, `concept` | Home thumbnails (16:9 crop) and the game icon, from a real game moment; approved title text is added afterwards, never drawn (`marketing-craft` skill; check with `tools/art/thumb_check.py`) |
| film-director | `storyboard`, `concept` | one panel per shot (staging, eyeline, screen direction, light direction) and colour-script vignettes per sequence; panels are proposals checked for continuity, never camera or geometry truth (`film-craft` skill) |

## 4. Steps
1. **Brief:** what the image must show and why (`rules/messages.md`): subject, purpose (target, mood, model input), the family, any input images.
2. **Manifest:** one row per image in a CSV: `id, family, identity, inputs, anchors`. `identity` describes only the subject (purpose, subject, pose or action, must-keep details, subject-specific "no" items: `references/prompt-patterns.md` §5); the style comes from the locks. Keep the manifest with the job (`knowledge/jobs/<job>/` or `content/<area>/<asset>/refs/`).
3. **Check the prompt:** `python tools/art/art_refs.py print <manifest>` and read the assembled prompt and the attached anchors. Fix the identity, not the lock.
4. **Generate (default route: ChatGPT in the agent's built-in browser, owner J009-D16).** The owner is signed in; never type credentials, never sign out. For each manifest row: open a **new normal chat** (`https://chatgpt.com/`; temporary chats cannot make images) in its own tab (several tabs run at once); set the thinking-effort control to the row's quality (I-13); paste "Create an image." plus the prompt assembled by `python tools/art/art_refs.py print <manifest>`; attach the row's input images and say each one's role; wait for "Generated image 1" (about 1-2 minutes). Read and view the result on the page, review it (§5), then ask the owner **once per batch** to approve the downloads (file list, source chat, destination `content/art/refs/<family>/<id>.png`); never download without that yes. Save the prompt beside the image (`<id>.json`: prompt, chat URL, date, route). **Clean up after every batch, whatever the answer** (owner J009-D18): approved → download, then archive each chat and close its tab; declined → archive each chat and close its tab. Archive, never delete (agents may not delete data; the owner bulk-deletes archived chats). Fallback route: `python tools/art/art_refs.py run <manifest> --limit N` (Codex; older model, lower quality in the 2026-10-21 comparison); it stops at the first failure: report it, do not retry in a loop.
5. **Review** every image (§5) before anyone builds from it. Regenerate with a fixed identity, max 2 tries per image, then report.
6. **Approve:** images the owner approves can become anchors (`art_refs.py approve <family> <id>`), so later batches match them.
7. **Hand over** the image path in the next brief's `refs`, with a note on what to take and what to ignore.

**Every agent has ChatGPT image access** through this tool (owner J002-D11, 2026-10-21: "ChatGPT has a better image gen model"). Routes: the tool (default, ChatGPT's newest image model via Codex; the owner always wants the newest model, J009-D9); a prompt pack the owner runs in the ChatGPT app for large batches; Figma `generate_image` only when the owner asks for it. Same locks in every route. No art bible yet (a kit test, a new game): `--bible templates/skill/art-bible.md` runs on the template's starter locks.

## 5. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| I-01 | **One style source.** Locks live once in the art bible; prompts never restate or tweak the style inline. A changed lock is an art-bible change the owner approves | first game: drifting styles until one shared lock per family (DestructionSimulator D-153, D-155) |
| I-02 | **Anchors beat adjectives.** Attach up to 3 approved anchors; the owner's own images first, our newest approved one last. Anchors guide the whole look (shape, color, light, materials, rendering); where an anchor and the lock disagree, the lock wins (owner J009-D11) | first game anchor library (2026-10) |
| I-03 | **Identity = subject only.** Name what it is, its parts, pose and the moment, in plain words; no style words, no franchise names | style words in identity fought the locks (first game) |
| I-04 | **Model references are single, clean views.** One subject, three-quarter view, T- or A-pose, nothing overlapping, plain background. Extra angles in one image make Tripo build extra models | first game, owner D-153 (2026-10-11) |
| I-05 | **Check before building:** views match, no impossible or hidden geometry, no extra or missing parts, the back is plausible, scale against a player is right, it reads at game distance | owner rejected first builds made without approved refs (first game and the dam game, 2026-10) |
| I-06 | **Images are inputs.** A reference is a target and a source of shapes, never the shipped asset; UI stays live layers, models are built, effects are built. Exception: marketing icons and thumbnails may ship as images after the owner reviews each one (J009-D8) | owner rule (UI built as layers; models from refs) |
| I-07 | **Franchise themes:** source stills first (kept out of git), then original designs that do not copy a franchise's characters, logos or text | first game franchise stages (2026-10) |
| I-09 | **Cut-out backgrounds:** for images that need transparency, use a plain magenta `#FF00FF` background; for pure glows, black plus a luminance-to-alpha key. Never green: a glowing subject on `#00FF00` picks up green spill in its glow | UI chat test 2026-10-21 (J002); first game ICON LOCK |
| I-11 | **Prompt budget: exact only where it matters.** Over-explained prompts give usable but stiff, odd, "AI-looking" images: the model keeps satisfying rules instead of using its own skill. Say the purpose, the subject in one or two lines, the 1-3 must-haves and the feeling; let the style come from the lock and anchors; leave camera details, lighting details, exact placement and decorative counts to the model. When an image looks stiff or strange, remove rules before adding any | owner J009-D14 ("we want to be specific in the correct way that allows it to use its creativity and skill properly"); style probe 2026-10-21: a long fixed layout made 8 styles look alike |
| I-12 | **One image, one chat.** `art_refs.py` runs every manifest row in its own new Codex session (the session id is in the image's `.json`), so a new image never edits or copies the last one. Never generate a batch in one shared ChatGPT chat: the model starts editing its earlier image and every image drifts toward the same style. For a style exploration set `anchors` to `none` (or name only that direction's own anchors) and attach no image from another direction | owner J009-D15 ("each image is in its own chat") |
| I-13 | **Quality floor: medium for every image, high for the best.** High for icons, characters and creatures, hero models, key art and marketing images; medium for everything else (concepts, props, environments, pose sheets, VFX frames, UI moods). ChatGPT web route: set the composer's thinking-effort control to Medium or High before sending (it governs how well the request is read and rewritten; the web app shows no separate image-quality control). API route: `quality` medium or high | owner J009-D17 |
| I-10 | **Working references only: attach the subject; name positions; name counts.** (Not for look, mood or concept images: there, I-11 wins.) An image of an existing character, creature or prop attaches its approved image as `inputs`; layouts say left, middle, right and the key relationship; panels and poses say "exactly N" | kit test batch 2026-10-21: the pose sheet drew a different character until the sheet was attached; a concept put the wave on the wrong side of the dam; 7 VFX panels came back instead of 3 (`references/prompt-patterns.md` §1b) |
| I-08 | **Show the owner images next to what they are for** (the sheet next to the model render, the key frames next to the frame script) in one batched review | owner gate practice, first game |

## 6. Rules (final check)
- No visual build starts from a reference the owner has not seen when the work is new-look (an L job's G2).
- No style text outside the art bible; no franchise characters, logos or real brands in prompts.
- No keys, passwords or account details in manifests or the repo; the tool uses the owner's logged-in Codex app.
- Generated images are saved with their prompt record; never overwrite an approved reference.

## 7. Self-check before returning
- [ ] Art bible exists and the family used has a lock.
- [ ] Prompt checked with `print` before `run`.
- [ ] Every image reviewed against I-05; failures listed, max 2 regenerations each.
- [ ] Paths handed over with take/ignore notes; anchors approved only by the owner.

Project overlay: if `knowledge/overlays/reference-images.md` exists, read it after this file; it wins for this game.
