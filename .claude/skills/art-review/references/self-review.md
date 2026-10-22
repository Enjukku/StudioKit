# Self-review and review lines

> Author: J018 maker art-director · claude-opus-5-5 · high · 2026-10-22. Part of `art-review`; built also from the owner's Riot transcripts (J018). Every check the art director runs: on its own direction images, bible, review files and briefs (§2, §4), and on the captures of the work it reviews (§3). The review checklist rows K01-K25 (`look-check.md` §4) name the lines they rest on. Commands: `look-check.md` §2 and §5. Repair round 2: every environment measure on the environment-only capture, clipped white on the UI-off cut, separation and lower-body values from the bible's §7, the concept-art questions in the packet.

## 1. How to run it
- **Inputs.** Each line names its input; a line whose input is missing is NOT REVIEWED with the capture or test that would close it (could-not-check list). Capture kinds: `look-check.md` §1.
- **Light checks** (owner J005-D8). Numbers for every case: run every measure the stage needs on every capture. Open images only for a failing number, the cold-read capture and at most 2 key cases; count images made, measured and looked at in the hand-back.
- **You see stills.** Timing comes from frame strips at a known rate and the partners' timing lists; feel at normal speed is the owner's call on a playable preview at the gate (write the line `owner-confirmed` or `not verified`, never `pass`).
- **Cold read** = what you see first, second and third on the phone-size grey (and black-fill) written before you open the brief's intent or the maker's notes, then compared with the intent. When your run allows a subagent (hand-spawned, inside the nesting limit), a fresh reader with only the image adds a second cold read; otherwise the next reviewer gives one at the check-in. A mirrored copy refreshes your own eye.
- **Starting values** below are PROPOSAL; the bible's value or the owner's wins; without either the line is MEASURED (a diagnostic), never pass or fail.
- **Order.** Run §3 big to small (gameplay read, composition, shape, value, light and colour, material and detail, identity and finish); stop at the first failing layer and report it before detail lines.

