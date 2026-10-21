---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J009-T02, Art_Director_Research_Paper.txt lines 359-602"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Art direction paper part 2: concept to direction, art bible, readability, hierarchy, measurable checks (lines 359-602)

Paraphrased notes. The paper (AP) stays outside git. Every row cites `AP:<line>`. Nothing here is fact-checked yet: claims are the paper's, listed in section 10 for the fact-check pass. The paper's research date is 2026-10-21. The paper ran no check itself: no image generated, no scene built, no screenshot measured, no player study (AP:17, outside this range). Every procedure below is a proposed check to run on the real project, not a result.

## 0. How to read

| Key | Meaning |
| --- | --- |
| AP:n | line n of `Art_Director_Research_Paper.txt`. One paragraph = one line. Source register = AP:1013-1695. |
| Tag | VERIFIED (published data, a measured study, or an explicitly documented platform or tool capability; says nothing about art quality), EXPERIENCE (a studio, artist or director reports its own process; no universal rule), OPINION (the paper's own proposal, interpretation, example or process; source id O00, dated 2026-10-21, "not an external study"). Tags are the paper's, not mine. |
| Src | paper source id, resolved in section 11 with its date. "undated, accessed D" = living page with no date; access is not publication. O00 = the paper itself. |
| Studio claim | marked [studio] = documented by the studio in its own post; [artist] = one artist's account; [paper] = the paper's interpretation of a source. |
| Row IDs | D direction, F feedback, BF art bible field, LK fictional example lock, RD readability, HI hierarchy, SH shape/palette principle, M measurable check card, N number, C claim, X contradiction or limit. |
| Check card | Fixed keys: Inputs, Procedure, Record, Pass (as the paper states it), Never proves, Tag/Src. A card whose inputs are missing returns `unassessed`, never an invented number (AP:485, 553). |
| Extractor additions | Marked "(extractor)". They are standard definitions added so a formula is complete; they are not paper text. |

## 1. Section 2: from concept to visual direction (AP:359-399)

### 1.1 Starting input and pillars

| ID | AP | Lesson (check or step) | Tag | Src |
| --- | --- | --- | --- | --- |
| D1 | 361 | Start from a compact designer brief with: player fantasy, repeated decisions, camera, movement speed, number and kinds of simultaneous actors, emotional tone, important state changes, target devices. Before asking for concept images, list the visual consequences the brief leaves missing. | OPINION | O00 |
| D2 | 361 | Do not push competitive-readability conventions onto a calm collection game; do not give a threat-heavy game decorative quietness. A game about careful target choice needs different emphasis from a calm collector even with the same friendly stylized cast. | OPINION | O00 |
| D3 | 363 | Turn each design pillar into an observable visual hypothesis. Paper example: "powerful destruction" becomes large readable masses that break into comprehensible chunks, clearly separated impact and aftermath states, and a hierarchy that makes the player's action look causal. | OPINION | O00 |
| D4 | 363 | A hypothesis is not yet a particle count, polygon budget or timing. Ask specialists to propose the implementation and show how it keeps the hypothesis. | OPINION | O00 |

### 1.2 Bounded exploration

| ID | AP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| D5 | 367 | Explore genuinely different directions, not palette swaps. For each candidate say what it changes: proportion, material language, density, light, historical reference, camera reading or emotional register. | OPINION | O00 |
| D6 | 367 | The number of candidates is a project decision. The paper found no evidence for an optimal number of style directions, mood-board images or review rounds. Continue only while alternatives can change the decision; stop when new images are cosmetic variations that test no real uncertainty. | OPINION | O00 |
| D7 | 369 | Keep three buckets apart: research reference, exploration, approved target. A mood board may hold conflicting examples because it records a question; an approved target resolves the relationship. Label every image by purpose, source and approval state so an AI does not treat all attached pictures as equally binding. A material-roughness reference need not set proportion; a composition reference need not set palette. | OPINION | O00 |
| D8 | 371 | Present each direction candidate as a comparable packet: the same gameplay problem; a representative character and environment; a UI and effect sample; a gameplay-camera composition; a small-screen view; the tradeoffs in words. These are proposed evidence categories, not a fixed image count. | OPINION | O00 |
| D9 | 371 | Match camera and exposure across candidates where possible. If one candidate uses a more flattering camera or stronger light, say so; do not credit the style for the camera's effect. | OPINION | O00 |
| D10 | 373 | Before production lock identity-bearing decisions and the review procedure. Do not lock details that depend on rig, camera, rendering or interaction tests. | OPINION | O00 |
| D11 | 373 | A target render is a visual hypothesis, not proof that Roblox can render it at the needed cost. Build a representative test scene holding the important combinations, not only the easiest asset. | OPINION | O00 |
| D12 | 373 | The owner picks the direction after the art director has stated both its appeal and its unresolved risks. | OPINION | O00 |
| D13 | 383 | At greenlight freeze what specialists need: intended fantasy, gameplay camera, identity cues, material grammar, palette roles, composition priorities, approved anchors. Allow change only through explicit change records, never by silently altering prompts mid-production. | OPINION | O00 |
| D14 | 383 | Do not run an approval treadmill. Ask whether the alternatives expose materially different choices and whether uncertainty is resolved, not whether a quota is met. | OPINION | O00 |

### 1.3 Studio examples with their narrow meaning

| ID | AP | What the source reports | Scope limit the paper states | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| D15 | 379 | Little Demon Tristana [studio, artist account]: three theme pillars; mood-board exploration; generally 8-10 chroma designs before choosing one. | These are chroma concepts, not a number of whole-game directions. | EXPERIENCE | R09, 2019-05-15 |
| D16 | 379 | Same report: the splash first resolved composition, lighting, anatomy and values in a thumbnail before greenlighting detailed rendering. Reported splash duration 4-6 weeks. Team held daily reviews; this illustrator asked for feedback once or twice a week. Paintovers fixed issues such as perspective. | One artist, one splash, 2019. Not a quota (AP:395). | EXPERIENCE | R09, 2019-05-15 |
| D17 | 381 | Separate 2018 account [studio]: a splash estimated at 75-100 hours, average four-week schedule including other duties. Internal illustrators direct outsourced artists, paint over peers' work, join product meetings. | Historical schedule and staffing. Not an AI-agent completion-time estimate. | EXPERIENCE | R10, 2018-07-26 |
| D18 | 379 | Lesson for the agent (paper's reading): resolve composition, light, anatomy and values in a low-detail thumbnail first, then spend rendering effort. | Paper's transfer; the thumbnail-first order is reported by R09, the "AI agent should do it" part is OPINION. | EXPERIENCE + OPINION | R09, O00 |

### 1.4 Feedback as a controlled experiment

| ID | AP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| F1 | 387 | Feedback record, in this order: asset/version and reviewed view; observed issue; violated lock or intended player reading; why it matters; priority; requested outcome; allowed variation; reference comparison; required proof; owner decision if a style lock changes. | OPINION | O00 |
| F2 | 387 | Avoid vague notes ("make it more premium"). Paper's model note: the decorative rim is the brightest area while the target indicator vanishes on the sand; lower the rim or move emphasis to the target, then show the same encounter at target output size. The specialist chooses how. | OPINION | O00 |
| F3 | 389 | Paintovers: separate literal geometry changes, composition guidance, value grouping and temporary markup. Store the unmodified screenshot, the overlay and the written purpose. | OPINION | O00 |
| F4 | 389 | A red arrow in a paintover is a direction mark, not a proposed red object in the game. Never let an AI train its next reference on annotation colors without removing or interpreting them. | OPINION | O00 |
| F5 | 389 | F1-F4 are proposed safeguards, not measured Riot methods. | OPINION | O00 |

Paper table AP:391-397: Tristana chroma exploration is a scoped example (8-10 chroma designs; EXPERIENCE; R09, 2019-05-15) / review cadence is not a quota (daily team review; artist once or twice weekly; EXPERIENCE; R09, 2019-05-15) / direction candidates must test meaningful alternatives (count is a project decision; OPINION; O00, 2026-10-21).

## 2. Section 3: the art bible (AP:401-467)

### 2.1 Principles

| ID | AP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| BF-p1 | 403 | The bible is a decision tool, not a picture encyclopedia. A specialist must be able to answer: what is fixed, what may vary, which anchor shows the rule, how approval is judged. Keep short working rules apart from deeper research and examples. | OPINION | O00 |
| BF-p2 | 403 | No sourced universal page count exists. Test usability like this: can another maker produce a compatible result without inventing a missing decision? | OPINION | O00 |
| BF-p3 | 407 | Text plus approved visual examples. An empty field means an unresolved decision, never permission for an agent to fill it silently. | OPINION | O00 |

### 2.2 Template: every field (AP:409-433)

Compare with `templates/skill/art-bible.md` (extractor note): that file today holds image-prompt locks per family and an anchor folder note. Most fields below (permitted variation, anchor register columns, cross-craft contracts, technical envelope, review and change control, forbidden confusions, scale references) have no slot there yet. Whether to add them is the lead's call.

| ID | AP | Field | Required content | Review consequence | Tag | Src |
| --- | --- | --- | --- | --- | --- | --- |
| BF1 | 411 | Identity and intent | Game name; player fantasy; designer pillars; owner decision; art direction revision. | Reject assets that promise a different fantasy even when each is polished. | OPINION | O00 |
| BF2 | 413 | Scope and camera | Gameplay viewpoints; target capture conditions; representative device classes; crowd states. | Compare at real use conditions, not only close-up renders. | OPINION | O00 |
| BF3 | 415 | Core visual locks | Meaningful rules for shape, proportion, value, palette roles, material treatment, edge language. | Every requested change records which lock it touches. | OPINION | O00 |
| BF4 | 417 | Permitted variation | Differences allowed by biome, faction, rarity, character role, mood or event. | Keeps variety without calling every difference drift. | OPINION | O00 |
| BF5 | 419 | Anchor register | Approved images with: purpose; asset or scene version; camera; lighting; crop; status. | Only current approved anchors bind new work. | OPINION | O00 |
| BF6 | 421 | Shape and silhouette | Dominant masses; recurring motifs; identity-bearing features; forbidden confusions. | Check the isolated silhouette and the silhouette in scene context. | OPINION | O00 |
| BF7 | 423 | Color and value | Semantic roles; accent restrictions; neutral regions; light and dark relationships. | Compare meaning and hierarchy, not raw color counts alone. | OPINION | O00 |
| BF8 | 425 | Materials and lighting | Material families; stylization of highlights and shadows; target lighting scenarios. | Review material and light together, without double-baking effects. | OPINION | O00 |
| BF9 | 427 | Detail and scale | Where detail belongs; where it is suppressed; scale references; camera implications. | Reject noise that defeats the intended focal structure. | OPINION | O00 |
| BF10 | 429 | Cross-craft contracts | VFX, UI, motion and sound roles; priority during overlapping events. | Test combinations; resolve competing emphasis. | OPINION | O00 |
| BF11 | 431 | Technical envelope | Supported rendering modes; device evidence; current known limits; unresolved measurements. | A visually approved asset is not runtime approved. | OPINION | O00 |
| BF12 | 433 | Review and change control | Approval owners; evidence packet; exception process; revision history; migration plan. | Prevents silent change and contradictory feedback. | OPINION | O00 |

### 2.3 Filled example: Lantern Workshop (FICTIONAL)

The paper authored this example. It is not a shipped game, not a case study, not measured, not built, not tested (AP:439, 459). Working title Lantern Workshop: a stylized mobile game; the player restores a miniature harbor town by collecting salvaged odd objects and building warm, useful inventions; mood curious and reassuring, with clear interaction opportunities, not constant danger. The owner must approve or revise it before production. Use it as a writing pattern, not as content. Its decisions invent no universal numeric rules.

| ID | AP | Lock in the example | Pattern to copy (what a good lock does) | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| LK1 | 441 | Shape: buildings = sturdy large masses, rounded corners, visible joinery; interactables carry a distinct graspable, turnable or openable feature; decorative clutter must not reuse an interaction cue's exact silhouette; playful asymmetry must look assembled on purpose, not warped. Specialist picks the modeling method; the director checks the shape language. | A shape lock names a forbidden confusion (clutter vs cue) and who decides method. | OPINION (fictional) | O00 |
| LK2 | 443 | Proportion: player and key tools stay readable together in the game camera; handles visibly grippable, doors say "entry", machines show their operation. No numbers are given as "industry constants". The modeler proposes dimensions in the project scale; animator and level builder test reach, traversal and camera occlusion before dimensions become anchors. | Proportion is tested by reach, traversal and occlusion before it is locked. | OPINION (fictional) | O00 |
| LK3 | 445 | Color and value: cool weathered harbor base; warm light marks repaired or active elements. Warm must not mean reward, warning and selection all at once. An interaction cue also gets a stable icon, shape or motion. A storm may change mood but must not flip UI meaning. The palette is named roles with approved swatches; swatch count is not a quality target. | Roles, not counts; one meaning per color treatment; a non-color backup cue. | OPINION (fictional) | O00 |
| LK4 | 447 | Material: painted wood, dull metal, fabric and glass stay distinct at the intended camera; texture supports the difference, no evenly spread noise; glossy highlights reserved for justified materials or story. Material specialist proposes mesh/texture/shader within documented Roblox capability; art director judges look and hierarchy; performance review decides affordability. | Appearance review and cost review are separate approvals. | OPINION (fictional) | O00 |
| LK5 | 449 | Lighting: everyday scenes keep interaction surfaces and player silhouette readable. Evening may be warmer and more directional, but no key control may fall into atmospheric shadow. Approve a reference capture per meaningful lighting situation; record the actual environment and exposure of each anchor. | One neutral anchor does not define every mood; anchors record their lighting. | OPINION (fictional) | O00 |
| LK6 | 451 | UI: panels feel like well-made workshop labels, not noisy wood; important actions stay distinct from decoration; UI designer owns layout and interaction; art director reviews shape, tone and emphasis fit; accessibility and legibility are constraints, not style exceptions. | Style never overrides legibility. | OPINION (fictional) | O00 |
| LK7 | 453 | Motion and sound: purposeful mechanisms, satisfying state changes; secondary motion supports character and material without bouncing everything; sound follows the same material and event hierarchy (a minor decoration not as loud as a finished repair). Animator and sound designer choose timings; the director reviews the shared impression and event priority. | Event priority is shared across picture, motion and sound. | OPINION (fictional) | O00 |
| LK8 | 455 | Anchor packet (categories, not a required seven): player silhouette; repaired workshop; unrepaired dock; tool family; an interaction state; an evening gameplay capture; a busy representative scene. Each anchor records what it controls. A tool reference does not override the evening lighting target; key art does not override gameplay-camera scale. | An anchor binds only what it states it controls. | OPINION (fictional) | O00 |
| LK9 | 457 | Allowed variation: neighborhoods vary in local motif and weathering; inventions may have distinctive secondary shapes; events may change mood and decorative color. Protected: stable interaction cue, core material families, scale relationships, readable player silhouette. An exception needs a reason and a replacement example, not "it looks better". | Exceptions carry a reason plus a new example. | OPINION (fictional) | O00 |
| LK10 | 459 | Acceptance packet: actual screenshots against the relevant approved anchor under matched conditions; run silhouette, value, semantic-color and small-screen checks; record runtime device and rendering mode separately; when atmosphere and interaction clarity conflict, show the owner both options with the tradeoff and do not quietly reduce the player's ability to act. | Packet = matched capture + four checks + device/mode + owner choice on conflict. | OPINION (fictional) | O00 |

Paper table AP:461-467: published League VFX guide has an explicit structure (4 goals, 5 areas; EXPERIENCE; R06, 2017-10-25) / bible records locks plus allowed variation (no universal page count; OPINION; O00, 2026-10-21) / filled Lantern Workshop example is authored (not built or benchmarked; OPINION; O00, 2026-10-21).

## 3. Section 4: readability and gameplay clarity (AP:471-507)

### 3.1 Published guide structure

| ID | AP | Lesson | Tag | Src, date |
| --- | --- | --- | --- | --- |
| RD1 | 477 | [studio] The public League VFX guide announcement says several teams lacked one standard for successful effects. It organizes four goals (gameplay clarity, reduced clutter, champion theme, player delight) through five areas (gameplay, value, color, shape, timing), reports months of revision, uses examples and visual explanations. | EXPERIENCE | R06, 2017-10-25; R07, 2017-10-26 |
| RD2 | 477 | Provenance limit: the indexed announcement and the release thread establish it. The legacy PDF redirected, so the paper did not read or measure the full PDF. Do not cite PDF content. | EXPERIENCE | R06, R07 |
| RD3 | 479 | Copy the structure, not the unexplained vocabulary. Every lock needs: purpose, scope, approved example, contrasting failure, test. "Clean stylized fantasy" fails because it decides neither where detail goes nor which colors carry gameplay meaning. | OPINION | O00 |
| RD4 | 479 | Reviewable lock pattern (paper's own example): interactive targets keep an uncluttered outer contour in the gameplay camera; decorative emitters may not cross that contour during the attack tell. It is a proposed project rule, not a Riot quotation, and needs stated exceptions and test clips. | OPINION | O00 |

### 3.2 Resistance Illaoi correction loop and the raster-width check

| ID | AP | Lesson | Tag | Src, date |
| --- | --- | --- | --- | --- |
| RD5 | 483 | [studio] Development report: an attack indicator was too busy; an opacity change made dodging easier than against the base effect; very fine lines of one pixel or less turned jagged; the team cut explosion effects and removed oil spills. | EXPERIENCE | R08, 2018-02-20 |
| RD6 | 483 | [studio] A red projectile was a problem against green terrain in colorblind tests. A larger luminous yellow core and more contrast near the dangerous tip improved focus. Workflow: Photoshop colorblind filters plus feedback from colorblind staff. The paper calls this stronger than saying grayscale or one simulated filter proves accessibility. | EXPERIENCE | R08, 2018-02-20 |
| RD7 | 485 | Treat the one-pixel finding as a warning about subpixel fragility, not a universal two-pixel minimum. | OPINION | O00 |
| RD8 | 485 | Report a pass only against explicit project criteria. If the criterion or a representative image is missing, return unassessed and make no number up. | OPINION | O00 |

### 3.3 Primitive recognition (Feeney art) and the ablation check

| ID | AP | Lesson | Tag | Src, date |
| --- | --- | --- | --- | --- |
| RD9 | 489 | [studio, artist account] Crude placeholder splashes served as a fast check of personality and distinct appearance. Difficulty drawing Taliyah recognizably in that simple style exposed a weak silhouette; changes improved the quick read. | EXPERIENCE | R11, 2017-02-17 |
| RD10 | 489 | Limit: a production heuristic, not a quantified perception study, and not proof that every character must be identifiable from an arbitrary scribble. | EXPERIENCE | R11 |
| RD11 | 491 | Proposed AI version: a silhouette/feature-ablation test. Remove textures and lighting, keep the gameplay camera, ask which approved identity features survive. Pair an unlabeled candidate with possible identities or functions; keep the answer and the uncertainty. | OPINION | O00 |
| RD12 | 491 | A vision model's confident label is not a validated human recognition rate. Use the result to flag ambiguity; test representative people before any claim about player comprehension. | OPINION | O00 |

### 3.4 Task-based clarity review

| ID | AP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| RD13 | 495 | Start from the player's decision, not a generic image score. Ask: what must be noticed, distinguished or predicted now; which is the relevant target; what competes; what is the cost of confusion. A pickup, a lethal attack and optional decoration need not get equal prominence; one asset has different needs in a quiet scene and a crowded fight. | OPINION | O00 |
| RD14 | 497 | Role-specific captures: targeting = target separation and facing; navigation = route and destination cues; interaction = affordance and its state; combat = source, path, area, result of the action; collection = identity and rarity without making every object loud. | OPINION | O00 |
| RD15 | 497 | Do not turn competitive combat guidance into a rule that every game must look urgent. | OPINION | O00 |
| RD16 | 499 | Phone review: separate physical display, rendered resolution, UI scale, crop, viewing conditions. A shrunk desktop screenshot is a stress test only; it misses touch occlusion, dynamic resolution, display brightness and player behavior. Test the real supported devices and interaction before claiming readability. Do not assume all children share reading ability, acuity, language or experience. | OPINION | O00 |
| RD17 | 507 | Roblox's own documentation says emulation cannot fully reproduce real hardware. P05 (Studio "Actual Resolution" option) is cited beside it; the paper gives no explanation of P05 beyond that. | VERIFIED | P03 / P05, undated, accessed 2026-10-21 |

Paper table AP:501-507: inspect raster-scale critical cues (Illaoi lines of one pixel or less aliased; EXPERIENCE; R08, 2018-02-20) / recognition tests must use the relevant task (project-specific acceptance; OPINION; O00) / phone emulation does not establish real hardware behavior (no universal screen size; VERIFIED; P03/P05, undated, accessed 2026-10-21).

## 4. Section 5: visual hierarchy and focus (AP:511-537)

| ID | AP | Lesson (check or step) | Tag | Src, date |
| --- | --- | --- | --- | --- |
| HI1 | 513 | A focal point is not permanently the brightest thing. The focus depends on task, camera and event. Name the current priority, then check the combined frame supports it. If UI, character, environment and effects each maximize local contrast, the whole can lack hierarchy although each part passes alone. | OPINION | O00 |
| HI2 | 515 | Screen ownership, not competition: level = navigable structure and calm regions; character art = identity; VFX = event information; UI = persistent and state controls; animation = action and intent. Negotiate per game. A foreground effect may dominate briefly for a major event but must not hide what the player needs to respond. | OPINION | O00 |
| HI3 | 517 | Layer review: compare the scene without UI, without effects, and fully composed. Check whether a low-priority layer becomes the main focal point. This is a diagnostic cut, not advice to ship stripped art. If removing a layer suddenly makes the action understandable, investigate that layer's value, density, placement, motion or duration with its specialist. | OPINION | O00 |
| HI4 | 519 | Calm space is a resource (low-detail wall behind a character, quiet area near key UI, a pause between bursts, restrained surface around a focal ornament). Do not force empty backgrounds everywhere; richness may serve exploration and mood if the current task stays legible. Mark where richness helps and where it competes. | OPINION | O00 |
| HI5 | 523 | [studio, VALORANT Icebox account] Level, concept, environment, lighting and QA teams work together. High-level concepts set the iconic direction; local concepts then fit the tested greybox. Artists may vary details but keep critical geometry. Materials avoid excess contrast and darkness where characters must read. Decorative detail generally above player height. Simple recognizable locations and colors help callouts. Story may extend into inaccessible spaces without changing playable angles. | EXPERIENCE | R12, 2020-11-16 |
| HI6 | 525 | [studio, 2020 shader account] Balances art, performance and competitive integrity. Quality-level parity; artist-controlled light-response gradients; avoiding dynamic shadows in playable spaces at that time because lower settings could lose information. The 144 FPS and 6.9 ms figures are the source's historical target and stated approximation (not exact reciprocals), not Roblox phone targets. No assumption that Roblox exposes VALORANT's custom shader work. | EXPERIENCE | R13, 2020-06-30 |
| HI7 | 527 | [paper's interpretation] Separate protected interaction space from expressive staging space. Test hierarchy at the lowest supported quality as well as the beauty preset. Ask for a target image plus a degraded-quality counterpart. A style is incomplete if a critical cue exists only in the premium render path. Proposed studio practice, not VALORANT art law. | OPINION | O00 |
| HI8 | 531 | Table row only: Riot's historical Rift hierarchy is contextual (environment, champions, VFX, restrained UI). The body text of the range does not explain it; use only this one-line statement. | EXPERIENCE | R04, reprint 2014-11-11 |

Paper table AP:529-535: Riot historical Rift hierarchy is contextual / review combined and isolated layers (no fixed contrast allocation; OPINION; O00) / do not transfer VALORANT performance targets to Roblox (historical 144 FPS and source-stated 6.9 ms; EXPERIENCE; R13, 2020-06-30).

## 5. Section 6: shape language, color, value and the measurable checks (AP:539-602)

### 5.1 Principles before measurement

| ID | AP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| SH1 | 541 | Shape language must be consistent enough for this game. Do not rely on a universal dictionary (triangle = evil, circle = friendly). Meaning depends on culture, context, material, pose, composition and the game's own learned conventions. Treat a shape association as a hypothesis to test against this fantasy and audience. | OPINION | O00 |
| SH2 | 543 | Write palette rules by function first, counts later. Roles: background support, character identity, interaction, team, danger, reward, disabled state, special narrative emphasis. Decide where colors may overlap and where they must stay distinct. A large palette is coherent if roles are controlled; a tiny one is confusing if one treatment signals incompatible states. No universal palette size. | OPINION | O00 |
| SH3 | 545 | Value structure is not the same as desaturation in an arbitrary editor. State which transformation is used and what it can show. Compare the key object against its local surroundings, not only the global average: a global histogram can stay similar while a key character vanishes on one background. Record both local comparison and full-frame context. | OPINION | O00 |
| SH4 | 547 | A swatch sampled from a screenshot carries lighting, material, tone mapping and display encoding. Never silently replace the bible's authored base color with the shaded pixel value. Keep three records apart: authored palette, rendered appearance, sampled measurement. When reference and render disagree, find which stage caused it before asking the modeler to repaint. | OPINION | O00 |

### 5.2 Formulas (copy exactly; they become code)

| ID | AP | Formula | Notes | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| FM1 | 551 | Normalize an 8-bit sRGB channel: c = value / 255, for R, G, B separately. | Scope: 8-bit channels. | VERIFIED | A06 |
| FM2 | 551 | Linearize each channel: lin(c) = c / 12.92 if c <= 0.04045; otherwise lin(c) = ((c + 0.055) / 1.055) ^ 2.4. | The older switch point 0.03928 was corrected in May 2021 (AP:551). Use 0.04045. | VERIFIED | A06 |
| FM3 | 551 | Relative luminance: L = 0.2126 * R_lin + 0.7152 * G_lin + 0.0722 * B_lin. Output range 0 (darkest black) to 1 (lightest white) per A06 key line. | Call it WCAG luminance only if exactly this was computed; an arbitrary desaturation slider is not it. | VERIFIED | A06 |
| FM4 | 563 | Contrast ratio = (L_lighter + 0.05) / (L_darker + 0.05). Keep the unrounded result. | A04 says the computed value must not be rounded up to pass. | OPINION (procedure) over VERIFIED thresholds | O00 / A04 |
| FM5 | 587 | Edge density = (number of edge pixels) / (number of valid pixels in the specified region). Edge map from OpenCV Canny with fixed resolution, smoothing and thresholds. | "Valid pixels" is not defined further in the paper; define the mask and keep it fixed. | OPINION over VERIFIED tool | O00 / A12 |
| FM6 | 579 | Silhouette IoU = area(A and B) / area(A or B), for aligned masks (extractor: standard definition; the paper names IoU, gives no formula). | Align camera, pose, scale first. | OPINION | O00 |
| FM7 | 569, 571 | Color difference: CIEDE2000 on Lab values via sRGB-to-Lab conversion (scikit-image provides both; paper cites version 0.26.0 docs). Document the color space and calculation used. | Paper sets no DeltaE threshold. | VERIFIED capability / OPINION use | A11 / O00 |

### 5.3 Check cards

#### M1 Luminance / grayscale conversion

| Key | Content |
| --- | --- |
| Inputs | Original color image (kept unmodified); gameplay-camera capture; scene state; the conversion used. |
| Procedure | Convert with FM1-FM3 (or record the other method exactly). Never overwrite the color original. Treat artistic "value" as a separate idea that may live in another image representation (the paper names none). |
| Record | Conversion name and formula; capture size; scene state; device and render mode. |
| Pass | No numeric pass exists. Pass = the approved identity and gameplay-cue test succeeds in the required scene states; fail = a documented lock is violated (AP:553). |
| Never proves | Full accessibility, aesthetic quality, readable motion (AP:555). Intentionally isoluminant decorative color can be valid; do not flatten the whole game to stark light/dark just to raise a global contrast score. Separate essential cues from atmosphere and decoration. |
| Tag / Src | FM1-FM3 VERIFIED A06 (2026-10-21 access); use rules OPINION O00. AP:551, 555. |

#### M2 Local object-versus-background value check (masks)

| Key | Content |
| --- | --- |
| Inputs | Capture; object mask; background mask; list of nearby competitors (effects, signs, UI). |
| Procedure | Compute the luminance distribution (M1) of object and background. Inspect contrast around the true object boundary. Compare the focal subject with nearby competing effects, signs, UI; do not require everything to be high contrast. |
| Record | Diagnostic crop; both masks; the computed distribution; boundary-region definition (the paper gives no ring width, so record the width used); full-frame context. |
| Pass | Same as M1. If no numeric acceptance range is set, report the measurement as diagnostic and ask for a project decision. Do not invent a cutoff (AP:553). |
| Never proves | That a scene-wide average is safe: a global mean can hide a threat disappearing against one patch (AP:545, 553). |
| Tag / Src | OPINION O00. AP:545, 553. |

#### M3 Contrast ratio against a declared standard

| Key | Content |
| --- | --- |
| Inputs | Foreground and background color for each UI role and accessibility mode; the rendered composited presentation; the standard the studio adopted for that role. |
| Procedure | State which standard applies to which role and mode. Never mix standards silently. Compute FM4 on the authored pairs and on the rendered, composited result (translucent HUD panels, outlines, glow, gradients, moving backgrounds). For text over variable backgrounds measure against the lowest-contrast background area (Xbox guidance, A07). Do not use only antialiased edge pixels in place of fill colors; and a passing fill does not guarantee a thin stroke survives downscaling. A dark backing panel or outline may fix the issue without changing the world palette. UI specialist picks the fix. |
| Record | Standard and clause; both colors; unrounded ratio; background sample set (not just the easiest background); capture size. |
| Pass | Threshold table in 5.4. Thresholds belong to their source and scope. |
| Never proves | That a game-world prop or enemy needs this ratio. WCAG numbers are web reference standards, not Roblox rules and not evidence for every enemy pixel (AP:559). One screenshot on the easiest background is insufficient (AP:563). |
| Tag / Src | VERIFIED thresholds A04, A05, A07; EXPERIENCE A09; procedure OPINION O00. AP:559-563. |

#### M4 Semantic color roles and redundant channels

| Key | Content |
| --- | --- |
| Inputs | Role list (threat, ally, interactable, reward, disabled, selected, environmental accent, purely decorative); captures from world, VFX, UI and marketing. |
| Procedure | Define roles before extracting swatches. Check the same role keeps its meaning across world, VFX, UI and marketing. Check reinforcing channels (shape, icon, pattern, position, motion, sound) for visibility and timing, not just their count. |
| Record | Role-to-treatment table; the channels carrying each key cue; where each channel is visible and when. |
| Pass | Key cues use an extra sensory or visual channel instead of color or audio alone (A08, Xbox). The paper adds no numeric rule. |
| Never proves | That counting channels equals clarity. |
| Tag / Src | VERIFIED A08; procedure OPINION O00. AP:567. |

#### M5 Palette extraction and comparison to anchors

| Key | Content |
| --- | --- |
| Inputs | Material/base-color reference images (separate from lit gameplay captures); lit gameplay captures; masks; approved role anchors. |
| Procedure | Mask out text, sky, transparency and UI when outside the question. Extract role-specific representative colors, or cluster a controlled sample using the same algorithm and settings across versions. Convert sRGB to Lab; compare candidate swatches with approved role anchors using CIEDE2000 (FM7); then inspect the matching image patches. |
| Record | Cluster count as an analysis parameter (not "the right number of colors"); algorithm, seed and settings; color space; difference formula; masks; the authored/rendered/sampled split (SH4). |
| Pass | Combines role assignment, authorized exceptions and an approved tolerance. Paper: no generic DeltaE threshold counts as proof of style consistency; no global palette count alone passes. A small difference can matter for a locked team color; a large one can be intended across day/night. |
| Never proves | Spatial correctness: a histogram drops where colors sit, so danger red on a harmless prop can still fail the design. Lighting, gradients, antialiasing and texture make many pixel colors even for a small authored palette. |
| Tag / Src | VERIFIED capability A11; method OPINION O00. AP:569, 571. |

#### M6 Color-vision-deficiency simulation

| Key | Content |
| --- | --- |
| Inputs | Original capture; grayscale; simulator output. |
| Procedure | Inspect the relevant simulations next to grayscale and the original. Check that essential states stay distinguishable through redundant cues. When practical, test with affected players. Do not "fix" the game with one global filter while team colors or unlabeled states stay ambiguous. |
| Record | Simulator and mode (e.g. Color Oracle v1.3, released 2018-05-05; site updated 2020-01-02; a free full-screen simulator for Windows, Mac, Linux; older tool, current compatibility untested by the paper). |
| Pass | No numeric rule. Essential states distinguishable by more than the simulated color. |
| Never proves | That every player's vision is covered. One simulated filter or grayscale does not prove universal accessibility (AP:483, 573). |
| Tag / Src | VERIFIED tool facts A10; procedure OPINION O00; field evidence EXPERIENCE R08. AP:483, 573. |

#### M7 Silhouette test

| Key | Content |
| --- | --- |
| Inputs | Subject at intended pose and game camera; mask with materials, textures and internal shading removed; the most similar approved asset; the bible's identity-bearing regions. |
| Procedure | Inspect identifying outer contours and negative space: weapon direction, head/torso relationship, limb separation, vehicle front and rear, building entrance. Repeat at the final presentation size, not only a large editor preview. |
| Record | Mask bounding-box width and height in pixels; fraction of viewport width and height; visible versus occluded area; confusion with the most similar approved asset. |
| Pass | None of these measures has a universal acceptable percentage in the reviewed evidence (AP:577). Use bible-defined criteria. |
| Never proves | Appeal, or player recognition in the real game. |
| Tag / Src | OPINION O00 (field heuristic EXPERIENCE R11). AP:577, 489. |

#### M8 Thumbnail and silhouette overlap

| Key | Content |
| --- | --- |
| Inputs | The actual icon/thumbnail slot or phone viewport; aligned masks of old and new silhouette. |
| Procedure | Do not assume a square crop or a fixed 64-pixel image. Preserve aspect ratio. Document the resampling method. Align camera, pose, scale before computing IoU (FM6). Use identity-bearing regions from the bible. |
| Record | Slot size; aspect ratio; resampling method; alignment method; IoU value; regions checked. |
| Pass | No threshold. IoU measures change only. |
| Never proves | Whether the change improves appeal. IoU near 1 can still hide the loss of a small critical weapon tip; a redesign that lowers overlap can be right. |
| Tag / Src | OPINION O00. AP:579. |

#### M9 Recognition test (human or AI screening)

| Key | Content |
| --- | --- |
| Inputs | Crops/captures at presentation size; the relevant task (target, facing, team or function). |
| Procedure | Ask reviewers or test players to identify target, facing, team or function without giving the answer in the prompt. Define the decision criterion before testing. Keep contradictory results. AI-only screening must report uncertain and ambiguous cases, not label every crop confidently. |
| Record | Mistakes; time-to-response; the encounter context; criterion; uncertain cases. |
| Pass | Project criterion set before the test. No universal exposure time, participant count or pass percentage is justified (AP:581). |
| Never proves | Human comprehension from a model label (AP:491). Owner acceptance is still required for new style directions. |
| Tag / Src | OPINION O00. AP:491, 581. |

#### M10 Preattentive-cue test design (evidence, not a threshold)

| Key | Content |
| --- | --- |
| Inputs | Cue candidates in realistic visual competition (lighting changes, camera motion, occlusion, particles, competing objectives). |
| Procedure | Test cues in realistic competition rather than a simple shape-vs-color ranking. |
| Record | Scene conditions; cue type; detection results. |
| Pass | None. The study result is a scoped finding: in a controlled 3D scene study, color and motion were reliably detected within 250 ms and shape detection was weaker. The preference experiment used 22 participants, 11 shared with the first experiment, and always showed motion before color. The authors warn that uniform scenes lacked changing lighting, camera motion, occlusion, particles and competing objectives, and display conditions were not fully controlled. |
| Never proves | A minimum Roblox telegraph duration; "every collectible should glow blue"; that silhouettes do not matter (AP:583). |
| Tag / Src | VERIFIED A14, 2026-05-13 (study facts); use limits OPINION O00. AP:583. |

#### M11 Clutter by edge density

| Key | Content |
| --- | --- |
| Inputs | Approved and candidate captures at equal resolution; region masks; Canny thresholds; smoothing setting. |
| Procedure | Compute FM5 on the same region with resolution, smoothing and thresholds held constant. Use it to find change in texture noise or competing detail between approved and candidate. |
| Record | Region definition; valid-pixel mask; resolution; smoothing; both Canny thresholds; software version (paper cites OpenCV 4.12.0 docs). |
| Pass | No numeric rule. Diagnostic only. |
| Never proves | Clutter in general: stylized outlines raise edge density on purpose, and a single bright distracting effect can dominate attention with few edges. |
| Tag / Src | VERIFIED capability A12 (version 4.12.0 docs; undated; accessed 2026-10-21); procedure OPINION O00. AP:587. |

#### M12 Hierarchy by regions, downsample and blur

| Key | Content |
| --- | --- |
| Inputs | Capture; region labels written before showing a model the image (must notice now / read next / atmospheric). |
| Procedure | Use low-detail or downsampled views and a controlled blur as diagnostic variants. Compare the focal subject's signal with adjacent busy regions and check the intended decision is still possible. Also run HI3 (without UI, without effects, full). |
| Record | Region labels; downsample factor; blur parameters; variant list. |
| Pass | Task-specific. The intended decision stays possible. |
| Never proves | Anything about a visual impairment: the squint test is an artist heuristic, not a calibrated model. More empty space, fewer colors, maximum contrast or lowest edge count is not better art in every genre. |
| Tag / Src | OPINION O00. AP:589. |

#### M13 Timeline of overlapping animation, VFX, UI

| Key | Content |
| --- | --- |
| Inputs | Captured frames of the event with sound present and with sound absent. |
| Procedure | Record when the cue first becomes visible, when it becomes interpretable, and when the player must act. Check whether an effect hides the anticipation or the next target while looking good in isolation. |
| Record | Three timestamps; sound on/off result; frames captured. |
| Pass | Combat clarity is not approved from one attractive impact frame. If the relevant frames cannot be captured the review is incomplete, not a pass. |
| Never proves | A required telegraph duration (paper gives none; see M10). |
| Tag / Src | OPINION O00. AP:591. |

#### M14 Raster-width of critical lines (from section 4)

| Key | Content |
| --- | --- |
| Inputs | The same interaction rendered at the declared device resolution and output scale; the approved baseline. |
| Procedure | Compare candidate with baseline. Count the actual raster width of critical lines. Note if they collapse, alias or vanish. |
| Record | Device resolution; output scale; each critical line's pixel width; outcome (holds / aliases / collapses / disappears). |
| Pass | Against an explicit project criterion only; else unassessed. Not a universal two-pixel minimum (AP:485). |
| Never proves | Meaning of the cue. Pair with grayscale, CVD simulation, and shape/location/timing/user checks. |
| Tag / Src | OPINION O00 on EXPERIENCE R08 (2018-02-20). AP:483, 485. |

### 5.4 Threshold scopes (do not mix)

| ID | AP | Threshold | Exact scope | Not | Tag | Src, date |
| --- | --- | --- | --- | --- | --- | --- |
| TH1 | 559 | 4.5:1 | WCAG 2.2 SC 1.4.3: ordinary text and images of text. | A Roblox game-world rule. Excludes inactive-component text and logotypes (among other cases). | VERIFIED | A04, undated, accessed 2026-10-21 |
| TH2 | 559 | 3:1 | WCAG 2.2 SC 1.4.3: large-scale text. Explanation uses 18 point regular or 14 point bold. | A Roblox pixel-size rule. | VERIFIED | A04 |
| TH3 | 559 | Rounding rule | Do not round a failing computed ratio upward. | - | VERIFIED | A04 |
| TH4 | 559 | 3:1 | WCAG 2.2 SC 1.4.11: against adjacent colors, for visual information needed to identify UI components/states and required parts of graphics, with stated exceptions. | Every prop or enemy pixel. | VERIFIED | A05, undated, accessed 2026-10-21 |
| TH5 | 561 | 4.5:1 | Xbox game guideline: standard-size text and important visual elements. | Roblox requirement. | VERIFIED | A07, undated, accessed 2026-10-21 |
| TH6 | 561 | 3:1 | Xbox: large-scale text and elements; inactive text. | - | VERIFIED | A07 |
| TH7 | 561 | 7:1 | Xbox: high-contrast-mode UI. | - | VERIFIED | A07 |
| TH8 | 561 | 36 px at 100 DPI; 72 px at 200 DPI; 144 px at 400 DPI | Xbox mobile large-text examples. | Roblox requirement. | VERIFIED | A07 |
| TH9 | 561 | measure over the lowest-contrast background area | Xbox advice for text over variable backgrounds. | - | VERIFIED | A07 |
| TH10 | 561 | 4.5:1 | Game Accessibility Guidelines: text and UI contrast; notes mobile sunlight and poor displays as relevant contexts. | Primary standard (tagged EXPERIENCE, a guideline site). | EXPERIENCE | A09, undated, accessed 2026-10-21 |

Paper table AP:593-599: WCAG ordinary and large text ratios have scope (4.5:1 and 3:1; VERIFIED; A04, undated, accessed 2026-10-21) / Xbox guidance differs for some roles (inactive text 3:1; high-contrast UI 7:1; VERIFIED; A07, undated, accessed 2026-10-21) / palette extraction is diagnostic (no universal palette size or DeltaE tolerance; OPINION; O00, 2026-10-21).

## 6. Review order that follows from the paper (extractor's assembly, each step from the rows cited)

| Step | Action | Rows |
| --- | --- | --- |
| 1 | Name the player's decision and the relevant roles for this moment. | RD13, RD14, HI1 |
| 2 | Match capture conditions to the anchor (camera, lighting, exposure, device, render mode). | BF2, BF5, LK5, LK10, D9 |
| 3 | Compare layers: no UI, no effects, full. | HI3 |
| 4 | Run value (M1, M2), contrast (M3), role color (M4, M5), CVD (M6). | section 5.3 |
| 5 | Run silhouette and thumbnail at presentation size (M7, M8), raster width (M14). | section 5.3 |
| 6 | Run clutter and hierarchy diagnostics (M11, M12) and the timeline (M13). | section 5.3 |
| 7 | Run recognition test (M9); AI screening flags uncertainty only. | RD11, RD12 |
| 8 | Test at the lowest supported quality and on real hardware. | HI7, RD16, RD17 |
| 9 | Write feedback in the F1 record; owner decides on conflicts and new directions. | F1, LK10, D12 |

## 7. Number register (AP:359-602)

"undated, accessed D" = living page, no publication date. "not stated" = paper gives no unit or detail.

| ID | Value | Unit / meaning | AP | Src, date | Tag |
| --- | --- | --- | --- | --- | --- |
| N01 | 3 | theme pillars, Little Demon Tristana | 379 | R09, 2019-05-15 | EXPERIENCE |
| N02 | 8-10 | chroma designs before selection (generally); not whole-game directions | 379, 393 | R09, 2019-05-15 | EXPERIENCE |
| N03 | 4-6 | weeks, reported splash duration | 379 | R09, 2019-05-15 | EXPERIENCE |
| N04 | daily; 1-2 per week | team review cadence; this illustrator's feedback requests | 379, 395 | R09, 2019-05-15 | EXPERIENCE |
| N05 | 75-100 | hours, estimated splash (2018 account) | 381 | R10, 2018-07-26 | EXPERIENCE |
| N06 | 4 | weeks, average schedule including other duties | 381 | R10, 2018-07-26 | EXPERIENCE |
| N07 | 4 goals, 5 areas | League VFX guide structure | 477, 463 | R06, 2017-10-25 | EXPERIENCE |
| N08 | 1 or less | pixels, Illaoi fine lines that turned jagged | 483, 503 | R08, 2018-02-20 | EXPERIENCE |
| N09 | 144 FPS; 6.9 ms | VALORANT 2020 historical target and source-stated approximation (not exact reciprocal) | 525, 535 | R13, 2020-06-30 | EXPERIENCE |
| N10 | 0.04045; 12.92; 1.055; 0.055; 2.4 | sRGB linearization constants | 551 | A06, undated, accessed 2026-10-21 | VERIFIED |
| N11 | 0.2126 / 0.7152 / 0.0722 | R / G / B luminance weights | 551 | A06 | VERIFIED |
| N12 | 255 | divisor for 8-bit channels | 551 | A06 | VERIFIED |
| N13 | 0.03928 | older switch point, corrected May 2021 | 551 | A06 | VERIFIED |
| N14 | 0.05 | offset in the contrast ratio | 563 | O00 over A04 | OPINION (procedure) |
| N15 | 4.5:1 / 3:1 | WCAG 1.4.3 ordinary / large text | 559 | A04 | VERIFIED |
| N16 | 18 pt regular; 14 pt bold | large-text explanation (not a Roblox pixel rule) | 559 | A04 | VERIFIED |
| N17 | 3:1 | WCAG 1.4.11 non-text | 559 | A05 | VERIFIED |
| N18 | 4.5:1 / 3:1 / 3:1 / 7:1 | Xbox standard / large / inactive text / high-contrast UI | 561, 597 | A07 | VERIFIED |
| N19 | 36 px at 100 DPI; 72 px at 200 DPI; 144 px at 400 DPI | Xbox mobile large-text examples | 561 | A07 | VERIFIED |
| N20 | 4.5:1 | Game Accessibility Guidelines text/UI | 561 | A09 | EXPERIENCE |
| N21 | 250 ms | reliable color/motion detection, controlled 3D scene study | 583 | A14, 2026-05-13 | VERIFIED |
| N22 | 22 participants; 11 shared | preference experiment size; overlap with first experiment | 583 | A14, 2026-05-13 | VERIFIED |
| N23 | v1.3, 2018-05-05; site 2020-01-02 | Color Oracle | 573 | A10 | VERIFIED |
| N24 | 0.26.0 / 4.12.0 | scikit-image / OpenCV doc versions | 569, 587 | A11 / A12 | VERIFIED |
| N25 | not established | page count of a good bible; number of directions, mood-board images, review rounds; palette size; DeltaE tolerance; silhouette percentage; exposure time; participant count; pass percentage; universal two-pixel line minimum; screen size | 367, 403, 485, 507, 543, 577, 581, 599 | O00 | OPINION-unresolved |

## 8. Lessons as one-line rules for the skill writer

| ID | Rule | Rows |
| --- | --- | --- |
| L1 | Every lock = purpose, scope, approved example, contrasting failure, test. | RD3, RD4 |
| L2 | An empty bible field is an open decision; ask, never fill. | BF-p3 |
| L3 | Only current approved anchors bind; each anchor states what it controls. | BF5, LK8 |
| L4 | Compare under matched camera, light, exposure; disclose any difference. | D9, LK10 |
| L5 | Authored color, rendered color, sampled color are three records. | SH4 |
| L6 | Measure local (object vs its background), not only global. | SH3, M2 |
| L7 | Say which conversion and which standard; do not mix. | M1, M3 |
| L8 | No cutoff the paper did not set; report diagnostic or unassessed. | RD8, M2, N25 |
| L9 | Critical cues need a second channel beyond color. | M4, M6 |
| L10 | Test at presentation size, at lowest quality, on real hardware. | M7, M8, HI7, RD16 |
| L11 | Layer cuts and a timeline, not a single beauty frame. | HI3, M13 |
| L12 | A model's confident label is a flag, not evidence. | RD12, M9 |

## 9. Source IDs used in lines 359-602 (resolved from AP:1013-1695)

| Id | Source | Date as shown | Tag | AP register line |
| --- | --- | --- | --- | --- |
| O00 | This paper's own recommendations, interpretations, fictional examples. "Not an external study." | 2026-10-21 | OPINION | 1015 |
| R04 | Defining the Rifts Visual Style (Riot, mobafire reprint). Quote: "It should clarify game space, not clutter it." | reprint 2014-11-11 | EXPERIENCE | 1129 |
| R06 | League VFX Style Guide announcement (Riot) | 2017-10-25 | EXPERIENCE | 1145 |
| R07 | Official League VFX Style Guide release thread (realtimevfx) | 2017-10-26 | EXPERIENCE | 1153 |
| R08 | Resistance Illaoi The Final Update (Riot) | 2018-02-20 | EXPERIENCE | 1161 |
| R09 | Little Demon Tristana Splash Art and Chromas (Riot) | 2019-05-15 | EXPERIENCE | 1169 |
| R10 | New Champions (Riot) | 2018-07-26 | EXPERIENCE | 1177 |
| R11 | Before There's Splash Art There's Feeney Art (Riot) | 2017-02-17 | EXPERIENCE | 1185 |
| R12 | The Art of VALORANT Map Environments (Riot) | 2020-11-16 | EXPERIENCE | 1193 |
| R13 | VALORANT Shaders and Gameplay Clarity (Riot). Quote: "performance, competitive integrity, and art" | 2020-06-30 | EXPERIENCE | 1201 |
| A04 | W3C, Understanding SC 1.4.3 Contrast Minimum | undated live WCAG 2.2 explanation, accessed 2026-10-21 | VERIFIED | 1401 |
| A05 | W3C, Understanding SC 1.4.11 Non-text Contrast | undated live, accessed 2026-10-21 | VERIFIED | 1409 |
| A06 | W3C, relative luminance definition | undated; threshold corrected May 2021; accessed 2026-10-21 | VERIFIED | 1417 |
| A07 | Microsoft, Xbox Accessibility Guideline 102 Contrast | undated live, accessed 2026-10-21 | VERIFIED | 1425 |
| A08 | Microsoft, Xbox Accessibility Guideline 103 Additional channels for cues | undated live, accessed 2026-10-21 | VERIFIED | 1433 |
| A09 | Game Accessibility Guidelines, high contrast text/UI | undated live, accessed 2026-10-21 | EXPERIENCE | 1441 |
| A10 | Color Oracle | v1.3 released 2018-05-05; site updated 2020-01-02; accessed 2026-10-21 | VERIFIED | 1449 |
| A11 | scikit-image color API | 0.26.0 docs; undated page; accessed 2026-10-21 | VERIFIED | 1457 |
| A12 | OpenCV Canny Edge Detection | 4.12.0 docs; undated page; accessed 2026-10-21 | VERIFIED | 1465 |
| A14 | Preattentive Features in 3D Games: Detection Accuracy and Player Preference (Springer) | 2026-05-13 | VERIFIED | 1481 |
| P03 | Roblox Creator Hub, Test on hardware. Quote: "emulation can't fully replicate what happens on real hardware" | undated living docs, accessed 2026-10-21 | VERIFIED | 1529 |
| P05 | Roblox Creator Hub, Implement designs in Studio. Key line: "select Actual Resolution" | undated living docs, accessed 2026-10-21 | VERIFIED | 1545 |

## 10. Claims for the fact-check

Kinds: studio / standard / tool / roblox / study. Tag is the paper's. Fact-check should confirm the claim matches the source, and that the source date is right.

| ID | Claim | AP | Src | Source date | Why it matters |
| --- | --- | --- | --- | --- | --- |
| C01 | Tristana report: three theme pillars, generally 8-10 chroma designs, splash 4-6 weeks, daily team review, artist asks for feedback once or twice weekly | 379 | R09 | 2019-05-15 | Anchors "no quota" advice; wrong numbers would be repeated as norms. |
| C02 | Splash resolved composition, lighting, anatomy, values in a thumbnail before greenlighting detailed render | 379 | R09 | 2019-05-15 | Basis for the thumbnail-first step. |
| C03 | 2018 account: splash 75-100 hours, average four-week schedule; internal illustrators direct outsourced artists and paint over | 381 | R10 | 2018-07-26 | Staffing context; must not become an AI time estimate. |
| C04 | League VFX guide announcement: four goals (gameplay clarity, reduced clutter, champion theme, player delight), five areas (gameplay, value, color, shape, timing), months of revision | 477, 463 | R06 | 2017-10-25 | Basis for the lock structure; names must match. |
| C05 | R06 and R07 establish provenance; legacy PDF redirected, not read | 477 | R06, R07 | 2017-10-25 / 2017-10-26 | Sets how far the guide may be cited. |
| C06 | Illaoi report: busy indicator, opacity change made dodging easier, lines of one pixel or less jagged, explosions reduced, oil spills removed | 483 | R08 | 2018-02-20 | Source of the raster-width check. |
| C07 | Illaoi report: red projectile vs green terrain failed colorblind tests; luminous yellow core and tip contrast improved focus; Photoshop colorblind filters and colorblind staff feedback | 483 | R08 | 2018-02-20 | Basis for CVD plus redundant-cue advice. |
| C08 | Feeney art: crude placeholder splashes as a quick check of personality and distinctness; Taliyah exposed a weak silhouette | 489 | R11 | 2017-02-17 | Basis for the ablation test. |
| C09 | Phone emulation cannot fully replicate real hardware; Studio "Actual Resolution" option (P05) | 507, 499 | P03, P05 | undated, accessed 2026-10-21 | Gates any "readable on phone" claim. |
| C10 | Icebox account: team set-up, high-level then local concepts, critical geometry preserved, avoid excess contrast/darkness for character reads, decorative detail above player height, callout-friendly locations | 523 | R12 | 2020-11-16 | Studio claims used for hierarchy guidance; must not be over-read. |
| C11 | 2020 shader account: quality-level parity, artist-controlled light-response gradients, no dynamic shadows in playable spaces at that time, 144 FPS and 6.9 ms figures | 525, 535 | R13 | 2020-06-30 | The numbers must never be adopted for Roblox. |
| C12 | Riot's historical Rift hierarchy is contextual (environment, champions, VFX, restrained UI) | 531 | R04 | reprint 2014-11-11 | Paper gives only a table row; check the source supports the order. |
| C13 | sRGB linearization: c/12.92 if c <= 0.04045, else ((c + 0.055)/1.055)^2.4; 8-bit divided by 255; threshold 0.03928 corrected May 2021 | 551 | A06 | undated, accessed 2026-10-21 | Becomes code; one wrong digit breaks every contrast number. |
| C14 | Relative luminance L = 0.2126R + 0.7152G + 0.0722B | 551 | A06 | undated | Becomes code. |
| C15 | WCAG 1.4.3: 4.5:1 text, 3:1 large text; excludes inactive text and logotypes; large = 18 pt regular or 14 pt bold; no rounding up | 559 | A04 | undated | Threshold scope table TH1-TH3. |
| C16 | WCAG 1.4.11: 3:1 against adjacent colors for UI components/states and required graphic parts | 559 | A05 | undated | TH4. |
| C17 | Xbox: 4.5:1 standard text and important visual elements; 3:1 large; 3:1 inactive text; 7:1 high-contrast-mode UI; mobile large text 36 px at 100 DPI, 72 px at 200 DPI, 144 px at 400 DPI; measure against the lowest-contrast background area | 561 | A07 | undated | TH5-TH9. |
| C18 | Game Accessibility Guidelines recommend adapting 4.5:1 and note mobile sunlight and poor displays | 561 | A09 | undated | TH10; tagged EXPERIENCE though it is a guideline site. |
| C19 | Xbox guideline: key cues use additional sensory or visual channels instead of color or audio alone | 567 | A08 | undated | Basis for redundant-cue rule. |
| C20 | scikit-image provides sRGB-to-Lab and CIEDE2000 | 569 | A11 | 0.26.0 docs, undated | Names the library for FM7. |
| C21 | Color Oracle: free full-screen color-vision simulator for Windows, Mac, Linux; v1.3 released 2018-05-05; site updated 2020-01-02 | 573 | A10 | 2018-05-05 / 2020-01-02 | Tool choice; compatibility untested. |
| C22 | A controlled 3D-scene study: color and motion reliably detected within 250 ms, shape weaker; 22 participants (11 shared); motion always before color; authors' stated cautions | 583 | A14 | 2026-05-13 | Easy to over-read into a duration rule. |
| C23 | OpenCV Canny uses threshold parameters to build an edge map | 587 | A12 | 4.12.0 docs, undated | Basis for FM5. |
| C24 | Paper's reading that R12 "decorative detail above player height" and R13 "no dynamic shadows" apply as studio facts of that time only | 523, 525 | R12, R13 | 2020 | Keeps studio practice from becoming law. |

## 11. Contradictions and limits

| ID | AP | Item | Handling in skills |
| --- | --- | --- | --- |
| X01 | 367, 403, 485, 507, 543, 577, 581, 599 | The paper states, repeatedly, that it found no defensible universal number for: candidates, mood-board images, review rounds, bible page count, palette size, DeltaE tolerance, silhouette fraction or percentage, IoU target, exposure time, participant count, pass percentage, line-width minimum, phone screen size. | Never state any as a rule. Leave project cells blank or "decide with owner". Measurements stay diagnostic. |
| X02 | 553 | If no numeric acceptance range is set, a measurement is diagnostic; the agent asks for a project decision. | Output `unassessed` or `diagnostic`, never an invented pass. |
| X03 | 551 | One paragraph mixes VERIFIED (A06 formula) and OPINION (usage rules). | Cite the tag per sentence: formula VERIFIED, rules OPINION. |
| X04 | 545, 551 | "Value structure" and "WCAG luminance" are different. The paper names no representation for artistic value. | Record the conversion; do not name one on the paper's behalf. |
| X05 | 559-561 | WCAG, Xbox and GAG numbers differ in scope (web, console, guideline). A09 is tagged EXPERIENCE. | Pick one standard per UI role and mode and write it down (M3). Never apply to world props by default. |
| X06 | 477 | R06 text: the legacy PDF was not read; counts of goals and areas come from the announcement only. | Cite only the announcement and thread. |
| X07 | 479 | The "uncluttered outer contour" rule is the paper's own example. | Never attribute it to Riot. |
| X08 | 531 | R04 is cited only as a table row. The body does not explain the order of environment, champions, VFX and UI. | Use as a one-line context note only. |
| X09 | 499, 507 | P05 is cited with P03 but the paper does not explain what P05 shows beyond its key line. | Fact-check P05 before relying on it. |
| X10 | 525 | 144 FPS and 6.9 ms are historical and not exact reciprocals. | Never copy to Roblox budgets. |
| X11 | 583 | A14 is one study with 22 participants, motion always before color, uniform scenes, display conditions not fully controlled. | Test design cue only; no duration or color rule. |
| X12 | 491, 581 | A model's label is not a human recognition rate. | AI pass is screening; flag ambiguity. |
| X13 | 519, 513 | Calm space is a resource, yet richness can be right; the focus is not always the brightest object. | Judge by the current task, not by a "less is more" rule. |
| X14 | 389, 487 | Safeguards on paintovers and the AI ablation test are proposals, not measured Riot methods. | Mark as proposal. |
| X15 | 439, 459 | Lantern Workshop is fictional and untested. | Never cite as evidence; use as a writing pattern. |
| X16 | 573 | Color Oracle is old (2018 release); current compatibility not tested. | Test the simulator before relying on it. |
| X17 | 379, 381 | Riot schedules (4-6 weeks, 75-100 hours) are human, historical, include other duties. | Not an AI estimate. |
| X18 | 17 (context, outside range) | The paper itself ran no scene, image, device or player test. All procedures here are instructions, not results. | Mark all checks to-do until this studio runs them. |

## 12. Coverage map

| Paper part | Where |
| --- | --- |
| §2 concept to visual direction + exploration + feedback + table AP:391-397 | sections 1.1-1.4 |
| §3 art bible principles, template (all 12 fields), fictional example (10 locks), table AP:461-467 | sections 2.1-2.3 |
| §4 guide structure, Illaoi, Feeney art, task review, phone review, table AP:501-507 | sections 3.1-3.4 |
| §5 hierarchy, VALORANT (R12, R13), table AP:529-535 | section 4 |
| §6 shape, palette, value, grayscale, contrast thresholds, color semantics, palette extraction, silhouette and small screen, clutter, table AP:593-599 | section 5 |
| Numbers with scope | section 7 |
| Claims for the fact-check | section 10 |
| Contradictions and limits | section 11 |
