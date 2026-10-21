> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-direction`. Source rows: N3 SV-01..27 (shot vocabulary, OPINION, 2026-10-21; geometry from F07 and Blender camera docs), N1 SH, MV, ST, ED. Typical length is UNKNOWN for every row: no source gives a defensible norm (N3 SV-00a).

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

Per move, write before choosing a path (N1 MV-02, MV-04): the reveal event; start and end composition; what may occlude; relation to the actor's speed; the static alternative. A stationary camera can still progress through entries, exits, turns, foreground occlusion and depth changes. Speed is UNKNOWN until authored and measured (N1 MV-05).

## 5. Composition and staging
- A thirds grid is a proposal for distributing attention, not a correctness test. Centred can mean confrontation or symmetry; off-centre can leave room for a threat, a gaze or a destination (N1 ST-04).
- Leading lines and depth layers help only if they lead to the intended information. Inspect from the final camera: foreground occluders, background tangencies, silhouette separation, overlapping bodies (N1 ST-04).
- A composition that reads as a full-size still may lose its key detail in a moving, phone-sized sequence: review in sequence and at target size.
- Crowded staging: name the primary readable action; decide whether each secondary action supports, delays or competes (N1 ST-03).
- Axis: the 180-degree system is a continuity convention (V, F08); breaking it is allowed when the gain is stated and a route back to readable geography exists (E, Murch; N1 ST-02, ST-06).

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

Fades, dips to black and wipes are transitions too: write why (time passes, a memory starts, a door "wipes" the frame as in N1 SC6-2). A transition used to hide a loading gap is a runtime fallback, recorded as such (`film-craft`).
