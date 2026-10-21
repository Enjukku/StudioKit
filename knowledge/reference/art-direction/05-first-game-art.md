---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J009-T05, DestructionSimulator art sources (read-only)"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# First-game art experience: the first art director, art-fundamentals, the art bible and the owner's rulings (kit-neutral lessons)

The first game (a stylized destruction game with a themed stage list and a story cast) is the owner's only hands-on evidence about art direction. Its sources: one art-director agent (2026-10-15), one art-fundamentals skill built from owner-supplied Riot Games transcripts, one art bible, one UI style note, three anchor images and about 60 art-related ledger rows. Lesson columns are kit-neutral. Game names, piece terms and stage names appear only in source columns, in the owner's verbatim words, and in section 6. Quotes are at most 15 words. Evidence labels: gate-verified = none here; every row below was read from the source files; "owner-confirmed" means the ledger row carries the owner's words.

Marks used in every table: **U** = universal; **UC** = universal with care (the condition is written in the row); **X** = game-specific (drop).

## 1. The first art-director role (agent file written 2026-10-15)

| id | facet | what the first agent had | lesson for the new agent | mark | source |
| --- | --- | --- | --- | --- | --- |
| AD01 | Why it existed | Owner saw no specialist for cohesion across art, UI, VFX, sound and motion. Asked for "Do we make the player's eyes go to the correct location?" and a check of "our sounds, our motion, our art, our UI in cohesion" | The role is a cross-craft cohesion reviewer, not a maker. Two standing questions: where do the eye and ear go first, and do all parts follow the same rules for meaning and style | U | D-281; `.claude/agents/art-director.md` |
| AD02 | Set-up | Opus, effort medium, tools Read/Grep/Glob/Write/Bash, one skill (art-fundamentals), writes only into a folder the brief names (default `output/art-direction/<slug>/`) | Review-only scope is right. Effort medium was set to save usage; for "no mistakes" work the kit pins high (see GP10) | UC: scope U, effort X | agent file lines 1-9 |
| AD03 | Method (6 steps) | (1) restate the moment: what the player does, the 1-2 things to notice first, emotion, device (phone first), camera; (2) read style sources (bible, taste table, UI style, specialist cards); (3) look at every named image, run squint (25 %) and greyscale tests with Python/Pillow, save the test images beside the report; (4) review with the checklist and cohesion table, each finding with evidence (image region, file path, card id); (5) rank by clarity first, then satisfaction, then style; propose the smallest fix and name who makes it; (6) list what a still cannot show | Keep the order. "Restate the brief first" and "every finding cites evidence" are the two habits that make a review checkable. Replace the ad hoc Pillow code with the measuring tool (look_check) | U | agent file, Work method 1-6 |
| AD04 | Output format | About 600 words plus files: verdict in one line; ranked findings table (problem, evidence, player impact, fix, owner of the fix); cohesion table (colour, shape, motion, sound meaning: consistent or not); files written; what works (keep it); could not check; proposals labelled PROPOSAL | Good shape. "What works (keep it)" protects owner-liked looks from a fix-everything pass. Add status line and per-item done / not done (kit messages rule) | U | agent file, Return |
| AD05 | What it could check | Stills: screenshots, renders, concept sheets, UI mock-ups; specialist cards (effect, cue, animation) read as text | Stills judge hierarchy, silhouette, scale, palette, completeness, consistency of look | U | agent file step 3-4 |
| AD06 | What it could not check | Sound (no listening), motion (no video), live Studio state. It had to name the captures it needed and ask the Studio operator | Say this in every report. Judge motion from frame sequences or reference clips at phone size, sound from cue cards plus a listening request. Never certify what was not seen or heard | U | agent file step 6 |
| AD07 | Fix routing | Findings named the specialist who fixes (content builder, UI, VFX, sound, animator) and never edited their files | Keep: the reviewer proposes, the owner of the craft fixes, nobody edits another craft's output | U | agent file |
| AD08 | Evidence of use | No art-director report exists anywhere in the game's `knowledge/` or `output/` (grep, 2026-10-21). The improve log of 2026-10-15 says "No agent has run yet" | The first art director is an untested draft. Treat its method as a starting hypothesis, not as proven practice | U | `knowledge/logs/improve/2026-10-15.md` "Not verified" |
| AD09 | Overlap | The rulebook already had a 5-angle self-review (front, side, back, high 3/4, player eye; checks: direction of directional pieces, floating or hidden pieces, scale against a player, match to concept art) | That self-review is geometry and match-to-reference. An art director must add what it cannot see: readability, completeness, mood, cohesion (section 5) | U | game `AGENTS.md` section 2.4 |
| AD10 | Taste memory | The only taste memory was a small "Taste" table in the owner profile: area / what the owner wants / what the owner rejected (world, UI, gear ideas, gear art, physics, debris) | The three-column table is the right shape and was read first by builders. It mixed art with physics and had no dates or owner quotes; keep it per game, dated, with the owner's words | UC: format U, content X | `rules/owner-profile.md` Taste |

