> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-craft`. Source: N2 SB-01..08, IG-01..06; N3 PM-04, SB-00..15, CL-01..07; N4 B-01..B-14; `reference-images` skill (I-01..I-10); owner decisions J015-D4 (ChatGPT boards through reference-images), J015-D7 (ChatGPT boards for intent and composition; Blender previs stills become the spatial truth once models exist). Image-model facts: `knowledge/reference/film/fact-check-blender-images.md`.

# Storyboards: ChatGPT panels as staging proposals

A board is a communication panel, not concept art: it proposes what the shot shows, where things are and what moment it catches (N2 SB-04). A generated image proves nothing about geometry, lens, camera path or continuity (N2 SB-06, IG-06; N3 DN-06). The shot list and the continuity ledger stay the authority where an image is ambiguous (N3 PM-04).

## 1. Before the first panel
1. **Shot list exists** (ids, size, angle, action, purpose, continuity) at stage `plan`. Boards follow the shot list, never the reverse (N3 PM-03).
2. **Approved references exist** for every character, place and key prop in the sequence (`reference-images` families `character`, `environment`, `prop`). The first game could not start boards because most of the cast and set were missing (N4 X-01): check readiness against the shot list on day one; missing items become tickets.
3. **Overhead blocking map** for any sequence where space matters: a simple top-down drawing (Blender orthographic top view of proxies, or a plain diagram) with entrances, exits, threats, character positions per beat, the action axis and each camera's side (N1 ST-03; N2 SB-04). It goes into each panel's `inputs` when position matters.
4. **Board policy** declared in the shot list (`board_policy`): `constraint` (boards fix staging and acting; layout follows them) or `layout-may-propose` (previs may change them through review) (N3 BP-01).
5. **Art bible** has the `storyboard` family and lock (`templates/skill/art-bible.md`). No art bible yet (a kit test): copy the template into the job folder, replace the WORLD STYLE LOCK placeholder with a neutral test style, and pass that copy with `--bible`; the template's placeholder text would otherwise be sent to the model word for word.
6. **No cast or set models yet:** block a Blender greybox first (`references/blender-previs.md`) and attach each shot's greybox still as image 1 ("keep camera and positions"); the first accepted panel then serves as the identity source for the rest. Boards propose intent, mood and acting on true geometry (J015 G2 gaps G2: every panel kept the planned geography this way).

## 2. Making panels
- **One panel per request** when continuity matters; assemble and label outside the image model (N2 IG-04).
- Brief per panel: `templates/film/storyboard-brief.md`; its `identity` line goes in the manifest. Pattern: `reference-images/references/prompt-patterns.md` §5 `storyboard`.
- **Attach, don't describe:** the approved character image as image 1, the previous approved panel as image 2, the blocking map when needed; say each image's role by order (I-10; B17 advice, see the fact-check). Chaining image-to-image from earlier generations drifted proportions in the first game; always attach the approved sheet (N4 B-02).
- **Name positions and counts:** left / middle / right, facing or moving left / right, "exactly one panel", "exactly two characters" (I-10).
- **Camera moves stay in text:** a move gets a start panel and an end panel if it matters; no arrows in the image (STORYBOARD LOCK).
- Third-party reference art is mood only; never attach an image whose source forbids AI use (N4 B-12).
- Image ids are lowercase (`boss-reveal-b-r1`): `art_refs.py` refuses capitals.
- Run `python tools/art/art_refs.py print <manifest>` before `run`; stop at the first failure (often quota) and report it.
- **Regenerate as an edit** of the failed panel: "Edit image 1. Change only <the fault>. Keep everything else exactly" (`reference-images/references/prompt-patterns.md` §3). Keep one image of the budget in reserve and spend it on the most story-critical failure first.

## 3. Reviewing panels (fail even if beautiful)
Per panel, against its brief and the continuity ledger (N2 IG-05; N3 SB-15):
| Check | Fails when |
| --- | --- |
| Identity | a character, costume or prop differs from the approved reference |
| Handedness and props | the prop changes hand or appears / disappears |
| Prop state | a prop's state is wrong for the moment (lit vs dark, open vs shut, whole vs broken) |
| Contact | touching vs not touching is wrong (a hand on an object that must stay just out of reach) |
| Screen direction | travel direction or facing reverses without a planned reason |
| Eyeline | the look points away from the planned target |
| Positions and landmarks | a landmark changes side or disappears; the exit is not where the ledger says |
| Light direction | the key light side flips |
| Focal subject | the subject the shot is about is not the first thing seen at small size |
| Story purpose | the panel does not show the new information its brief names |

Then lay all panels side by side as a contact sheet in shot order and read the sequence: does each panel prepare the next; does geography hold across cuts? Max 2 regenerations per panel, then revise the plan openly or report. Store the accepted image with its full brief, the shot-list revision and the ledger; old panels stop being "approved" when the sequence changes (N3 SB-15).

## 4. When Blender stills take over
- Once the cast and set exist as models, rough-posed Blender stills from the previs cameras are the spatial truth: real scale, real positions, the actual lens (J015-D7; the first game chose this for cast and scale consistency, N4 B-01).
- ChatGPT panels stay useful for intent, mood and composition before models exist, and for colour-strip vignettes (`concept` family) per beat (N1 LC-05).
- When a panel and the previs disagree, previs wins on geometry and timing; the director decides whether the panel's intent is still met.

## 5. What to show the owner
Contact sheet in shot order with shot ids, one line of purpose per panel, the blocking map, and the open items (lens, timing: UNKNOWN until previs). Ask for approval of staging and order, not of rendering quality.