## 2. Your own direction work
| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| DR1 | The brief states problem, constraints (camera, device, budget, quality floor, mechanics and numbers, genre parameters), read-first items, target experience, the target player and a dated "fans want" line, and the success test before the first prompt; each image caption names the problem it answers | your brief, captions and the image log timestamps | all present and dated first |
| DR2 | Research board has both halves (our anchors; real-world per aspect with its purpose and one observed property taken), one outside-games source, a keyword table, pillar words, a sensitivity line, key features per subject, a real source per body part for creatures, overlap references for a fusion, a reference for every key pose and material | the board file | all present; no single reference copied (compare the rough with each board image) |
| DR3 | Hooks: 6-12 lines from different sources, the warm-up labelled; 3-4 kept that differ in proportion, material, density, light, camera reading or emotion; one radical; costume options shown in at least two attitude poses; merges named ("A's silhouette + B's materials") | hooks list; black-fill row of the contact sheet | the kept options' black-fills differ (not colour only); one radical present |
| DR4 | Grey and silhouette pass done before colour was judged: per option, `value` luminance image and `thumb` at the phone viewport; the read-first item holds the strongest local contrast | per option JSON; contact sheet (one image) | read-first item first in the squint contrast pairs (`look-check.md` §5 line 2); options failing it are not shown as recommended |
| DR5 | Owner sheet: the 2-3 options that passed DR4 (the recipe's G1 count) at equal finish and layout, labelled, each packet answering the six concept-art questions (`exploration.md` §3 item 5); the others listed with their failing numbers; goal question, one recommendation with a reason tied to the brief and the sell list, a rejection reason per option, risks; a direction is logged as closed only after the owner's words, and none reproposed without new owner words | the sheet, its note, the closed-doors list | all present; no failing option shown as an equal; no option visibly more polished |
| DR6 | Theme fit and niche: each option against the tone words; one line on how the theme differs from the nearest existing theme | option notes; bible tone words | no option reads as a neighbouring genre; the niche line exists |
| DR7 | Style levers stated (saturation, proportion push, realism, value structure) and one stylisation level for characters and places | the direction packet; a character-in-place rough | the levers named; the capture reads as one style family |
| DR8 | Every design choice traces to a line of the character card, personality words or sell list | the packet's choice list | no untraced choice |
| DR9 | Image budget kept and reported: hooks, generated (small, medium quality while exploring), regenerated (max 2 per image, counted inside the round cap), measured, looked at | the image log | within `exploration.md` §8 or the brief's cap |
| DR10 | Every generated image you hand on passed `exploration.md` §5 (views agree, construction and attachments possible, counts, light, no generic substitution, no proportion drift, no text or franchise trait, reads small, matches the lock); model sheets have front, side, back and the game-camera view; prompts name only parts the rig can move; placeholders marked PROPOSAL and listed as open items | each image with its §5 row results | every row passed or the image is in `_rejected/` |
| DR11 | Cheap proof before polish: the representative tests (hero blockout or proxy, one key place in greybox with 2-3 lighting variants, one shared event) were captured at the game camera next to a player-size avatar and passed the §3 read lines before any polish was asked | the test captures and their dates | passed and dated before the first polish request |

| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| BB1 | Every lock is a relationship with purpose, scope, example, failure example, a named test (a measure or a line here) and allowed variation; no direction text inside lock blocks | the bible revision | every lock has a runnable test |
| BB2 | The §7 standards of `art-bible.md` exist or are marked PROPOSAL / UNKNOWN: screen order, value bands with both units, reserved colours, key light per place, shape vocabulary, palette roles, motion line, sound pointer, UI thematic, identity anchors, theme library, exceptions, stylisation level, the named sources of a blended style | the bible revision | no blank row |
| BB3 | Drift check: lock text vs newest owner decision vs current anchor | bible, `decisions.md`, anchor register | all three agree, or one edit proposed for all three |
| BB4 | Exceptions (top tier, format pieces) each logged with the locks still protected and a decision id; none leaking into normal assets | bible exceptions table; review captures | every break traces to a row |

## 3. Reads on the captures you review
**Pick the lines by job.** Run EV1-EV7 first on every review; then the row for the recipe; add a line outside the row only when the goal question needs it, with the reason in the review file. Lines whose input is missing are NOT REVIEWED, never skipped silently.
| Job (recipe) | K rows | Line groups |
| --- | --- | --- |
| Direction round (any recipe) | K01, K12, K15 | §2 DR1-DR11, BB1-BB4; RD1-RD5; SH1-SH3; CL1-CL3 |
| Character (model, rig, animation, variant, cosmetic) | K01-K04, K06-K08, K10-K12, K23-K24 | RD1, RD3, RD6, RD13-RD16; SH1-SH9, SH12; CL3-CL6, CL11, CL16; MD1-MD5, MD7-MD9; ID1-ID13 |
| Stage (place, hub, level) | K01-K02, K04, K06, K09-K10, K13, K19-K23, K25 | RD1-RD12; SH5-SH6, SH14; CL1-CL9, CL13, CL15; MD1-MD6, MD9; CP4-CP6, CP9, CP11; WO1-WO8 |
| Effect | K01, K06-K07, K09, K11, K13, K19 | RD2, RD5, RD12; CL2-CL3, CL10; CP9-CP10; EVT1-EVT6 |
| UI screen | K01, K05-K07, K16-K18, K22 | RD1-RD2; SH5 (corners); CL2-CL3; CP1-CP2 |
| Cutscene | K01-K02, K04, K11, K21-K22 | RD1-RD2, RD10; CL8, CL13-CL14; CP3-CP5, CP7-CP8; EVT1-EVT2 |
| Marketing art | K01, K14, K22, K24 | RD4; ID2, ID8; CP1-CP3, CP5, CP8; MK1-MK8 |
| Feature (visible parts) | the rows of the crafts it touches | the groups of those rows |

Inputs abbreviated: **busy** = busiest game-camera capture; **cuts** = layer cuts (which layer competes; never a layer's own numbers); **ui-off** = the UI-off layer cut; **env** = environment-only capture (every measure of the environment: band, depth, extremes, saturation, reserved hues); **mask** = mask capture; **low** = lowest-quality capture; **strip** = frame strip at a known rate; **flat** = flat-key render; **line** = lineup; **phone** = `thumb` at the phone viewport.

**Evidence and inputs** (run first, on every review and every direction round)
| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| EV1 | Every image has a manifest row; versions, bible revision and anchors match the candidate; missing fields say `missing` | manifest | every row complete or flagged |
| EV2 | Every check names its input and label (gate-verified, MCP-verified, owner-confirmed, not verified); no check passed on an input that cannot show it (a timing claim from one screenshot, performance from the emulator) | your review lines | every line labelled; none overreaching |
| EV3 | Before/after pairs share camera, FOV, pose, light, seed and competing effects | the two manifest rows | identical, or the difference stated and the pair marked not verified |
| EV4 | The capture kinds the question needs exist: game camera at the game FOV, phone size, the real place, effects, other players and UI on, the busiest moment, the lowest quality; no verdict rests on a turnaround, an editor view or a close-up | manifest | each needed kind present or the line NOT REVIEWED |
| EV5 | Cold read written before the intent or the maker's notes were opened: first, second, third read and what each main shape reads as (a good misread may stay) | your notes, timestamped before the hand-back was read | present |
| EV6 | Fresh eyes: the mirrored and grey copies looked at once; on long jobs another reviewer's cold read | `look-check.md` §5 line 3; the luminance image | done |
| EV7 | Timing and feel: frame strips at a known rate for order and peaks; feel at normal speed sent to the owner's playable preview | strip; the owner's gate | `owner-confirmed` or `not verified`, never `pass` |

**Gameplay read and hierarchy**
| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| RD1 | Cold read names route, threat, objective, ally or enemy and own state at a glance | busy at phone, grey | every critical fact found in the cold read |
| RD2 | Read order: one contrast pair per ranked item (inside the item vs its adjacent background) on the squint view | busy, `look-check.md` §5 lines 2 | ratios fall in the brief's rank order; no environment element above a character or effect |
| RD3 | Layer bands: p5 and p95 of each layer region inside its band; no pure black in the environment | environment-only capture, play-area box (`look-check.md` §5 lines 8-9); flat or mask for characters | inside the bible's bands (starting values: `art-bible.md` §7); near-black px 0 in the environment box |
| RD4 | Focus by lowering: the focal subject's ring is calmer than the subject (narrower p5-p95) and its subject/ring ratio is the highest of the ranked items | busy + mask, `value --mask` | focal ratio highest; ring spread narrower than subject spread |
| RD5 | Extremes are small: the brightest values and pure white sit only on the named accents; no large clipped area, no two competing peaks | busy: `value --mask` p95 per region; ui-off: §5 line 9 on the box below the horizon, the accents' black-fill excluded (the HUD and a clipped sun never count) | top p95 on the accent region; clipped share outside the accents ≤ 0.0005 (starting value, PROPOSAL) |
| RD6 | Every character against every background, and typical avatar colourings, separate | flat character renders composited or captured in each place + mask | subject/ring ratio per pair at the bible's character target; critical markers at its marker target against the lowest-contrast local background (starting values: `art-bible.md` §7 Separation targets) |
| RD7 | The smallest gameplay object on the busiest floor is found, also with 30-50 % of it hidden behind cover; item types differ in top and side profile | busy with the object placed, phone | found and its type named in the cold read |
| RD8 | Detail clumps: busy zones sit on the named detail spots with rest areas between; the player band calm | squint view of busy | manual: matches the hierarchy table (no tool measure yet: proposal) |
| RD9 | Distance lowers contrast: near band vs far band | env, `value --box` per depth band (`look-check.md` §5 line 8; boxes below the horizon, rows from the depth markers) | far p5-p95 spread narrower than near |
| RD10 | Contrast follows intensity: dramatic moments wide, calm places narrower | ui-off captures of a climax and of a hub, `value --box` below the horizon | climax spread wider than calm spread |
| RD11 | The grey proof holds after colour and post: the colour capture's grey keeps the approved value order; the read survives Bloom and ColorCorrection off | grey of the approved rough vs busy; a recapture with post off | same rank order; read holds with post off |
| RD12 | Lowest quality keeps every cue (silhouettes, colour roles, key values, markers) | low next to busy | every listed cue present |
| RD13 | Characters: head, shoulders, hands and held item brighter and more contrasted than the lower body; the lower body still separates from the ground; a back view | upper vs lower: flat or mask, region masks (§5 line 1); lower body vs ground: the in-scene capture over the real ground + its mask capture, upper region excluded from the ring (§5 line 1, "Lower body against the ground"); never a flat render for the ground half | lower p50 ÷ upper p50 at or below the bible's ratio (starting value about 0.6-0.7: `art-bible.md` §7 Value bands); lower subject/ring at the character target (§7 Separation targets) |
| RD14 | Noise in motion: the character stays nameable while moving with lighting and a typical effect on | strip (frames from the capture operator) | named in every key frame of the strip |
| RD15 | Parts separate by value and shape, not by lines: in grey with outlines ignored and any Highlight turned off, every main part and plane change is a value step | grey of flat or busy; a recapture with Highlight off | every main part separates |
| RD16 | High-contrast features grouped and spaced like letters in a word: no shimmering dense pattern, no lone bright outlier away from the focus; an object's detail cluster sits in close values framed by a contrasting base | phone; `value --mask` on the detail cluster | the cluster's p5-p95 narrow; no outlier in the cold read |

**Shape and silhouette**
| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| SH1 | Subject, role or owner, mood (dangerous, friendly, stable), the archetype when it is one, and how it would move (heavy, light) named from the black-fill alone | flat or mask, `silhouette` + phone | named in the cold read; matches the brief and the motion set |
| SH2 | The identity anchors (the bible's list and count, `art-bible.md` §7) are visible and chunky at phone size; pushed features change the outline | phone of the black-fill | every listed element visible |
| SH3 | Intended silhouette cuts survive at phone size; no tiny notches | phone | each cut visible |
| SH4 | Size steps among sibling shapes | `silhouette` components or bbox of each sibling | no two neighbours within about 15 % of each other |
| SH5 | One shape vocabulary: off-vocabulary shapes counted; shape meaning matches role (threats sharp, safe things soft, per the bible) | a prop and detail sheet; line | off-vocabulary shapes rare and deliberate |
| SH6 | Size signals importance across the lineup | line, `silhouette` bbox heights | size order matches the threat or value rank |
| SH7 | No look-alike: the new design vs its nearest neighbours in shape and palette | line; `silhouette --compare`, `palette` | IoU and palette overlap recorded; a high overlap is a finding |
| SH8 | Extremities track: hands, head and feet separate; nothing hangs in front of shoulders and arms in idle, run and attack | key-pose black-fills from the animator | arm outline separate from the torso in each |
| SH9 | Each key pose has one clear line of action; hook shapes, the signature shape and the move itself read at the held moments (key poses, hit pause), so the player's own move is known from its silhouette | key-pose black-fills at phone size | type, move, hook shape and signature element named in each |
| SH10 | One motif at big, medium and small scale, integrated, not a sticker; it still reads as a one-colour icon | flat; `thumb_check.py icon` on the motif's black-fill | at least 3 scales; reads at 150x150 |
| SH11 | Group silhouette tells the idea (team, encirclement) | black-fill of the group shot at thumbnail size | combined shape reads as intended |
| SH12 | One asymmetric element visible at the game camera | mirror of flat | the mirror differs visibly |
| SH13 | Main lines lead: one top line and one bottom line, slopes along the action, panel lines to shared points | edge or black-fill side view | lines converge or run parallel; no stray lines |
| SH14 | Backdrop pieces (plants, distant props) have one clear gesture, simple surfaces | black-fill of a backdrop group | each gesture a clear curve, not a blob |

**Colour and light**
| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| CL1 | Reserved-hue share outside gameplay objects | env; §5 line 4 with the gameplay objects excluded (never a frame with characters, effects or the HUD: a red health bar counts as decoration) | near 0 (the owner sets the number); the bible's distance (starting value: `art-bible.md` §7) |
| CL2 | One meaning per hue: effects, UI cues and pickups by colour role; no hue for both help and harm | captures + the colour-role table; `palette --roles` | no double meaning |
| CL3 | Not colour alone: every team, tier, state and threat told apart in grey | busy grey (luminance image) | all identified |
| CL4 | Palette roles: area shares of the top colours; each colourway's grey keeps the value structure and balance | flat or masked region, `palette`; grey of each colourway side by side | near 60/30/10 or one dominant family as the bible says; same value order per colourway |
| CL5 | New colours come from the palette: role swatches vs clusters | `palette --roles`: the bible's authored hexes on a base-colour render; on a lit capture the roles as rendered by their reference blocks under the same light, plus a neutral-light capture for a dim or night look (`look-check.md` §2 Roles file) | every role within the bible's ΔE (diagnostic without one) |
| CL6 | No flat fills; shadows shift hue, not just value; gold stays saturated in shadow | flat or busy: `look-check.md` §5 line 10 on a box on one material's lit side (screening aid; its false readings are listed there); `contrast --sample` lit vs shadow boxes (their hex) | `hue_sd_deg` above the flat limit (starting value: line 10), the variation inside the colour family; a value texture in one hue fails as monochrome; shadow hue differs from lit hue |
| CL7 | Light and shadow temperatures follow the bible | `contrast --sample` lit and shadow boxes on one material | shadow on the bible's temperature side |
| CL8 | One key light direction per place and every light motivated; highlights on all assets face the same way | grey of busy; lighting variants | one direction; every light has a source |
| CL9 | Saturation field: the player band calmer than above head height; saturated pixels a small share on focal spots | env, §5 line 5 with boxes from the row markers, the upper box below the horizon | player band chroma below the band above |
| CL10 | An effect's main hue sits next to its caster's; one main hue per effect | strip peak frame; `palette` on the effect mask | hue family adjacent; one main family |
| CL11 | Same-colour parts that overlap still separate | key pose with overlap, grey; `contrast --sample` | a value step between the parts |
| CL12 | Finals checked on a phone view and exported sRGB | the export file; a phone or phone-size capture | no large hue or value shift; profile sRGB |
| CL13 | Mood reads from colour alone | squint of busy at thumbnail size | cold read names the mood |
| CL14 | Separation light: rim light where a figure meets a background of similar value; threat lit from below in reveals | cutscene or key-art grey | manual: edge visible; light direction matches the beat |
| CL15 | No key position in deep shadow; a character standing there still separates | busy grey with a character at each key position + mask | subject/ring ratio per position at the bible's character target; none lost |
| CL16 | Materials in light: skin temperature consistent across face, hands and body; environment bounce in character shadows where the bible asks | `contrast --sample` boxes on each | same temperature family |

**Materials and detail**
| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| MD1 | Every material named at game size (gold reads gold); masses (hair, grass) read as clumps | busy at phone; cold read | every material named |
| MD2 | Detail that vanishes at phone size is gone or in texture; every side an orbiting camera sees is finished | phone; orbit captures from the modeler or operator | no wasted detail; no bare side |
| MD3 | Form and finish: still objects read as 3D in grey (form shadows that follow the planes, a clear terminator, contact shadows where parts touch); key forms have defined edges, not every edge hard, not all soft; contrast committed at the end; no muddy overworked zone | grey of flat or busy at phone and one close view | manual: no flat, mushy, stiff or muddy zone |
| MD4 | Controlled variation: wear at touch points, no exact repeats or kit duplicates at the same angle in one view, no visible tiling, no identical mirrored marks or text, no single flat swatch | busy; CL6's line 10 per material | no repeat at the same angle; each material passes CL6 |
| MD5 | Grounded and to scale: no floating props, no straight clipping seams, a player-size reference near every large focal prop | busy | none floating; reference present |
| MD6 | Key materials judged under the place's final light, compared with the mood anchor | busy next to the anchor | reads as the anchor's material |
| MD7 | Functional parts readable: how it is held and used | flat or busy | stated from one image in the cold read |
| MD8 | Ornament is one shaped motif; patterns invisible at thumbnail size, visible close | phone and a close render | as stated |
| MD9 | Even finish: no region clearly more finished than its equals (a finished statue in blurred grass) | busy and one close view | none |

**Composition and frame**
| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| CP1 | Composed in the real frame: overlay of HUD and safe areas, the icon square, badge and pass circles, thumbnail bottom band; nothing focal under them | busy with HUD; key art with the overlay | no focal element under an overlay |
| CP2 | Small frames: the identifying parts fill the crop; faces large enough | `thumb_check.py icon`; crops at player size | anchors and face readable |
| CP3 | Flow: main lines converge on the focal point; motion lines in stills are 2-3, through the focus | grey or black-fill of the frame | lines lead to the focus |
| CP4 | Three depth groups readable; foreground never blocks the play view | busy grey; key art layers | three value planes; play view clear |
| CP5 | Negative space planned: calm room around hero and title; no accidental bare gaps | busy or key art grey | as stated |
| CP6 | The focal landmark is the tallest shape and not occluded | black-fill of the level view | tallest, visible |
| CP7 | Visual weight balanced where planned | grey | manual: no unplanned heavy side |
| CP8 | Camera height states status in icons, thumbnails, previews, cutscenes | the image and its brief | matches the brief |
| CP9 | Judged on the integrated capture; the clean frame (no effects) passes on its own | busy and the effects-off cut | both pass |
| CP10 | After the hit the eye moves to the result (brightest region moves) | strip before and after the hit | brightest region moves |
| CP11 | The first view after spawn frames the goal or main landmark as the strongest focus | capture of the first frame after spawn at the default camera | goal first in the cold read |

**Identity, variants and tiers**
| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| ID1 | Every identity anchor present in the variant (one may hide in a pose); dropped landmarks have their slot filled | base and variant flat or mask, `silhouette` of both | all anchors listed as present |
| ID2 | Same likeness in model, icon, portrait, cutscene, key art | the set side by side at one size with the anchor images | "same person" for each |
| ID3 | Variant type recorded and true: new version (new palette) or same character (base palette) | `palette` of base and variant | change matches the record |
| ID4 | Next to 2-3 approved anchors at the same size it reads as the same game | the new piece beside the anchors | cold read: one game |
| ID5 | Cosmetic footprint and brightness: black-fill area vs base at the same camera; cosmetic glow below combat-effect brightness; combat cues still visible | flat or mask of base and variant (`area_frac`, `bbox_px`); busy with the cosmetic | within the band (about 10 % of base area, the design table's value); glow p95 below the combat flash |
| ID6 | Tiers: silhouette and finish rise with real rank; top-tier exception documented; premium parts take separate finishes and keep at least the base's secondary motion; paid random tiers: frames and colours follow the bible, no lower result wears a higher tier's look, no effect covers the odds (`platform-policy` wins) | line of the tiers; reveal frames from the VFX designer | order matches the design table |
| ID7 | The card's words (a prop's personality words, a variant's tone with its appeal kept) and what the thing does and how tough it is come back from a cold read; an outside reader's genre, mood and role match intent | busy or flat, no notes | words and genre match |
| ID8 | Theme reads at thumbnail size; the hidden story element is invisible there and findable close up | phone and a close render | as stated |
| ID9 | Personality accents visible at the game camera | busy at phone | each accent visible |
| ID10 | Stated culture represented accurately; sensitive themes moved onto a prop motif; no franchise trait | the image and the brief | reviewer check, `platform-policy` where needed |
| ID11 | The fantasy survives every real view: tiny, from above and behind, in a fast frame; design survives extreme poses | phone, back view, strip frames, the rigger's stress poses | recognisable in each |
| ID12 | The built asset keeps the approved image's iconic qualities at least as strong; the gaps the modeler listed were decided inside the bible or by a paint-over | the image next to the game-camera capture at the same size | every iconic quality listed as present |
| ID13 | Your variant or remake brief holds: the twist line with its lore reason, the two-line story, the anchors kept, each ability's VFX and sound re-theme note, 1-3 theme nods on anchors, inherited parts justified or replaced by similar mass, the prop citing the costume revision and a shared motif, costly parts with a reason and fallback, concepts made on the mannequin overlay; for a remake, loved traits kept and dated traits trimmed | your brief | every item present |

**Places**
| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| WO1 | Each piece says what it is and what you can do, and behaves as it looks (an open doorway is walkable, soft things do not block, one material per gameplay property); each zone has a landmark with a unique black-fill visible from its entry and every fork | busy and fork captures; the play-test mismatch list | named in the cold read; landmark visible; no unexplained mismatch |
| WO2 | A player-size reference near every large focal prop; interaction props sized to the player | busy; studs from the operator | present; sizes match |
| WO3 | Story facts readable (who lives here, what happened) | busy, cold read | at least one intended fact named |
| WO4 | Hazards show their source and containment; boundaries are believable pieces | busy | stated per hazard and boundary |
| WO5 | Objectives marked on the approach and in the floor; head-height cues where height matters | approach captures | marker seen before entry |
| WO6 | Props judged inside their place at the game camera, not alone | in-place capture per approved prop | one per prop |
| WO7 | In a themed game the greybox already reads as a place: each major blockout shape could be a real structure of the theme | greybox capture at the game camera | a real structure named per major shape |
| WO8 | Completeness: every face finished (no missing or untextured side), every room furnished, every path joined, the ground continuous (no gaps, floating edges or holes at seams) | busy and orbit captures from the operator; the walk-through route captures | none missing (the first game's most repeated owner correction) |

**Events across crafts** (you check agreement; the owners judge their craft)
| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| EVT1 | One event: pose, effect, UI and sound cues share one name, one mechanic verb, one importance rank (top tiers dominate, low tiers do not compete), the bible's colour role, shape code and motion line; timing keys from the animator's timing list | strip; timing list; cue cards | agreement on rank, verb, colour and names; feel owner-confirmed |
| EVT2 | Effect read order: primary (where, what it hits) brightest; secondary weaker; few tertiary bits; the energy core brightest with a saturated halo | strip peak frame grey; `value --mask` per layer if masked | primary first |
| EVT3 | Effect shape code: heal, shield, damage told apart by shape in grey | strip key frames, grey | told apart |
| EVT4 | Worst-case crowd: every character and the thing the player acts on stay visible; nothing covers HUD or targets | busy with every player's effect | nothing needed covered |
| EVT5 | No popcorning in masses; strobes low and behind; the focus never flashes | strip | as stated (flash safety is the VFX designer's measure) |
| EVT6 | Ambient effects small, slow, partly hidden; map mechanics (pads, doors, teleporters) quiet outside their planned moments; nothing is the brightest or fastest thing near a sightline without a reason | busy and a short strip near a sightline | as stated |

**Marketing art**
| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| MK1 | Icon at 150x150: one shape, anchors visible, master square and at least 512 | `thumb_check.py icon` (key `FF00FF` on magenta) | master checks met; subject read at small size |
| MK2 | Thumbnail at the measured tile: subject reads; nothing essential in the bottom band | `thumb_check.py thumbnail --size <tile> --size-source "<capture id, device>" --bottom-band 20` with a mask | subject share in the band near 0 |
| MK3 | Truthful: every shown experience exists in the current game | the art next to in-game captures | each matched |
| MK4 | The launched thing is the hero and the largest readable element | thumbnail at the tile, cold read | named first |
| MK5 | Finals at final resolution, no upscale blur | file dimensions; 100 % view | dimensions match the target |
| MK6 | The master survives every planned crop; layers switchable | crops of the master at each ratio, `thumb_check.py` | hero and title in every crop |
| MK7 | Brand pattern kept with one visible change per event; the event motif traces to an in-game icon or the story's key object; the brief names its tone shift against the last event | new logo or title beside the last two at thumbnail size | exactly one property differs; the motif's source named |
| MK8 | Promo and story art: a one-sentence premise reads; the character's pose matches the signature move's key frame from the game | the image next to the animator's key frame | pose matches; premise named in the cold read |

## 4. Your notes, briefs and hand-back
| ID | Look for or measure | Input | Pass (starting value) |
| --- | --- | --- | --- |
| FB1 | Every note names the goal, the layer, the observation (region, numbers) and one fix or a paint-over; worst problem first | your review file | all notes complete |
| FB2 | Visual notes carry a marked capture or a paint-over, before and after; generated paint-overs only for the 1-2 worst notes, inside the image cap, with the batch yes (else listed pending in `image-prompts.md`) | review file attachments; the image log | one marked capture or paint-over per visual note; generated count within the cap |
| FB3 | Notes describe problems, not solutions; a note that named a solution was restated; fixes re-checked against the problem | review file; the maker's re-capture | problem lines present |
| FB4 | Conflicting notes went to one owner with both readings at one camera | review file | no averaged note |
| FB5 | The review ran big to small; no detail note while a bigger note is open | review file order | order kept |
| FB6 | New wishes after the gate are tickets with a cost; gates not reopened; met conditions passed (no moving goalposts) | ticket list | as stated |
| FB7 | Briefs quote the same target-experience line, carry sourced standards (bible rows, decision ids), answer what the receiver needs and leave the craft open; every number has a source; receivers' hand-backs list no unanswered look question | briefs; receivers' hand-backs | no unsourced number; zero open look questions |
| FB8 | You asked for rough states (blockout, first capture, option sheet) and gave notes there, not first at polish | job log | notes dated at the rough stage |
| HB1 | One honest weakness of your own work, with a next step (or why there is none) | hand-back | present |
| HB2 | Budget used and every stop criterion shown passing | hand-back | present |
| HB3 | Images made, regenerated, measured and looked at | hand-back | counted |
| HB4 | Could-not-check list: step, missing input, the capture or test that closes it | hand-back | present (or why empty) |
| HB5 | The direction is pitched as the player's moment (what they see and feel in play), not an asset list | hand-back, owner digest | one or two concrete sentences |