## 2. art-fundamentals as checks (source: Riot Games "So You Wanna Make Games??" ep. 1-4 unless marked)

The skill (2026-10-15) paraphrases owner-supplied transcripts. Ledger mapping: ep. 1 game-art intro -> sections 1-2; ep. 2 concept art -> section 6; ep. 3 character art -> section 3; ep. 4 environment art -> sections 4 and 6. Sections 5 and 7 are the orchestrator's synthesis, not one transcript. Ep. 5-10 landed in other skills. The `references/expert-workflows.md` file stayed an empty table (header only): the planned long expert talks were never ingested. Nothing in the skill has a number, a tolerance or an example from the game.

| id | check | origin | mark | condition |
| --- | --- | --- | --- | --- |
| AF01 | Three jobs of game art: clarity (what is a threat, goal, mine, breakable), satisfaction (every action answered in the same frame), style (one look that sets the emotion). Style is a tool for emotion, not decoration | Riot ep.1 | U | |
| AF02 | Rank what is on screen for this moment; only the top 1-2 items get high contrast | Riot ep.1 | U | |
| AF03 | To make one thing stand out, lower the contrast of everything else, not only raise the target | Riot ep.1 | U | |
| AF04 | Contrast channels, strongest first: value, saturation, hue, shape, size, detail density, motion, timing. Critical items use more than one channel (colour alone fails colour-blind players and phones in sunlight) | Riot ep.1 | UC | order is a heuristic from the transcript, not measured; check it with a greyscale pass |
| AF05 | Detail is a contrast channel: alternate calm areas with busy areas; detail everywhere means focus nowhere | Riot ep.1, ep.4 | U | |
| AF06 | Distance reads simpler: less detail, contrast and saturation far away | Riot ep.1 | UC | flat or high-contrast stylized looks may deliberately skip depth fade; follow the bible |
| AF07 | Light is a pointer: a bright spot draws the eye, a dark area hides | Riot ep.4 | U | |
| AF08 | Shapes point and mean: spikes read danger, round reads friendly, squares stable | Riot ep.1 | UC | cultural and style dependent; fix the shape language in the bible, then enforce it |
| AF09 | If every element is loud, nothing is loud: save the biggest, brightest, longest effect, sound and motion for the biggest moment | Riot ep.1 | U | |
| AF10 | Squint test: shrink to about 25 % and view in greyscale; the top-ranked item must still win | Riot ep.1 | UC | 25 % is a rule of thumb; test at the real slot or phone size (the look_check tool does this) |
| AF11 | Choose the 2-3 iconic elements that make a thing recognisable; when small, simplify down to them and push them | Riot ep.3 | U | |
| AF12 | Check silhouette as a solid shape at the real camera distance and angle; two different things must not share one | Riot ep.3 | U | |
| AF13 | Size ranks importance | Riot ep.3 | UC | scale can be fixed by design (boss size); check it against the intended rank |
| AF14 | Proxy first: big blocks of shape and colour, check proportion and silhouette in the game, then add detail | Riot ep.3 | U | |
| AF15 | A design that looks good in a neutral pose can fail in motion; test extreme poses before polish | Riot ep.3 | U | |
| AF16 | Scale cues are what the player touches (doors, handles, stairs, rails, chairs); build next to a player-sized reference | Riot ep.4 | U | |
| AF17 | Story in the space: leftovers of use, wear where hands and feet go, dirt in low corners | Riot ep.4 | U | |
| AF18 | Modular kits: pieces that look different when rotated, mirrored, scaled or recoloured, yet generic enough not to read as copies | Riot ep.4 | U | |
| AF19 | Art and rules must agree: soft-looking things must not stop a truck; weak-looking materials break easily | Riot ep.4 | U | |
| AF20 | Cohesion table: colour meaning, shape meaning, motion personality, sound personality and loudness, material and age language must match across world, VFX, UI, icons, animation, audio | synthesis (ep.1, ep.6-8 ideas) | U | |
| AF21 | Feedback habits: show proxies early, no grand reveals; ask goal questions ("which feels heaviest?") not taste questions; find the problem behind a proposed fix; work broad to narrow and do not reopen a closed direction without new evidence | Riot ep.2, ep.4 | U | |
| AF22 | Review checklist of 8 items: top items win squint and greyscale; calm areas exist; silhouette and iconic traits read at game distance on a phone; player-sized reference present; story of use; meanings match the rest; looks match behaviour; nothing important signalled by colour alone | synthesis | U | all 8 are yes/no by eye; none is measured |

