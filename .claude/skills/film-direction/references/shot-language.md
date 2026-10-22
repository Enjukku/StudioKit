> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-direction`. Source rows: N3 SV-01..27 (shot vocabulary, OPINION, 2026-10-21; geometry from F07 and Blender camera docs), N1 SH, MV, ST, ED. Typical length is UNKNOWN for every row: no source gives a defensible norm (N3 SV-00a). Revised by J018 maker film-director · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§2 camera height, §5 rewritten, §7 added).

# Shot language: what each choice can do, and what it hides

A vocabulary word is not a direction. "Push in" says nothing about path, speed, aim, roll or length; the shot list records those separately after previs (N3 SV-00b). Every effect below is a possibility in context, never a guarantee.

## 1. Size
| Size | Can do (when) | Can hide or cost | Write in the shot list |
| --- | --- | --- | --- |
| Extreme wide | Put scale or isolation first, when the surroundings dominate | Faces, small actions; reads as empty on a phone if the subject is tiny | what in the surroundings carries the meaning |
| Wide / long | Make geography and relationships readable (where things are, who is near whom) | Performance detail | the landmarks that must be visible (exit, threat, goal) |
| Full | Keep whole-body gesture and silhouette | Facial detail | the gesture that must read |
| Medium | Balance gesture with the surrounding relation | Wider geography | what relation stays in frame |
| Close-up | Put a face or a significant action first | Who or what approaches behind; context | the reaction or action, and what is deliberately excluded |
| Extreme close-up / insert | Isolate useful evidence (a lock, a key, a wound on a hand) | All context; the viewer may not know whose hand or where | what the insert proves and the shot that places it |
| Two-shot | Keep a relationship visible in one frame | Each face's detail | who is where, who looks at whom |
| Over the shoulder | Tie the viewed person to the observer | The observer's face | whose shoulder, the eyeline target |

## 2. Angle
| Angle | Can do (when) | Watch for |
| --- | --- | --- |
| Eye level | Observe without a vertical relationship; mutual recognition | Flat if every shot uses it |
| Low | Look up; may stress size or obstruction (a boss blocking the route) | Not automatic power (N3 DN-03); on avatars of different heights the line-up changes |
| High | Look down; may clarify vulnerability or layout | Not automatic weakness |
| Overhead | Make layout or graphic relationships stand out; can hide identity or flatten a relationship | Loses faces; can confuse screen direction on the next cut |
| Dutch (roll) | Destabilise an established balance on purpose | Comfort; needs a reason and a reduced-motion version |
| Point of view | Give the view to a perceiver, when context says whose | Say whose view it is and whether the next image is literal sight or an editorial link (N1 SH-06) |
| Camera height vs the eyes | A character above the camera looks down at the viewer and *can* read as distant or ruling; eye level *can* read as meeting an equal | Not automatic: write the intended feeling in the shot row and check it in the render |

## 3. Lens and perspective (geometry: V)
- From a fixed position, changing focal length changes only angle of view and magnification; relative perspective changes only when the camera moves (N1 SH-01, F05). "Long lens compresses" is really "the camera is far away".
- A focal length is meaningless without the gate (sensor size), the sensor fit and the output aspect; Roblox sets a field-of-view angle. Conversion and maths: `film-craft` (`references/blender-previs.md`).
- Production numbers (1917, as reported in Deakins interviews: mostly 40 mm, 35 mm inside the bunker, some river shots at 47 mm on a large-format camera) are examples with their camera, not presets (N1 SH-02, E; FC-03 confirmed in secondary interviews, the paper's own source unread).
- Long-lens framing: narrower view at the stated gate; distance sets the perspective. Wide-lens framing: broader view; check close-viewpoint effects on faces and props (N3 SV-26, SV-27).
- Never write "use a cinematic lens": store shot size, camera-to-target distance, FOV and its convention, focal length if used, pitch/yaw/roll, subject screen position and the information the shot must give (N1 SH-03).

## 4. Movement: operation vs effect
| Move | Operation | Can do (when) |
| --- | --- | --- |
| Pan / tilt | Rotate the view (horizontal / vertical) | Move attention; reveal height (footprint up to guardian) |
| Dolly | Move the viewpoint toward or away | Approach a discovery; withdraw |
| Truck | Move the viewpoint sideways | Show changing overlaps (tracking beside a walking pair) |
| Crane | Change height | Change spatial overview (rise out of a trench) |
| Orbit | Move around a subject | Change which relationships are revealed (the blocked route behind an actor) |
| Push in / pull out | Approach / withdraw as the beat turns | Emphasis or understanding changes; pull-out adds context or changes isolation (allies around the player) |
| Whip pan | Very fast rotation with a brief unreadable stretch | Hand attention over abruptly (an intimate moment interrupted by a figure in silhouette) |
| Handheld style | Controlled variation | Embodied observation; must have a calmer alternative if comfort suffers (N3 SV-20) |
| One shot / oner | Continuous presentation, not a movement type | Plan as named attention beats with a reason to transfer attention; a famous long take's length is that film's number, not a target (N3 SC-01) |

Per move, write before choosing a path (N1 MV-02, MV-04): the reveal event; start and end composition; what may occlude; relation to the actor's speed; the static alternative. If the static version reads as well, choose by style and cost, never by "motion is better"; a move hurts when it hides acting, loses a landmark or fights a subtitle. A stationary camera can still progress through entries, exits, turns, foreground occlusion and depth changes. Speed is UNKNOWN until authored and measured (N1 MV-05). A move that eases in and out reads as weight and intent; a constant-speed move reads mechanical, which is right only when the shot wants it (a security camera, a conveyor).

## 5. Composition and staging
**The first-second read.** Every shot names the one thing a player must take in during its first second (the story beat and the hero: "the statue's head is turning", "the exit is open"), seen at phone size. If the frame needs study, the shot fails, however good it looks.

**Read order.** Plan the reads: one primary, one secondary, at most a third; a phone screen holds fewer reads than a monitor, so cut to two where you can. Then make everything in the frame agree:
| Tool | How it leads to the primary | Watch for |
| --- | --- | --- |
| Value | the subject owns the widest value range and the brightest area; the surround is calmed first, then the subject raised if still needed | a bright sky, practical light or white prop elsewhere that out-shines it |
| Light | a motivated source lands on the subject; a value gradient falls off toward the frame edges | even, flat light that leads nowhere |
| Shape flow | set lines (paths, rails, roof lines, cliff edges), cast shadows and gaze lines point at the primary | lines that run off-frame or to a minor element |
| Motion | during a build, motion converges inward to the focus; after the peak, the old spot calms and the eye moves to the result | busy motion left at the old spot after the hit |
| Size and isolation | the primary is the largest readable shape, or the one shape isolated in calm space | two shapes of equal size competing |
| Accents | small secondary movers (birds, sparks, embers) sit along the path to the primary, smaller and lower in contrast | an accent that outshines the focus |
| Source of power | in a threat shot, the weapon, glowing hand or jaw is the primary read | a beautiful face while the danger sits in the dark |

When a shot does not read, find the missing contrast (value, size, shape, motion, isolation) and add it; adding detail adds noise and usually lowers the contrast that was there.

**Inside the real frame.** Compose from the first thumbnail inside the delivery frame: the letterbox bars, the subtitle zone, the skip control, the narrowest supported display at the fixed vertical field of view, and on the handoff frame the HUD players will have. Key subjects, eyelines and the action stay out of those zones. In a small or cropped frame the identifying parts fill it (a face and the signature item, not a small whole figure).

**Depth.** Three groups are enough: a darker foreground element at the frame edge that frames the subject and can be removed; the subject in the midground with most of the care; a quiet background that takes global changes. Distance lowers contrast and detail (Atmosphere and fog do this in Roblox), which pushes attention to the near action. A thirds grid is a proposal for distributing attention, not a correctness test; centred can mean confrontation or symmetry, off-centre can leave room for a threat, a gaze or a destination. Leading lines and depth layers help only if they lead to the intended information; inspect from the final camera for foreground occluders, background tangencies, silhouette separation and overlapping bodies.

**Scale, status and groups.** A group has its own silhouette: stage the combined outline so it tells the beat (heroes back to back inside a ring of small repeated threats reads as "surrounded"). A giant figure behind small heroes sells threat; scale contrast is pushed past real but the giant still stands, steps and lands with believable weight, and moves slower than a person. Camera height relative to the eyes *can* state status (a character above the camera looks down at the viewer); write the intended feeling and check it in the render. Size signals importance: the bigger threat reads bigger.

**Balance and restraint.** Dark heavy masses pull the frame to their side; place a brighter mass against them so the balance sits where you planned. One subject per shot; the layout is clean before smoke, sparks and particles are added. Negative space is planned (room for a gaze, a title or the subtitle line), never an accidental gap.

**Staging relationships.** Stage through space: who holds the doorway, who blocks a route, who turns away, who must move to keep eye contact. These beat "make him look powerful". One room, two characters, a doorway and two light zones can carry a scene before expensive faces exist. Crowded staging: name the primary readable action; decide whether each secondary action supports, delays or competes.

**One world.** The cast is the in-game cast (same rig, face kit, proportions and palette as its approved anchors); the light follows the game's setup and the art bible. Places show who lives there, what happened and how long ago (wear, repairs, things left behind), at backdrop-level contrast. Crowds and extras vary in pose and timing so no two neighbours move as copies; what carries meaning (a uniform, a team colour) never varies.

**Sequence and size.** A composition that reads as a full-size still may lose its key detail in a moving, phone-sized sequence: review in sequence and at target size.

**Axis.** The 180-degree system is a continuity convention (V, F08); breaking it is allowed when the gain is stated and a route back to readable geography exists (E, Murch; N1 ST-02, ST-06). Keep an overhead map (entrances, exits, threats, the camera half-plane) and a continuity ledger of eyeline target and screen direction per shot.

## 6. Cuts and their relations
| Relation | What it joins | Use when |
| --- | --- | --- |
| Match on action | Two parts of one action | Keep flow while changing size or angle |
| Graphic match | Similar shapes | Link two places or times visually |
| Eyeline | A look, then what is looked at | Attribute attention ("she sees the open lock") |
| Montage | Disparate events | Compress time or build a relation; keep the causal choice (N1 SU-02) |
| J cut | Incoming sound before its picture | Pull the viewer forward; a warning before the reveal (V, F10) |
| L cut | Outgoing sound over the incoming picture | Let a moment linger into the next |

J and L describe a relationship, not an overlap length (N1 ED-07). Name the intended relation instead of calling every smooth cut a "match cut" (N1 ED-03). Review an edit by saying what question each image opens and what the next image answers (N1 ED-05).

Fades, dips to black and wipes are transitions too: write why (time passes, a memory starts, a door "wipes" the frame as in N1 SC6-2). A transition used to hide a loading gap is a runtime fallback, recorded as such (`film-craft`). Title cards and graphic transitions move in the game's motion material (the art bible's motion line, the same as its UI: a light flutter or a heavy slam), so the tone reads before any word does.


## 7. Stills from a cinematic (key frames for marketing, splash and update art)
A still taken from a cinematic is composed as its own picture, big to small:
1. **Premise and hero first.** One sentence says the moment it shows; the thing being launched or featured (the new boss, the new world) is the hero: the largest readable element, at the highest contrast. Compare 4-5 small framings of the frame on one sheet and pick the clearest against the premise.
2. **The final frame and crop.** Compose inside the delivery frames from the start (16:9 thumbnail, the square or circular crops marketing will cut, the title's calm area); the identifying parts sit inside every crop.
3. **Composition and value on the clean frame.** Big shapes, the read order and the value plan pass in grayscale before colour, and the clean frame (no smoke, sparks or glow) passes before any effect is added.
4. **The pose comes from the game.** A character's pose is the signature move's key frame from the animation set, posed on the rig at the still's camera by the animator, never a new generic pose.
5. **Layers for the next maker.** Foreground, midground, background, lights and effects live in named collections or groups that can be switched, so marketing can make the whole asset kit (crops, banners, end cards) without asking again.
6. **Motion in a still.** Two or three committed flow lines (wind, cloth, a trail) run through the focal point; more lines become noise.

The marketing role owns the final crops and the promise (`marketing-design`); the director delivers the key frame and its layers.