## 3. Art-bible practice

The bible (2026-09-30) is one file with 4 visual pillars, 14 fenced "lock" blocks (prompt text for the image tool), palette rules per stage (dominant, secondary, accent) and an audio and VFX direction table. A script reads the lock blocks, so each lock exists exactly once. It carried the status PROPOSAL from the first day and never changed. Decisions that changed looks were written in the decision ledger, not in the bible.

| id | what happened | lesson | mark | source |
| --- | --- | --- | --- | --- |
| AB01 | Lock structure: one fenced block per image family (world, structure, creature, character, model reference, style test, prop, layout, UI kit, UI screen, icon, effect sheet, effect storyboard, print texture), first words `<NAME> LOCK:`. The tool assembled every prompt as identity + family lock + world lock | One source for style text, machine-read, assembled by a tool: worked. Style never lived in agents' memories | U | art-bible.md; `tools/art/art_refs.py` |
| AB02 | Each lock names forbidden things (no text, no logos, no watermark, no brand names, plain background) and cut-out colour (magenta where transparency is impossible) | Put the exclusions in the lock, not in each brief | U | art-bible.md locks |
| AB03 | The look held where the owner decided it after seeing it: one seam rule after a hands-on test (a thin gap looked best close up but shimmered in motion), plastic look with real-material behaviour, hand-painted 3D character style picked from four test styles, default engine lighting and shadows | Locks that survived were chosen by the owner from rendered alternatives or measured in motion, not by argument | U | D-047, F-014, D-090, D-155, D-139 |
| AB04 | Drift 1: the UI locks (glossy cartoon: sheen band, gradients, thick outline) stayed in the bible while the UI note moved twice (chunky cartoon, then matte rendered pieces with "no glossy candy sheen", then built in a 3D tool). The UI anchor image still shows the glossy style the owner had left | When a direction is superseded, change the lock, the anchor and the note in the same edit. A drift check (lock vs latest decision vs anchor) is a standing art-director duty | U | art-bible.md UI KIT/UI SCREEN LOCK vs ui-style.md "Direction lock v2"; D-129; anchors/uiscreen |
| AB05 | Drift 2: the character-lock text says clean T-pose; a note right under it says T-pose and chaining made characters drift and to use a relaxed A-pose. A one-off style-test lock stayed in the bible. Two character locks (soft painterly sheet style vs hand-painted 3D style) coexisted | Retire test locks after the test. One live lock per family. A rule found later must edit the lock text, not sit beside it | U | art-bible.md MODEL REF LOCK + note; CHARACTER LOCK; STYLE TEST LOCK; D-150, D-155 |
| AB06 | Drift 3: palette rules covered 4 of 14 stages; later stages had their look only in concept images and stage notes | A bible needs a rule for how each new environment gets its palette (one dominant, one secondary, one accent) and where it is recorded | U | art-bible.md Palette rules |
| AB07 | Drift 4: the bible's effect budget (3 emitters and 64 particles per blast) was later challenged by the owner, who asked why a similar emitter rule said 5 when professionals use far more; the budget moved to measured practitioner sources | Technical budgets belong in the craft skill with measured sources, not in the art bible | UC: art numbers X, rule U | art-bible.md Audio & VFX; D-286 ("if the pros are doing it this way, I'm sure it'll be fine") |
| AB08 | Anchors: three files only, one per family (character sheet, three-character style lineup, shop panel). Files starting `gen-` are agent-generated and approved by a command; owner-supplied files have no prefix and come first. At most 3 anchors attach to any generation; a row may name which. Anchors steer proportions, palette and vocabulary; the lock sets the style | Few, named, approved anchors beat many. Keep the owner's own references separate from the agents' own output | U | art_refs.py (`MAX_ANCHORS`, `gen-` prefix, `approve`); content/art/anchors/ |
| AB09 | Anchor gaps: no anchor for structures, though most work was structures; those relied on the lock plus attached real photos. The character anchor was marked by the owner as a design reference, "not the final art style" | An anchor must say what it fixes (shape, palette, proportion, render style) and what it does not | U | D-150; anchors/ listing |
| AB10 | Style test: one cast rendered in four candidate styles (vinyl toy, clay, outlined toon, hand-painted) on one page; owner picked one in one sentence; the winner became a lock | The cheapest way to lock a style: same subjects, same pose, 3-4 styles, one page | U | D-155; refs/styletest/ |
| AB11 | Reference pipeline that worked: real photos first for real subjects; a generated hero view per subject next; other views from the approved hero; contact sheets for review; rejected sheets kept in a `_rejected` folder with their prompt JSON; a required-views list (two opposite 3/4 views, four sides, top, a plan per floor, one interior per room, a cutaway) and a minimum of 15 consistent concept images per environment | Numeric coverage lists make "enough references" checkable. Keep rejects with prompts so a dead style is not retried | U | D-025, D-072, D-163, D-164; refs/_rejected |
| AB12 | Owner UI references (six third-party screenshots) were kept local-only, never attached to prompts, each with a "what to learn" row | Keep inspiration separate from generation inputs; extract rules, not images | UC: also a copyright rule | references/ui-toybrick-party/README.md |
| AB13 | Image-to-3D references: exactly one character, one angle that shows everything (three-quarter, 40 degrees), one pose; extra angles made the tool build extra models; chaining from an earlier model reference made characters drift | Pass the approved design sheet each time; never chain generations | UC: tool-specific (Tripo) but the "one subject, one view" rule is U | D-153; art-bible.md note |

## 4. Owner art rulings as universal lessons (owner's words verbatim, at most 15 words)

The quote column is verbatim and may carry game words. The lesson column is neutral.

| id | lesson | owner's words | mark | source |
| --- | --- | --- | --- | --- |
| OR01 | One consistent rule beats a menu of per-case options; the owner withdrew a "both looks" option within a day | "let's just stay consistent" | U | D-046, D-047 |
| OR02 | Judge looks in motion and from the player camera, not only in stills; a finish that is best still can flicker when moving | "I prefer the seamless ones" (after a hands-on look test) | U | D-045, D-047, F-014 |
| OR03 | Show 2-3 renders of the same subject from the same camera; the owner chooses by looking | "I like the top row second image." | U | D-076 |
| OR04 | Size variety inside a surface (big mass pieces plus small detail pieces) reads better than one size | "it would be kind of nice if we had some smaller bricks too" | UC: the mix is a style choice | D-068, D-049 |
| OR05 | Build at player scale or slightly above; small "miniature" builds are rejected; plan with a blueprint (floor plans, furniture, player silhouette) before building | "it's almost like you're making a miniature on purpose" | U | D-091, F-012 |
| OR06 | Review order: blueprint, then offline render beside the concept sheet, then engine placement; the owner approves each step before the next | "you might have to start doing it like blueprint style" | U | D-091; owner-profile "Review order" |
| OR07 | Ground has relief, but every change in level blends in (slopes, stairs); sudden steps and mismatched grass heights look like errors | "it should just be blended in smoothly" | U | D-143, D-146, D-106 |
| OR08 | Every environment gets its own light mood; a first level should read bright and cheerful, not dim | "the lighting is a little bit dim" | UC: mood target is the game's | D-126 |
| OR09 | Use the engine's own lighting and shadow settings; do not invent custom systems; measure cost before cutting | "Why are we like inventing our own stuff?" | U | D-139, F-018 |
| OR10 | Transparent materials must still read as their material at game distance; do not force one tint | "make glass more cartoony, like you can see the glass more" | U | D-086 |
| OR11 | Every face of a building is finished; blank back or side walls look wrong | "all the panels don't have windows, which looks a little bit strange" | U | D-192 |
| OR12 | Overused primitive shapes look odd; use them as accents and merge organic forms (trees) into one coherent silhouette | "the use of all these various like spheres also looks very odd" | U | D-192 |
| OR13 | Every room is fully furnished; exteriors, roofs and streets get decoration too. First plans were under-decorated | "some of the rooms do look under-decorated. Like, the kitchen" | U | D-165, D-016, D-188, D-195 |
| OR14 | Roads and paths must join at proper junctions; no stubs, no gaps | "the roads don't properly connect between each other with intersections" | U | D-168, D-157, D-158 |
| OR15 | For real subjects, real photos are the accuracy source; a generated image is a style hint and is rejected when inaccurate | "I would prioritize our real references" | U | D-164, D-163 |
| OR16 | Parts that are fine alone can still fail together: the cast must share one world look | "the models look fine, but they don't look like they exist in the same world" | U | D-153 |
| OR17 | A cast member must differ by more than colour: own mouth, eyes, nose, brows | "they should all have like a different like mouth feature" | U | D-186 |
| OR18 | A villain's face must be visible and human enough that players dislike the character; state the intended emotion in the brief | "the player should hate this character" | U | D-150, D-151 |
| OR19 | Show a story trait with 2-3 quiet cues (eyes, posture, a hidden accessory); an over-signalled cue was rejected | "You went too hard on the collar" | U | D-152 |
| OR20 | What the owner already likes is locked; test any change side by side and keep it only if it matches | "I really like the way the villain's eyes are set up." | U | D-184 |
| OR21 | Generated UI that is flat and 2D reads as AI-made; the owner moved to lit, rendered assets where highlights and shadows are real | "we seem to struggle creating UI that doesn't look like AI" | UC: the 3D-lit answer is this owner's taste | D-129; owner-profile Taste |
| OR22 | When the owner supplies a reference, match its construction literally first (flat frames, header tile, large tiles); round rims, keycap shapes and rows of small cells were rejected | reference reviews v1-v4, 2026-09-30 (no verbatim quote kept in source) | UC | ui-style.md "Direction lock v2" |
| OR23 | HUD stays out of platform-reserved corners and thumb zones; fewest possible buttons (aim and fire by tapping the screen) | "No FIRE or THROW buttons" (as recorded in the UI note) | UC: layout numbers X, principle U | ui-style.md HUD layout |
| OR24 | Collectibles must read as collectibles, not rubble: a colour that never matches the surroundings, hover, spin, glint. 2D sprites in a 3D world were rejected after a play-test | no verbatim kept for the main rule; a related trim: "we don't need the shadows underneath it" | U | D-053, D-054, D-056, F-015 |
| OR25 | Reward flights need cause and connection: burst with the explosion's velocity, land, then curve in from all directions, one connected 3D-to-2D motion, an impact on arrival, no clutter in screen centre. Five written rounds in one day failed to land it | "the three D effect is very linear" | U | D-138, D-140, D-142, D-144, F-019 |
| OR26 | Effects: look from a reference clip plus a motion blueprint, then real captures; 2D mock-ups were dropped. Camera shake only on some effects. Owner always gives the final look | "not everything should have camera shake. Even explosions" | U | D-283, D-284, D-286 |
| OR27 | Agents apply known standing rules without being told each time (effects are visual only; fake damage is allowed as cosmetic parts) | "I shouldn't have to specify that there's no damage or breaking" | U | D-289, D-290 |
| OR28 | Differentiate environments as a whole, not element by element; do not cut an iconic place only because an earlier one had something similar | "I just want each stage to be different from one another" | U | D-194 |
| OR29 | Spend polish on the focal and repeated things; accept "good enough" elsewhere. A coverage score is a floor, not the finish; polish rounds are welcome | "further polishing rounds is good" | U | D-130, D-125 |
| OR30 | After reference images and plans are approved, builders proceed with self-review against the references and the owner sees results later | "You no longer need my approval." | UC: kit gates decide | D-170, D-164, D-191 |
| OR31 | Describe a look by the origin of its materials: "made from whatever was lying around" gave a coherent rule for a whole prop family | "very scrap like we can see there made by what was lying around" | UC | D-149 |
| OR32 | Copy the recognisable look of a real or famous subject but leave out protected marks: names, logos, lettering, characters. Decide this per project with the platform-policy skill | "no logos or like lettering that could be copyrighted" | UC: legal and platform policy decides | D-017, D-156, D-187, D-194 |

## 5. Reviews: what exists, what they caught, what they missed

No art-director review report was found (grep of the game's `knowledge/` and `output/`; the agent never ran, AD08). The nearest evidence is the agents' own offline and in-engine self-reviews and the owner's corrections after them.

| id | review type | what it caught | what it missed (owner found later) | lesson | source |
| --- | --- | --- | --- | --- | --- |
| RV01 | Offline before/after render set for one large landmark: same cameras for before and after, a plan view marking what stays and goes, a player-eye view, a cut-away section, plus a written self-review (directional pieces, floating pieces by a connectivity check, holes, scale with a player figure) | Direction of pieces, floating pieces, holes, scale, brick counts | Owner called an earlier version boxy; later accepted a simpler one: "it works. Fun." | Before/after at fixed cameras and a plan marked with changes make a review easy to read. Keep the self-review list for geometry | `output/review/day-2026-10-09/mountain-redesign/README.md`; D-125 |
| RV02 | Ground-level audit with before/after pictures and a height map | Level jumps between buildings, grass and terrain | Found only after the owner saw odd steps in play | Add a ground continuity check across the whole site, not per building | `output/review/day-2026-10-10/ground-level/`; D-143 |
| RV03 | Lighting preset comparison: default vs two presets from the same camera | Showed look differences side by side | The preset switch had no effect in play, so values were copied by hand; the owner had already called the light dim | Verify that a switch changed the picture; compare at one camera | `output/review/day-2026-10-09/shadows-lighting/README.md`; D-126 |
| RV04 | Agent-run review of the builders (30 days of runs) | Real owner rejections: scale too small, coarse furniture, facing (lectern, carpet), boxy mountain and cave | These were found by the owner, not by agent review | Scale, furniture density, facing and silhouette shape are the repeat offenders; the art director's checklist must name them | `knowledge/logs/agent-review/2026-10-09.md` |
| RV05 | Owner reviews of stage plans and hero images | Under-decorated rooms, unconnected roads, blank back walls, odd spheres, bad trees, inaccurate generated landmark images | Not caught by the 5-angle self-review: it checks pieces and scale, not completeness or believability | A completeness check against the blueprint (every face, every room, every road end) is the biggest gap | D-165, D-168, D-192, D-164 |

Summary: reviews caught correctness (direction, floating, holes, scale). Owner corrections concerned readability, completeness, consistency across a whole site, mood, and accuracy. None of the five review types measured whether the focal point reads at phone size.

## 6. Drop as game-specific (the lead can grep for these terms)

| id | what to drop | grep terms | mark |
| --- | --- | --- | --- |
| DR01 | Game and tool names, file paths, decision ids | `DestructionSimulator`, `destruction`, `Destrutionnn`, `D-0`, `D-1`, `D-2`, `F-0`, `Q-`, `content/art`, `art_refs`, `icon_studio`, `kit.json`, `rules/owner-profile` | X |
| DR02 | Piece and material vocabulary of the toy look | `brick`, `stud`, `plate`, `wedge`, `2x2`, `ABS`, `running-bond`, `baseplate`, `seamless`, `SmoothPlastic`, `toy`, `Lego`, `interlocking`, `stud grid`, `mixed masonry` | X |
| DR03 | Stage names and themes | `Blockcraft`, `Stage 1` ... `Stage 14`, `Landmarks`, `Dream House`, `Dream Doll House`, `North Pole`, `Titanic`, `Harbor`, `Toy Bedroom`, `Dino Park`, `Pirate Isles`, `Bikini Bottom`, `Animal City`, `Airport`, `Candy Kingdoms`, `Haunted Vampire School`, `Nether`, `End`, `Void Dragon`, `lobby`, `tube` | X |
| DR04 | Franchise and inspiration names | `Minecraft`, `Barbie`, `Santa`, `Toy Story`, `Jurassic`, `One Piece`, `SpongeBob`, `Zootopia`, `Adventure Time`, `Hotel Transylvania`, `Pet Simulator`, `Genshin`, `Fisch`, `Teardown`, `THE FINALS`, `Disney`, `Pixar` | X |
| DR05 | Story cast and gameplay words | `King`, `villain`, `golem`, `companion`, `sorcerer`, `halo`, `furnace`, `DETONATE`, `backpack`, `C4`, `rocket`, `Boom Cube`, `pets`, `eggs`, `Itempedia`, `rarity`, `Secret` | X |
| DR06 | The lock texts themselves (all 14); keep only the structure (name, first words, exclusions, cut-out colour) | `WORLD STYLE LOCK`, `STRUCTURE LOCK`, `CREATURE LOCK`, `UI KIT LOCK`, `ICON LOCK`, `VFX SHEET LOCK`, `PRINT TEXTURE LOCK`, `STYLE TEST LOCK` | X |
| DR07 | UI numbers and colour assignments | outline 4 px, shadow 6 px, radii 8/16/24, overshoot 6 % at 180 ms, press sink 3 px, colour roles gold/green/red/blue/purple, font names. Keep the principle "one outline, one shadow, one radius scale, colour roles" | X numbers, U principle |
| DR08 | Effect budgets from the bible | `3 emitters`, `64 particles`, `emitter count (≤5)` | X (owner rejected) |
| DR09 | Build and scale numbers | `1.5×`, `45 × 60 studs`, `5.2 studs`, `100k`, `125k data bricks` | X |
| DR10 | Process names tied to this repo | `5-angle review`, `brickc`, `Studio MCP` check names, `studio-operator`, `content-builder`, `gui-ui` | UC: the idea is U, the names are not |

## 7. Gaps the new art director should fill

| id | gap in the first agent or its sources | what the new agent needs | source |
| --- | --- | --- | --- |
| GP01 | The first agent never ran; its method is untested | A real first test on a live brief; record what the owner changes | AD08 |
| GP02 | Squint and greyscale tests were ad hoc Pillow code, with one rule of thumb (25 %) | The look_check tool (value, silhouette, palette, thumbnail at the real slot) used as measurement, never as a taste score | AD03, AF10; J009-T06 |
| GP03 | No one owned the art bible: PROPOSAL status for weeks, locks and notes in conflict | Own bible hygiene: one lock per family, drift check against the decision ledger and anchors, retire test locks, palette rule for every new environment | AB04-AB06 |
| GP04 | Anchors were few, unnamed in purpose, one contradicting the latest UI direction | Anchor register: what each anchor fixes, approval date, which lock it serves, a check that it still matches the newest decision | AB04, AB08, AB09 |
| GP05 | Generated reference images were reviewed by eye; real subjects came out inaccurate | A reference-image review: count and place things, compare with real photos side by side, check text, hands, extra limbs, pose; flag inaccurate real subjects | OR15, D-164 |
| GP06 | The 5-angle self-review checks geometry only | A completeness pass against the blueprint (every face, every room, every road end, ground continuity) and a believability pass | RV02, RV05, OR11-OR14 |
| GP07 | Lighting and mood were split between skills and had no owner; the improve log itself lists "a lighting/mood owner" and "a concept-art role" as open | A mood and colour script per environment (light, palette, fog, time of day) reviewed with the environment designer | OR08; improve log 2026-10-15 "Next" 3 |
| GP08 | Character read (hateable villain, controlled army, own face per cast member) was found by the owner | A character read check: role readable from the face and posture in 1 s, expression set, cast looks like one world, different faces | OR16-OR20 |
| GP09 | A still cannot show motion; reward flights needed five rounds | Review motion from reference clips and frame sequences at phone size; ask for the clip before words; judge connection and clutter | OR25, OR26 |
| GP10 | Effort medium set for usage reasons; owner expects no mistakes | Effort high for review work; per-finding evidence and a "could not check" list | AD02 |
| GP11 | No rule for when and how to show the owner work | Show 2-3 renders at one camera; ask goal questions; keep "what works"; after approval, work proceeds and the owner sees results at Gate 3 | OR03, OR30, AF21 |
| GP12 | Taste memory was one small table mixed with physics, with no dates or quotes | A dated per-game taste log with the owner's words, split by area (world, UI, characters, effects), read first | AD10 |
| GP13 | Phone and accessibility checks were by eye ("phone first", colour not alone) | Thumbnail-size and greyscale runs at real device sizes; a colour-blind simulation; contrast ratios only for UI text and components, labelled with the rule used | AF04, AF10 |
| GP14 | The expert-talk reference file stayed empty | Keep a short, dated lesson list; promote a lesson only when it changes the agent's behaviour every time | AF header note |
| GP15 | No handling of owner-supplied references vs generated images vs real photos | A source ranking per subject (real photo, owner reference, generated), and a rule that owner references stay out of generation inputs | AB11, AB12, OR15 |

## 8. Pointers to the other kit papers (not re-checked here)

- Bible template and measurable checks: paper 02 (`02-direction-bible-readability.md`, sections 2 and 5). Compare AB01-AB06 with its template fields and AF10, AF22 with its check cards M1-M14; where a paper gives a measured method, use it over this file.
- Anchors, light, cohesion and feedback: paper 03 (`03-light-cohesion-anchors-feedback.md`). Compare AB08-AB09, GP04 and AF21 with it.
- OR05, OR07, OR11-OR14 are the environment designer's checks as much as the art director's; hand them to both. OR21-OR25 belong equally to the UI designer and the VFX designer; the art director reviews cohesion, they own the craft.
