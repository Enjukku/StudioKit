---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J015-T01, Film_Director_Research_2026.txt lines 1-507"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Film-director paper part 1: evidence method, 15 directing rules, scene studies as mechanisms, shots, movement, staging, editing, short structure, light, acting, sound, game cinematics, skip / handoff, multiplayer contract (lines 1-507)

Paraphrased notes. The paper (FP) stays outside git. Every row cites `FP:<line>`. Nothing here is fact-checked and no web access was used (extraction only): claims are the paper's, listed in section 16 for the fact-check pass. The paper's evidence date is 2026-10-21. No source cited in lines 1-507 is dated after 2026-06-01 (newest: Adobe J/L page, updated 2025-08-22); the paper's own OPINION text is dated 2026-10-21. Four sources are undated live pages or interviews and must be re-read live (F05, F06, F08, G07). The paper is careful: its limits sit next to its claims and are collected in section 17. The rest of the paper (storyboards, previs, Roblox implementation, the Arcane supporting study) is not extracted here.

## 0. How to read

| Key | Meaning |
| --- | --- |
| FP:n | line n of `Film_Director_Research_2026.txt`. One paragraph = one line. Source register = FP:1205-1527 (only entries cited in lines 1-507 are resolved, section 15). A range such as FP:63-73 is a numbered list in the paper. |
| Tag | The paper's own mark, copied unchanged. VERIFIED = checked official technical spec, documented feature or reported measurement; it does NOT make the document's artistic advice proven (FP:13). EXPERIENCE = a filmmaker's, studio's or identified analyst's account (FP:13). OPINION = the paper's interpretation, procedure, example or acceptance criterion (FP:13). "none" = the paper does not mark that text. "none*" = no mark on the paragraph itself but it sits in a block whose source carries a mark (named in Src). Compound marks are copied as written. |
| Kind (my label) | RULE = one of the paper's 15 rules. MECH = transferable mechanism. BEATS = source-described order of a scene. COND = conditional effect. DEF = vocabulary. PROC = procedure or brief shape. CASE = reported account or fact. LIMIT = caveat the paper states. UNKNOWN = value the paper declares not established. FRAME = framing. The paper itself uses only Tag. |
| Src | The paper's source id, resolved in section 15. "live-read" = undated live page, read by the paper on 2026-10-21; access is not publication (FP:15). "paper" = the paper's own text, dated 2026-10-21. |
| Row IDs | EM evidence method, RU rules, SP shapes index, SC1-SC8 the eight scene studies, SH shots / angles / lenses, MV movement, ST staging, ED editing, SU short structure, LC light / colour, AC acting, SN sound, GC game cinematics, SK skip / replay / comfort / handoff, MM multiplayer / mobile contract, U unknowns, N numbers, FC claims to check, X limits. Hyphenated (SH-01). |
| Beats | A "BEATS" row keeps the order of what the source describes, stripped of plot names. The paper's own lists are not full edit lists (FP:57). Their counts and scene ids are organizing labels, not production facts (FP:17). |
| Rule of use | OPINION rows are proposals, never industry law. "May" / "can" in a row stays "may" / "can". Never turn an UNKNOWN into a number. A scene study teaches its mechanism; film details are anchors for the fact-check, not recipes. |

## 1. Evidence method and role (FP:1-17, 51)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| EM-01 | 1, 3, 5 | FRAME | A research and operating handbook for the role identified as film-director. Evidence checked 2026-10-21. Fixed pipeline: ChatGPT storyboard images, then Blender previs, then Roblox runtime. | none | - |
| EM-02 | 7 | FRAME | The role proposes how a story beat becomes images and sounds, explains the intended emotional change, and reviews the assembled result. The owner is creative director and decides. The game designer owns gameplay and story requirements; the art director owns the visual system; animator, environment artist, VFX, sound and UI designers execute. These boundaries and the pipeline are studio-brief requirements, not claims about other studios. | OPINION | paper, operating scope, 2026-10-21 |
| EM-03 | 9 | FRAME | Main recommendation: direct attention and decisions before polish. Specify what the player must understand, which image establishes it, what changes inside the shot, why the next cut is needed, and how the player returns to play. A prettier frame does not replace a legible sequence. An authored working method, not a measured law of audience response. | OPINION | paper, synthesis |
| EM-04 | 13 | LIMIT | VERIFIED covers the document, not the artistic recommendation. A claim may carry two marks when a documented capability supports an authored recommendation. | none | - |
| EM-05 | 15 | LIMIT | Scene studies cover only the portion their sources describe; they are not frame-by-frame logs of films the author watched. Quotes appear once, in the register. | none | - |
| EM-06 | 17 | LIMIT | UNKNOWN = the inspected evidence does not establish the value. It is not zero, not a default, not licence to pick a familiar number and call it research. The paper's filled example leaves durations, lenses, camera distances, camera heights and travel speeds open until real previs is measured. | OPINION | paper, evidence policy |
| EM-07 | 51 | FRAME | The 15 rules are authored operating rules dated 2026-10-21; the later sections separate the facts and practitioner evidence that motivate them from the rules. | none | - |

## 2. The fifteen rules (FP:19-49)

All 15 carry OPINION (paper, 2026-10-21). Rules 11 and 12 have their body in sections outside lines 1-507; only their anchors in this part are listed.

| ID | FP | Rule in my words | Tag | Detail in |
| --- | --- | --- | --- | --- |
| RU-01 | 21 | Fix the emotional change and the information the player gains before choosing camera coverage. | OPINION | EM-03, ED-04, SU-02 |
| RU-02 | 23 | Every shot has a job no other shot already does. | OPINION | ED-03, ED-05 |
| RU-03 | 25 | Describe framing effects as conditional. No angle or lens guarantees an emotion. | OPINION | SH-04 to SH-07 |
| RU-04 | 27 | Move the camera only when the changing view adds to the beat. | OPINION | MV-02 to MV-04 |
| RU-05 | 29 | Track staging, eyelines and screen direction across cuts before polish. | OPINION | ST-01 to ST-05 |
| RU-06 | 31 | Cut for a change in information, performance or emphasis, not on a fixed timer. | OPINION | ED-03 to ED-06 |
| RU-07 | 33 | Keep source timings exactly; mark absent timings UNKNOWN. | OPINION | EM-06, SC-00, section 14 |
| RU-08 | 35 | Direct the character's intention and visible change, not a pose name. | OPINION | AC-01 to AC-05 |
| RU-09 | 37 | Give sound an intentional relation to picture, including deliberate absence. | OPINION | SN-01 to SN-07 |
| RU-10 | 39 | State the player character's role and the return to gameplay. | OPINION | GC-01 to GC-03, SK-04, MM-06 |
| RU-11 | 41 | Treat generated storyboards as proposals that need continuity review. | OPINION | body outside part; only the pipeline in EM-01 (FP:5) |
| RU-12 | 43 | Resolve staging and timing in Blender previs before expensive finish. | OPINION | body outside part; GC-06 (FP:435) limits what previs proves |
| RU-13 | 45 | Verify the final Roblox sequence on the real target devices and under multiplayer conditions. | OPINION | LC-05, AC-04, MM-01 to MM-10 |
| RU-14 | 47 | Test skip, interruption and control restoration as separate endings of one sequence. | OPINION | SK-04 to SK-06, MM-05, MM-06, X-33 |
| RU-15 | 49 | Give the owner alternatives and evidence. Never turn a directing proposal into approval silently. | OPINION | EM-02, MV-04 |

## 3. Shapes the lead will build skills from (index only)

Each shape is written out in the cited row.

| ID | Shape | Row | FP |
| --- | --- | --- | --- |
| SP-01 | Reveal template: expectation, contradiction, comprehension, choice or control return | ED-04 | 293 |
| SP-02 | Reveal geometry: geography, somebody's alarm, object, consequential reaction | SC1-2 | 75 |
| SP-03 | Causal chain in verbs for an opening | SU-02 | 313 |
| SP-04 | Per-move brief (start info, motivating event, new reveal, end state) plus unmoved alternative | MV-04 | 253 |
| SP-05 | Shot record (separate fields) | SH-03 | 229 |
| SP-06 | Acting brief and causal-experience wording | AC-02, AC-04 | 379, 383 |
| SP-07 | Shared cue sheet and cue attributes | SN-02, SN-06 | 399, 407 |
| SP-08 | Light plan fields and sequence strip | LC-02, LC-05 | 345, 351 |
| SP-09 | Skip / replay / pause / comfort / handoff set | SK-04, SK-05 | 447-459 |
| SP-10 | Eight-point multiplayer contract | MM-01 to MM-09 | 477-495 |
| SP-11 | Overhead staging map and relationship staging | ST-03, ST-05 | 269, 273 |
| SP-12 | Reference-board delivery label | GC-06 | 435 |
| SP-13 | Edit audit: what question each image opens, what the next answers | ED-05 | 295 |

## 4. Section 1: directing attention through documented scenes (FP:53-219)

### 4.0 Frame

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SC-00 | 55 | FRAME | Directing makes a change in attention, understanding or relationship legible through images, performance and sound. Eight principal cases with different evidence scopes: three film cases reconstruct published shot order; the rest describe reframings or scene beats a source documents. Not eight measured shot-by-shot logs. Exact edit boundaries and unpublished camera metadata are UNKNOWN. | OPINION | paper |
| SC-01 | 57 | LIMIT | The lists rebuild only the shot changes or reframings the inspected sources describe. They are not edit decision lists. No shot duration, lens, camera height or movement speed is known unless the text states it. Film release dates differ from source publication dates. | none | - |

### 4.1 Study 1: reveal after an attack, Jaws 1975 (FP:59-75)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SC1-1 | 63-73 | BEATS | Order as described: a travelling two-shot of two walkers; inside that take a reported 180-degree pan swings the view to the sea while tracking continues; cut to a reverse of the pair approaching from farther away; in the reverse an upset third figure enters the foreground and the music changes before the discovery is shown, while the protagonist advances to foreground; cut to a detail of the grisly object; cut back to the protagonist with enough surrounding space to read his look. The pan is camera rotation, not proof of an editorial axis violation (FP:65). | EXPERIENCE | F01, Singleton, DGA Spring 2006 (page adds a 2025 anniversary intro) |
| SC1-2 | 75 | MECH | Reveal design: geography first, then somebody's alarm, then the object, then the consequential reaction. Do not open on the gruesome insert if anticipation is the goal. Duration and focal length UNKNOWN. | OPINION | paper |

### 4.2 Study 2: seeing a way out, Yojimbo 1961 (FP:77-89)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SC2-1 | 81-85 | BEATS | A captive's usable eye sits in a patch of light; the eye widens; cut to an open padlock; cut wider to the trunk that carries the lock, which makes a hiding place legible. | EXPERIENCE | F02, Aronofsky, DGA Fall 2006 |
| SC2-2 | 87 | MECH | A compact chain: perception, then a useful detail, then a spatial solution. In a game this could show an escape route without explaining dialogue. Do not call the third image the character's literal optical POV without checking footage. Times and lens values UNKNOWN. | OPINION | paper |
| SC2-3 | 89 | CASE | Aronofsky reads a repeated framing (the protagonist placed between two opposed pairs, at the start and later) as showing his place between rival factions. Practitioner analysis, not Kurosawa's documented intention. | none* | F02 (block EXPERIENCE, FP:79) |

### 4.3 Study 3: bathroom climax, Fatal Attraction 1987 (FP:91-113)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SC3-1 | 95-111 | BEATS | Condensed order (nine items, not every cut; the source account has 14 beats): a tactile-sound detail; a detail that justifies sound downstairs masking danger upstairs; one moving shot that leaves the full bath, follows a body and hand up to a wiped mirror and reveals the threat, with music starting at the reveal; a turn intercut with a breaking bottle; water on the downstairs ceiling linking the two spaces; a low, slightly tilted view with the rescuer's arrival; a wider view of the bath interrupting close coverage, with top and underwater views fragmenting the struggle; flat water and no music before the threat resurges; a weapon detail before the shooter is identified. | EXPERIENCE | F03, Lyne, DGA Spring 2010 |
| SC3-2 | 113 | MECH | Study information timing and sound masking (a reason for sound to hide danger, music entering at the reveal, music absent before a resurgence, a detail before identification). Not a recipe for Roblox violence. Durations UNKNOWN. Lyne's recalled lens and frame-rate estimates are uncertain and must not become exact specs. | OPINION | paper |

### 4.4 Study 4: Feast (FP:115-131)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SC4-1 | 117-125 | BEATS | Repeated meal compositions keep food central with a fixed camera; the dog looks up and really sees its owner's face; the camera becomes mobile at that emotional turn; the dog leaves the food to act for its owner. | EXPERIENCE | A01, Reed, 2014-11-13 |
| SC4-2 | 127 | CASE | The first storyboard cut and recorded dialogue made the film ordinary in the filmmakers' judgment; the food-centred restriction restored its distinctive point of view. Reed's six minutes covering twelve years describes the whole film, not this scene. | EXPERIENCE | A01 |
| SC4-3 | 129 | CASE | Light and shadow express the dog's food preference, not an objective good / evil code: good food lit, undesirable food shadowed. Osborne withholds camera movement until the dog's behaviour warrants it. | EXPERIENCE | A02, Osborne, 2014-09-08 |
| SC4-4 | 131 | MECH | Set up a repeatable visual contract before breaking it. Example transfer: repeat a reward-centred setup for a greedy companion; move the focal subject and the camera only when it notices a hurt friend. A story-specific analogy, not licence to copy shots. Check with before / after thumbnails: the viewer should name what stopped mattering and what replaced it. If the camera already moves constantly, the turn loses its contrast. | OPINION | paper, 2026-10-21 |

### 4.5 Study 5: Into the Spider-Verse (FP:133-137)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SC5-1 | 135 | CASE | Beveridge: the apprentice starts out of sync with the mentor, then coordinates, then they trade a glance. Character animation generally runs on twos while the moving camera runs on ones. Practitioner testimony, not an independent frame count. | EXPERIENCE | A04, 2019-03-22 |
| SC5-2 | 137 | MECH | Choreograph the relationship, not only the bodies: divergent launch and landing timing, then an aligned decisive action, then an earned mutual glance. Keep control and collision requirements instead of copying alternating frame rates. A variable-frame-rate Roblox camera is not an offline camera sampled on ones; the example cannot justify running the whole game at a lower frame rate. | OPINION | paper, 2026-10-21 |

### 4.6 Study 6: God of War, the mother's knife (FP:139-161)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SC6-1 | 141 | LIMIT | Based on cinematographer Dori Arazi's published ordered breakdown; the paper did not watch or time every frame. A shipped real-time scene, not a trailer. The sequence is reframing inside one continuous camera, not separate edited shots. | EXPERIENCE | G01, 2018-09-28 |
| SC6-2 | 145-159 | BEATS | Wide frame puts the child in cold exterior light; an opening door reveals a warmly lit body inside; cold backlight recedes as the lens tightens around mourning; a whip left reveals the father in cold silhouette and breaks the intimacy; camera and staging keep his cold lighting while he takes control and the child leaves; alone, he steps into warmth and briefly shows grief; his turn away returns the relationship to its colder presentation; later, after the child drops the knife, a threatening frame on the father sets up a reversal when he tends the child's injured hand. | EXPERIENCE | G01 |
| SC6-3 | 161 | MECH | Author a change in relationship, not a decorative orbit. One room, two characters, a doorway and contrasting light regions can carry a scene before costly facial detail exists. Colours are locally assigned to relationships and actions; no fixed colour = moral label. On a phone, check that silhouette, gesture and the injured-hand beat still read without close faces; reject any shot that needs a desktop-sized eyebrow to explain the goal. | OPINION | paper, 2026-10-21 |

### 4.7 Study 7: God of War, the first boss (FP:163-183)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SC7-1 | 165 | LIMIT | Combat designer Denny Yeh describes the shipped encounter's phase order and its production; not a frame-accurate shot list. | EXPERIENCE | G02, 2018-08-16 |
| SC7-2 | 169-179 | BEATS | Intro sends the player from the front of the house to the back; play starts with a comparatively passive boss, inviting a strike through destructible scenery; a transition throws both onto a roof, and spinning and impact motion hide staging fixes the no-cut camera needs; the next arena brings in the rage mechanic, then more defensive pressure; a quieter climb breaks the action before the last phase; the boss's fuller attack set doubles as a defence tutorial, favouring perceived intensity over excess first-boss difficulty. | EXPERIENCE | G02 |
| SC7-3 | 181 | CASE | Yeh reports that a closer camera and environmental destruction helped sell a human-sized opponent as a god-level threat. | EXPERIENCE | G02 |
| SC7-4 | 183 | MECH | The reveal should leave the player in an actionable arrangement: identifiable enemy, readable threat, usable ground, visible next action. Spectacle and instruction can share a beat. A first boss need not show every attack in its entrance. For a small team a purposeful cut often beats elaborate hidden repositioning kept only for a one-shot look. The camera trick must not blur where control returns. | OPINION | paper, 2026-10-21 |

### 4.8 Study 8: Half-Life: Alyx opening (FP:185-201)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SC8-1 | 187 | LIMIT | Derived from Valve developer commentary as transcribed by the Combine OverWiki mirror. The mirror says it transcribes official scripts, captions and internal data; the paper did not check it against the game audio. Valve confirms the commentary's release on 2020-11-12. An interactive attention sequence, not a fixed shot list. | EXPERIENCE (G04, secondary-hosted primary transcript); VERIFIED (G05) | G04 / G05, 2020-11-12 |
| SC8-2 | 189-197 | BEATS | Balcony: a distant landmark, mid-scale references, lighting and helicopter sound compete with inviting nearby objects. Greenhouse: a calmer space hosts a video call, keeping exposition apart from first input exploration. Strider: a close encounter with layered sound builds scale and physical presence. Refuge: quieter, optional object interaction deepens the protagonist's place in the resistance. | EXPERIENCE | G04 |
| SC8-3 | 199 | CASE | The call was moved because room objects distracted players; at the balcony it clashed with the establishing vista and control learning. | EXPERIENCE | G04 |
| SC8-4 | 201 | MECH | When players own the camera, direct the order of opportunities, not identical frames. Keep seeing the landmark, learning the controls and hearing the mission apart when they compete. A landmark reveal can start with sound and offer a safe viewing spot without locking the camera. VR staging does not transfer unchanged to phones; the transferable idea is information competition, which needs a phone playtest. | OPINION | paper, 2026-10-21 |

### 4.9 Evidence table and section-1 rule tables

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SC-02 | 205 | LIMIT | G01 supports intended framing, lighting and performance progression; it does not support universal colour psychology or measured emotion. | none | G01, 2018 |
| SC-03 | 207 | LIMIT | G02 supports a designed handoff, staging, tutorial and escalation; it does not support an optimal boss-intro duration. | none | G02, 2018 |
| SC-04 | 209 | LIMIT | G04 / G05 support a documented interactive attention sequence (with the mirror caveat); not fixed shots or identical player behaviour. | none | G04 / G05, 2020 |
| SC-05 | 215 | CASE | Rule: tell cuts from internal reframing. Evidence: a Raiders take reported at 90 seconds, and only that figure (see X-30 for the tag conflict). | EXPERIENCE and analyst observation | F04, 2014-05-06 |
| SC-06 | 217, 219 | LIMIT | Do not invent source coverage (exact shot timings UNKNOWN). Transfer the mechanism, not the imagery (no universal scene length). | OPINION | paper, 2026-10-21 |

## 5. Section 2: shot size, angle, lens (FP:223-241)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SH-01 | 225 | MECH | From a fixed position, a change of focal length changes angle of view and magnification, not the relative perspective of objects. Keeping the same subject size across a focal-length change usually means moving the camera, and that move changes perspective. Do not merge geometric perspective with lens aberration or edge distortion. | VERIFIED | F05, undated, live-read |
| SH-02 | 227 | CASE | Deakins on 1917: Alexa Mini LF with Signature Primes; mostly 40 mm, 35 mm inside the bunker, some river photography at 47 mm to leave out background. Sensor / filmback goes beside every focal length. Production examples, not what a millimetre "feels like". | EXPERIENCE | F06, undated interview, 2020 awards season, live-read |
| SH-03 | 229 | PROC | Shot record: keep separate fields for shot size, camera-to-target distance, filmback / FOV, focal length where applicable, pitch / yaw / roll, subject screen position and intended information. Reject a bare instruction to use a cinematic lens as under-specified. | OPINION | paper |
| SH-04 | 231 | COND | Size: extreme wide can put distance or environment ahead of a face; medium can keep useful gesture; extreme close can exclude context on purpose. | OPINION | paper |
| SH-05 | 231 | COND | Angle: eye-level, overhead and POV answer different spatial questions. Overhead can clarify layout, hide identity or flatten a relationship, depending on staging. | OPINION | paper |
| SH-06 | 231 | PROC | POV: say whose perception is shown, and whether the next image is literal optical vision or an editorial association. No shot size, angle or lens guarantees an emotion. | OPINION | paper |
| SH-07 | 233 | COND | Ask what the frame leaves out. A close shot can clarify a performance and hide someone approaching behind. A wide shot can feel intimate when shared action and distance carry the bond. Choose the information trade-off before an emotional adjective. | OPINION | paper |
| SH-08 | 237-241 | LIMIT | Separate viewpoint from focal length (VERIFIED, F05). Keep production context with every lens figure (EXPERIENCE, F06). Typical shot lengths per mood are UNKNOWN (OPINION, evidence policy). | VERIFIED / EXPERIENCE / OPINION per row | F05, F06, paper |

## 6. Section 3: camera movement (FP:245-261)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| MV-01 | 247 | CASE | 1917 final run per Deakins: the camera rises from the trench on a 50-foot Technocrane, is handed to a 20-foot crane on a vehicle, tracks the run, then booms as the runner returns to the trench. The crew rehearsed transitions and timings before shooting. A production path, not a full list of hidden joins. | EXPERIENCE | F06 |
| MV-02 | 249 | PROC | Before choosing a spline or rig, fix the reveal event, start and end composition, occlusion constraint and relation to actor speed. A still camera can still deliver progression through entries, exits, turns, foreground occlusion and changing depth. Compare a static blocking pass with a moving one before paying for choreography. No source gives a universal m/s or degrees/s for fear, grandeur or sadness. | OPINION | paper |
| MV-03 | 251 | DEF | Pan / tilt rotate the view; dolly / truck move the viewpoint; crane changes height; orbit circles a subject; push-in approaches, pull-out withdraws; whip pan moves attention fast with deliberately blurred or briefly unreadable travel; handheld adds variation, but simulated shake must still serve the scene and comfort needs; a one-shot is continuity of recording or presentation, not a particular move. Working vocabulary; emotional effects stay conditional. | OPINION | paper |
| MV-04 | 253 | PROC | Per move, write: starting information, the motivating event, what is newly shown, the end state. Test an unmoved alternative; if both communicate equally, pick by approved style and production trade-off, not by assuming motion is better. A move can hurt by hiding a performance, losing a landmark, fighting a subtitle or causing discomfort. Numeric speed limits need this project's own captures. | OPINION | paper |
| MV-05 | 257-261 | LIMIT | Speed UNKNOWN until authored and measured. Do not turn crane gear into mood presets. For calmer cinematic treatment, no numeric shake threshold is published. | OPINION; EXPERIENCE; VERIFIED and OPINION (G07) | paper, F06, G07 |

## 7. Section 4: composition, staging, space (FP:265-281)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| ST-01 | 267 | DEF | The 180-degree system keeps dialogue coverage on one side of the character / action axis to hold screen relationships. A convention. | VERIFIED | F08, undated, live-read |
| ST-02 | 267 | CASE | Murch treats complementary gaze directions as a continuity check, and allows sacrificing continuity when emotion or story justifies it. | EXPERIENCE | F09, 2020-02-10 |
| ST-03 | 269 | PROC | Draw an overhead map: entrances, exits, threats, the current camera half-plane. Track gaze target and screen direction per shot. Change the line by a readable on-screen reposition, a re-establishing composition, or a deliberately disorienting cut. Judge what the player can infer; do not reject every axis crossing automatically. In crowded staging, pick the primary readable action and decide whether secondary action supports, delays or competes. | OPINION | paper |
| ST-04 | 271 | COND | A thirds grid distributes attention; it is a proposal, not a correctness test. A centred figure may express confrontation or symmetry; off-centre may leave room for a threat, gaze or destination. Leading lines and depth layers help only if they lead to the intended information. Check foreground occluders, background tangencies, silhouette separation and overlapping bodies from the final camera. A composition that reads in a full-size still may lose key detail in a phone-sized moving sequence. | OPINION | paper |
| ST-05 | 273 | PROC | Stage relationships by approach, retreat, interruption and unequal access to space. Record who controls a doorway, who blocks whose route, who turns away, who must move to keep eye contact. These are more specific than telling a character to look powerful. A deliberate axis break needs a stated intended experience and, where gameplay needs it, a route back to readable geography. | OPINION | paper |
| ST-06 | 277-281 | LIMIT | Screen relationships: the 180 system is a convention (VERIFIED, F08). A defended continuity sacrifice has no automatic penalty score (EXPERIENCE, F09). Judge composition in sequence and on the target display; no mandatory thirds placement (OPINION). | per row | F08, F09, paper |

## 8. Section 5: editing rhythm and tension (FP:285-305)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| ED-01 | 287 | CASE | Murch ranks emotion, story and rhythm above continuity; his 51% for emotion states priority, not a measured psychological share. Do not train an agent to score audience emotion from those percentages. | EXPERIENCE | F09 |
| ED-02 | 289 | DEF | A J cut starts the incoming audio before its picture; an L cut carries outgoing audio over the incoming picture. These are timing relations, not required overlap lengths. | VERIFIED | F10, updated 2025-08-22 |
| ED-03 | 291 | PROC | Name the relation a cut makes: match-on-action (parts of one action), graphic match (shapes), eyeline (looking linked to the thing looked at), montage (time compression or a built relation between unrelated events). Do not call every smooth cut a match cut. Hold a reaction only while something perceptibly develops. Cut when the next image adds information, shifts allegiance, completes an action or makes a deliberate contrast. Test the real animatic with and without the cut. | OPINION | paper |
| ED-04 | 293 | PROC | Reveal template: expectation, contradiction, comprehension, choice or control return. A proposal, not a discovered universal. No consulted film source gives an ideal Roblox intro length, boss-intro length, close-up duration, maximum unskippable interval or cuts-per-minute target. Set provisional durations in your own animatic, label them design choices, and record comprehension and skip behaviour. | OPINION | paper |
| ED-05 | 295 | COND | Suspense differs from delay: a hold works when a changing expression, offscreen cue or approaching consequence gives something to track; a hold with no development may only postpone information. Rapid montage compresses time but can delete the causal action that makes the next event clear. Audit: state what question each image opens and what the next answers. | OPINION | paper |
| ED-06 | 297 | PROC | Rhythm is the spread of new information, not the cut count. A continuous take can hold several attention changes; a fast edit can repeat one idea. When comparing versions, keep the approved story outcome and audio revision explicit so a changed response is not blamed on shot length alone. | OPINION | paper |
| ED-07 | 301-305 | LIMIT | Murch percentages are priorities (EXPERIENCE, F09). J and L describe relations, not seconds (VERIFIED, F10). Mood-to-seconds mapping UNKNOWN: measure the real edit (OPINION). | per row | F09, F10, paper |

## 9. Section 6: short structure, setup, payoff, attention (FP:309-337)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SU-01 | 311 | CASE | Osborne's first dinner list ran from single life through dating and romance to a breakup; a one-second-per-day experiment suggested quick-edit compression. An inspiration experiment, not a claim that the finished film uses one-second shots. | EXPERIENCE | A02, 2014-09-08 |
| SU-02 | 313 | PROC | For an opening, separate what the player needs to act from what only enriches emotion. Write the causal chain in verbs: wants, attempts, meets resistance, notices something, chooses, changes. A diagnostic, not a mandatory six-beat formula. Repeat a framing or object only if its meaning changes. Montage compresses elapsed story time; it does not permit skipping the choice that explains the next action. | OPINION | paper, 2026-10-21 |
| SU-03 | 317-321 | LIMIT | Reed's six minutes / twelve years is a production description, not a Roblox target (EXPERIENCE, A01). One second per day describes the experiment only (EXPERIENCE, A02). Preserve the choice that changes behaviour; no numeric threshold (OPINION). | per row | A01, A02, paper |
| SU-04 | 325 | PROC | A setup earns its place when it changes the meaning of a later event: record the expected reading and the later re-reading. If the player must grasp an ability or exit, the payoff must be actionable, not just surprising. Show a decision through behaviour when that reads; use dialogue or UI when silent staging would hide essential information. The show-rather-than-tell maxim is a preference, not a ban on words. | OPINION | paper |
| SU-05 | 327 | PROC | State the minimum dramatic change and test the animatic against it. A shot may be event-bounded (it lasts until the player recognizes a blocked exit) before seconds are approved. Do not turn that into a universal attention span. | OPINION | paper |
| SU-06 | 329 | UNKNOWN | No source in the research gives an ideal Roblox cutscene length, a standard skip rate, a numeric phone-viewer attention limit, or a reliable causal link between cinematic duration and retention. Lens values, shot lengths and runtimes of the analysed scenes stay UNKNOWN where sources omit them. A bounded gap, not a claim that no data exists anywhere. | none | - |
| SU-07 | 331 | LIMIT | The authored-camera versus player-directed split is mostly a difference in artistic goals. The sharper disagreement is Laidlaw's historical preference for linear narrative satisfaction: keep it as attributed practitioner opinion, not scientific consensus. Modern comfort, accessibility and replay needs also argue against copying every historical staging choice unchanged. | none | G03 (by name only here) |
| SU-08 | 335, 337 | LIMIT | Do not infer attention limits from famous shorts (Roblox skip rate and ideal length UNKNOWN). Give a setup a consequential payoff; no prescribed beat count. | OPINION | paper |

## 10. Section 7: light, colour, sequence mood (FP:341-359)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| LC-01 | 343 | CASE | Deakins on Blade Runner 2049: the desert colour came from tested combinations of camera filtration, light gels and gelled windows, not post. For 1917's town: moving flare light and a burning-church lighting effect planned with a scale model. | EXPERIENCE | F11, 2017-09-14; F06 |
| LC-02 | 345 | PROC | Plan light as a change in visibility and attention, not a mood adjective. Name the motivated source, subject / background separation, bright-area hierarchy, silhouette readability and what stays hidden. Keep colour continuous across the sequence, then test deliberate contrast at the turn. A palette can set a learned story association; fixed equations such as red = anger or blue = sadness are not supported. Review in the final delivery transform: a lovely previs does not prove readable faces under the gameplay camera. | OPINION | paper |
| LC-03 | 347 | CASE | Fortiche makes at least one colorscript vignette per sequence, during or after boarding, to judge emotional progression. No exact colour values given. | EXPERIENCE | A05, 2024-12-30 |
| LC-04 | 349 | CASE | DeBlois: Deakins tied storyboards, layout and lighting together on the Dragon films. In one courtship scene dawn grows across shots; sunlight bouncing off rock warms the scene and signals time passing. DeBlois objected to locking composition long before light and shadow were known. | EXPERIENCE | A06, 2020-01-08 |
| LC-05 | 351 | PROC | Sequence strip before final lighting, per vignette: subject value, background value, dominant hue family, practical light source, intended emotional shift. Judge each beside its neighbours. Hue-emotion links are project conventions, not universal psychology. For a reveal plan both the concealing image and the revealed one; a bare request to brighten is not enough. Judge Roblox output from captures on the target device; a Blender preview's tone does not carry over unchanged. | OPINION | paper, 2026-10-21 |
| LC-06 | 355-359 | LIMIT | Board the colour progression (at least one vignette per sequence is Fortiche's reported process). Include light and shadow before committing composition (no universal lighting ratio or brightness value). Colour as a local narrative convention (RGB values are project decisions). | EXPERIENCE; EXPERIENCE; OPINION | A05, A06, paper |

## 11. Section 8: directing animation and performance (FP:363-391)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| AC-01 | 367-377 | BEATS | Piper (supporting study): the hero avoids the threatening waves, back turned; a smaller creature gives a different example of behaviour; fear turns to interest as she sees the smaller creature untroubled; she learns her own response rather than only obeying her mother. Barillaro briefed the animator with a child's playground injury and then curiosity about another child's resilience: actionable motivation, not a list of faces. Scale and feather movement helped show vulnerability. | EXPERIENCE | A03, 2017-02-16 |
| AC-02 | 379 | PROC | Give the animator the causal experience in words, for example a character who refuses to approach after being hurt and then cannot look away when someone smaller succeeds. Require separate readable poses for avoidance, noticing, evaluation and decision. Do not swap in a two-emotion-label order (scared, then happy): it drops the thought that changes the action. Stage the demonstrator and the protagonist together when the relation must read. Test silent grayscale thumbnails before paying for effects. No universal pose hold or reaction duration. | OPINION | paper, 2026-10-21 |
| AC-03 | 381 | CASE | Wanneroy (Season 1): match storyboard intent and poses; live-action reference plus keyframes, not mocap, for that production; he had to tone expression down, because head and body angles could carry intent without pushing the face. Not a guarantee about later Fortiche work. | EXPERIENCE | A07, 2021-12-08 |
| AC-04 | 383 | PROC | Acting brief, director to animator: what the character believes before the shot; the new stimulus noticed; the tactic used on another character; the visible decision; the final pose the next shot needs. Add framing and occlusion constraints. Ask for reference alternatives before polished animation. Review the pose through the real camera, not the animator's viewport. A micro-expression that vanishes at delivery resolution is not effective screen acting. | OPINION | paper, 2026-10-21 |
| AC-05 | 387-391 | LIMIT | Direct the psychological cause (no universal blink or pause duration). Match expression size to shot and style (no percentage or facial-motion threshold reported; Season 1 only). Require stimulus, decision, action in readable form (no mandated frame count). | EXPERIENCE + proposed application; EXPERIENCE; OPINION | A03, A07, paper |

## 12. Section 9: sound, music, silence, cues (FP:395-417)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SN-01 | 397 | CASE | Murch: Coppola kept music out before the restaurant killings; an offscreen elevated train becomes a rising, screeching expressive element; music is saved for afterwards. Murch hedges the train's return at about five times, so five is not a measured cue count. An example of environmental sound doing a score's job; not proof that realism must always give way. | EXPERIENCE | F12, 2020-03-15 |
| SN-02 | 399 | PROC | Cue attributes: onset, offset, narrative role, listener perspective, permitted overlap, priority against dialogue. Silence is the removal of a defined layer: no music is not zero audio. For a reveal compare advance warning, exact sync and delayed sound. Keep dialogue intelligible; decide who can hear the cue inside the story. | OPINION | paper |
| SN-03 | 401 | CASE | Barillaro brought in the composer early and iterated sound and picture together; he rejected a broadly grand orchestral beach because it would miss the heroine's intimate viewpoint. | EXPERIENCE | A03 |
| SN-04 | 403 | CASE | Arcane used temporary tracks to carry musical intent; the final track came late and sounded different but kept the intended emotion. | EXPERIENCE | A05 |
| SN-05 | 405 | CASE | Linke: open-ended scratch-voice iteration created too much material, so production set a dialogue-lock boundary for recording, with ADR possible from the previous episode. A reported pipeline trade-off, not proof that dialogue must never change. | EXPERIENCE | A08, 2025-05-23 |
| SN-06 | 407 | PROC | One cue sheet shared by director and sound designer, keyed to shot IDs and event markers: stimulus audible, character hears it, reaction begins, action lands, music enters / exits. Mark each cue locked-to-action, flexible, or pending-music. Label temporary tracks temporary; build no unapproved licensing assumptions into the release. If a replacement score moves a dramatic accent, reopen the animatic instead of keeping cuts blindly. No universal music-to-cut sync offset. | OPINION | paper, 2026-10-21 |
| SN-07 | 411-417 | LIMIT | Invite music before pictures are final (no universal lead time). Separate emotional intent from temp-track details (no BPM rule). Define a lock boundary (no reusable quota). One shared cue sheet (event times are project-specific). | EXPERIENCE x3; OPINION | A03, A05, A08, paper |

## 13. Section 10: game cinematics, identity, control (FP:421-505)

### 13.1 Player identity and authored versus player camera

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| GC-01 | 423 | CASE | Laidlaw's archived development account: Half-Life avoided third-person cinematics; its opening disaster convinced the team a major event could stay first-person; NPCs address the hero while the player supplies much of his identity. A writer's design commitments, not proof every game should use a silent hero. | EXPERIENCE | G03, original file 1998-11-09, posted 2016-10-03 |
| GC-02 | 425 | MECH | God of War's authored movement and Half-Life's player-facing events solve different problems: one keeps camera continuity unbroken while controlling the view tightly; the other keeps first-person embodiment while constraining progression. Neither shows that "no cuts" equals freedom. Pick the constraint for the scene's experience, not as a badge. | OPINION | paper |
| GC-03 | 427 | MECH | Authored camera: when a precise reveal, spatial deception or performance relation is needed and the interruption is justified. Player-directed staging: when finding or physically acting in the event is the emotional point. Hybrid: when a short authored cue can hand the meaningful action back to the player. A long camera move does not replace giving the player something consequential to do. | OPINION | paper |

### 13.2 Labels for reference material

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| GC-04 | 431 | CASE | Naughty Dog animator Jonathan Cooper separates interactive cinematics from full gameplay and from noninteractive cinematics; his 2018 article says the studio's cinematics from Uncharted 4 onward are real-time. The paper saw only indexed passages (full-page fetch timed out) and relies on it for no scene-specific implementation claim. | EXPERIENCE | G09, 2018-03-09 |
| GC-05 | 433 | CASE | Blizzard's official Dragons page calls it an animated short and announces a website premiere; it is not a shipped gameplay sequence. | VERIFIED | G10, updated 2016-05-16 |
| GC-06 | 435 | PROC | Label each reference: shipped interactive event, shipped noninteractive real-time cinematic, pre-rendered film, or marketing material. "In-engine" alone does not show the footage ran live on the target device, with the player's avatar, at shipped quality. A Blender previs render is a communication asset; it does not prove the final Roblox camera, lighting, streaming or timing. | OPINION | paper |
| GC-07 | 437 | PROC | For an avatar-centred scene, prototype in real time early to expose costume, scale, missing-animation and composition problems. For a prerecorded insert, state what is fixed and how the return to the current avatar and world stays coherent. Do not claim one render method is inherently more emotional. | OPINION | paper |

### 13.3 Skip, replay, pause, comfort, handoff

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SK-01 | 441 | CASE | Ragnarök's New Game Plus announcement offers cinematic skipping when replaying the story. It shows a skip option can coexist with that studio's cinematic style; it gives no skip rate and says nothing about first playthroughs. | VERIFIED | G06, 2023-04-05 |
| SK-02 | 443 | CASE | The official Ragnarök accessibility page separates gameplay ambient sway from cinematic smoothing; the latter reduces handheld shake and sway where possible. | VERIFIED | G07, undated living page, live-read |
| SK-03 | 445 | CASE | Naughty Dog documents cinematic descriptions and developer commentary for The Last of Us Part II Remastered. | VERIFIED | G08, 2024-01-16 |
| SK-04 | 447-457 | PROC | Five separate requirements. Skip: advance to the correct resulting story state without sitting through the performance. Replay: revisit a finished performance without repeating rewards, progression, damage or irreversible choices. Pause: stop the local viewing where technically allowed; do not pretend the shared world stopped if it did not. Comfort: offer less shake or a calmer camera while keeping the information the original move carried. Handoff: restore the expected view, movement, interface and audio state with a clear first playable action. | OPINION | paper, 2026-10-21 |
| SK-05 | 459 | PROC | A skip must not leave the player confused: keep the essential objective in a short readable form outside the skippable performance. Do not award progression only at a fragile visual cue; specify progression ownership and camera playback separately with engineering. Cinematic description, captions and readable staging belong in the directing brief, not only a late UI pass. | OPINION | paper |
| SK-06 | 461 | PROC | For repeatable boss entrances, test the return path after failure as seriously as the first entrance. A reveal's value on a repeat attempt need not equal its first value. Offer replay where affordable; do not call it a universal platform requirement without a platform source. | OPINION | paper |
| SK-07 | 465-469 | LIMIT | G06: precedent for skip on replay; no published optimal skip policy or rate. G07: a separate comfort treatment; not a Roblox implementation spec. G08: shipped / announced features; no retention uplift established. | none | G06, G07, G08 |

### 13.4 Multiplayer and mobile: proposed directing contract (FP:473-505)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| MM-00 | 475 | LIMIT | Everything in this subsection is a proposed Roblox production spec, not a report that Santa Monica or Valve use this network design. Roblox API behaviour and implementation must be checked against current Roblox documentation (the paper defers this to its implementation section, outside this part). | OPINION | paper |
| MM-01 | 479 | PROC | Audience: one player, a party or everyone present? What does a late joiner see? | OPINION | paper |
| MM-02 | 481 | PROC | World behaviour: do NPCs, hazards and timers keep running while someone watches? What prevents unfair damage? | OPINION | paper |
| MM-03 | 483 | PROC | Authority: who decides that the shared event is complete, versus one client's playback ending? | OPINION | paper |
| MM-04 | 485 | PROC | Missing assets: which actor or prop is indispensable, and what happens if it is not ready? A load failure must not leave the camera on an empty mark forever. | OPINION | paper |
| MM-05 | 487 | PROC | Skip policy: individual, unanimous, host-controlled, or fixed shared start. Show the policy; do not surprise viewers silently. | OPINION | paper |
| MM-06 | 489 | PROC | Return path: where the player is, what they face, and their first safe action after completion, skip, death, disconnect or cancellation. | OPINION | paper |
| MM-07 | 491 | PROC | Accessibility: captions, reduced motion and alternative exposition must still carry the same required information. | OPINION | paper |
| MM-08 | 493 | PROC | Identity: do differing avatar heights, accessories and costumes keep the intended gesture and focal point? | OPINION | paper |
| MM-09 | 495 | LIMIT | Do not tie group-wide narrative rewards to every viewer finishing a camera track. Do not freeze an uninvolved player because someone else triggered the scene. If some skip and others watch, stage the border between viewers and players already active. The best policy depends on the game's social contract; no universal majority-vote answer. | OPINION | paper |
| MM-10 | 499-505 | LIMIT | Camera continuity versus player agency: "no cuts" does not quantify freedom (compares G01 and G03). Label reference delivery type: no implied target-device benchmark (G09, G10). Deliberate repeat viewing: skip rate UNKNOWN (G06). Multiplayer audience and exit state: no universal voting threshold. | OPINION; OPINION; VERIFIED and OPINION; OPINION | paper, G01, G03, G06, G09, G10 |

## 14. Unknowns and numbers

### 14.1 Values the paper leaves UNKNOWN or says no source establishes

| ID | FP | What stays unestablished | Scope |
| --- | --- | --- | --- |
| U-01 | 57, 75, 87, 113, 329 | Shot duration, lens, camera height, movement speed, runtime of the analysed scenes | Scene studies 1 to 8 (unless a source gives it) |
| U-02 | 241 | Typical shot lengths per mood | Section 2 |
| U-03 | 249, 257 | m/s or degrees/s speed for fear, grandeur, sadness | Camera moves |
| U-04 | 253, 261 | Numeric speed limits; numeric shake threshold | Camera moves, comfort |
| U-05 | 281, 279 | Mandatory thirds placement; automatic penalty for a continuity break | Composition, continuity |
| U-06 | 293, 305 | Ideal Roblox intro, boss-intro or close-up length; maximum unskippable interval; cuts-per-minute; mood-to-seconds | Editing |
| U-07 | 321, 337 | Numeric threshold for preserving the choice; prescribed beat count | Short structure |
| U-08 | 329, 335 | Ideal Roblox cutscene length; standard skip rate; phone-viewer attention limit; duration-retention causal link | Roblox cutscenes |
| U-09 | 357, 359 | Universal lighting ratio or brightness; RGB values (project decisions) | Light |
| U-10 | 379, 387, 389, 391 | Pose hold, reaction, blink or pause duration; percentage or facial-motion threshold; frame count | Acting |
| U-11 | 407, 411, 413, 415 | Music-to-cut sync offset; music lead time; BPM rule; dialogue-lock quota | Sound |
| U-12 | 441, 465, 503 | Skip rate; optimal skip policy | Skip |
| U-13 | 469 | Retention uplift from described / commentated cinematics | G08 |
| U-14 | 501, 505 | Target-device benchmark; universal voting threshold | Reference labels, multiplayer |

### 14.2 Numbers that appear

| ID | FP | Number | Scope and paper's limit | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| N-01 | 19, 51 | 15 rules | All OPINION, 2026-10-21 | OPINION | paper |
| N-02 | 55 | 8 principal cases; 3 film cases | Evidence scopes differ; not shot-by-shot logs | OPINION | paper |
| N-03 | 59, 77, 91 | Film years 1975, 1961, 1987 | Release dates, distinct from source dates (FP:57) | none | - |
| N-04 | 93, 95-111 | 14 beats in the source account; 9 listed | Condensed; durations UNKNOWN | EXPERIENCE | F03 |
| N-05 | 65 | 180-degree pan | A camera rotation inside one take, not an axis violation | EXPERIENCE | F01 |
| N-06 | 127, 317 | Six minutes covering twelve years | Whole film, not one scene; not a Roblox target | EXPERIENCE | A01 |
| N-07 | 135 | Twos (characters), ones (camera) | Practitioner testimony; no frame count | EXPERIENCE | A04 |
| N-08 | 215 | 90 seconds (Raiders take) | The only reported figure; internal timings absent | EXPERIENCE and analyst observation | F04, 2014-05-06 |
| N-09 | 227, 239 | 40 mm mostly; 35 mm in the bunker; 47 mm some river shots; Alexa Mini LF / Signature Primes | 1917 production examples; filmback must accompany | EXPERIENCE | F06 |
| N-10 | 247, 259 | 50-foot Technocrane; 20-foot crane on a vehicle | 1917 production path; not mood presets | EXPERIENCE | F06 |
| N-11 | 287, 301 | 51% for emotion | A priority, not measured contribution | EXPERIENCE | F09, 2020-02-10 |
| N-12 | 311, 319 | One second per day | An experiment, not a finished shot length | EXPERIENCE | A02 |
| N-13 | 313 | Six verbs in the causal chain | Diagnostic, not a mandatory six-beat formula | OPINION | paper |
| N-14 | 347, 355 | At least one colorscript vignette per sequence | Fortiche's reported process; no colour values | EXPERIENCE | A05 |
| N-15 | 397 | About five train returns | Hedged recollection; not a measured count | EXPERIENCE | F12 |
| N-16 | 423 | 1998-11-09 (original file); 2016-10-03 (posted) | No register anchor for the 1998 date (X-40) | EXPERIENCE | G03 |
| N-17 | 431 | Uncharted 4 onward = real-time cinematics | Indexed passages only | EXPERIENCE | G09, 2018-03-09 |
| N-18 | 447-457, 479-493 | 5 requirements; 8 contract items | Organizing labels, not facts | OPINION | paper |

## 15. Source ids used in lines 1-507 (resolved from FP:1205-1527)

Quotes are the register's own, 15 words or fewer, one per source; a few are shortened to a continuous part. "Cited at" = lines inside 1-507. Not cited in this part: F07 (Adobe shot types), A09, A10.

| ID | Source, date and the paper's scope note | URL | Cited at FP | Reg. FP | Key quote (register) |
| --- | --- | --- | --- | --- | --- |
| F01 | Singleton, "In the Mouth of Jaws", DGA Quarterly; Spring 2006, page adds 2025 anniversary intro. EXPERIENCE. Screening commentary; text inspected, footage not. | https://www.dga.org/craft/dgaq/issues/0601-spring-2006/screening-room-john-singelton | 61 | 1209 | "Moving the camera for the sake of moving the story forward." |
| F02 | Aronofsky, "Sword of Doom", DGA; Fall 2006. EXPERIENCE. Screening commentary on Yojimbo. | https://www.dga.org/craft/dgaq/issues/0603-fall-2006/screening-room-darren-aronofsky | 79 | 1219 | "I think every film has its own grammar" |
| F03 | Lyne, "Girl Crazy", DGA; Spring 2010. EXPERIENCE. 14 illustrated beats; lens and frame-rate memories qualified. | https://www.dga.org/craft/dgaq/issues/1001-spring-2010/shot-remember-fatal-attraction | 93 | 1229 | "There has to be a beat where you get the geography." |
| F04 | Every Frame a Painting, "The Spielberg Oner"; 2014-05-06. Register mark OPINION. Footage not timed; internal order incomplete; subtitle mirror read. | https://www.youtube.com/watch?v=8q4X2vDRfRk | 215 | 1239 | "This is a single unbroken, 90-second take." |
| F05 | Cambridge in Colour, "Understanding Camera Lenses"; undated, acc 2026-10-21, live-read. VERIFIED. Position-driven perspective vs focal length. | https://www.cambridgeincolour.com/tutorials/camera-lenses.htm | 225, 237 | 1249 | "perspective only changes with one's location relative to their subject" |
| F06 | Deakins on 1917, British Cinematographer; undated, interview discusses 2020 awards season, acc 2026-10-21, live-read. EXPERIENCE. Publication date not verified. | https://britishcinematographer.co.uk/exclusive-interview-roger-deakins-cbe-bsc-asc-on-1917-bc97/ | 227, 239, 247, 259, 343 | 1259 | "shot almost everything on a 40mm" |
| F08 | Adobe, "180-degree rule"; undated, acc 2026-10-21, live-read. VERIFIED. A convention with exceptions; not audience research. | https://www.adobe.com/uk/creativecloud/video/discover/what-is-the-180-degree-rule.html | 267, 277 | 1279 | "there are times when it can be bent or broken." |
| F09 | Hullfish interviews Murch, ProVideo Coalition; 2020-02-10. EXPERIENCE. Priorities explicitly nonempirical; gaze; interview read, not whole books. | https://www.provideocoalition.com/aotc-murch-books/ | 267, 279, 287, 301 | 1289 | "I had to make the numbers jump around to achieve that effect!" |
| F10 | Adobe Premiere, J cuts and L cuts; updated 2025-08-22. VERIFIED. Definitions only. | https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/perform-j-cuts-and-l-cuts.html | 289, 303 | 1299 | "Both are a type of split edit" |
| F11 | Mulcahey interviews Deakins, Filmmaker Magazine; 2017-09-14. EXPERIENCE. Blade Runner 2049 on-set colour methods. | https://filmmakermagazine.com/103272-the-color-of-the-future/ | 343 | 1309 | "I did a lot of tests in preproduction to find the right gels." |
| F12 | Hullfish, Murch on seven films, ProVideo Coalition; 2020-03-15. EXPERIENCE. Godfather train sound, approximate recurrence, music timing. | https://www.provideocoalition.com/aotc-murch-films/ | 397 | 1319 | "Francis wanted to hold any music off until after the murder." |
| A01 | AWN, chat with Kristina Reed on Feast; 2014-11-13. EXPERIENCE. Direct producer interview; footage not timed. | https://www.awn.com/animationworld/chat-kristina-reed-creating-winston-and-disney-s-feast | 117, 317 | 1329 | "you see the face, we unlock the camera" |
| A02 | Skwigly, Feast creators interview; 2014-09-08. EXPERIENCE. Not finished-film shot timings. | https://www.skwigly.co.uk/disney-feast/ | 129, 311, 319 | 1339 | "the camera represents the movie's 'magic'" |
| A03 | AwardsDaily, Barillaro on Piper; 2017-02-16. EXPERIENCE. Not a full shot log. | https://www.awardsdaily.com/2017/02/16/interview-short-film-animated-director-alan-barillaro-piper/ | 367, 387, 401, 411 | 1349 | "Music can tell a story as well" |
| A04 | Wired video, "How Animators Created the Spider-Verse"; 2019-03-22. EXPERIENCE. Transcript read; footage not measured. | https://www.wired.com/video/watch/how-animators-created-the-spider-verse | 135 | 1359 | "They start more out of sync" |
| A05 | Cartoon Brew, Maunoury on an Arcane sequence; 2024-12-30. EXPERIENCE. Text read; ordered parts are not a full cut order. | https://www.cartoonbrew.com/series-craft/series-craft-director-barth-maunoury-breaks-down-an-emotional-arcane-sequence-244539.html | 347, 355, 403, 413 | 1369 | "as if Isha had drawn her memories" |
| A06 | SYFY Wire, DeBlois on Deakins and Dragon finale; 2020-01-08. EXPERIENCE. The quote is DeBlois quoting Deakins, not a Deakins interview. | https://www.syfy.com/syfy-wire/awards-contenders-legend-roger-deakins-played-a-huge-role-in-the-how-to-train-your-dragon | 349, 357 | 1379 | "Whose perspective are you following?" |
| A07 | SyncSketch blog (vendor host), Wanneroy on Arcane; 2021-12-08. EXPERIENCE. Season 1 workflow, not universal. | https://blog.syncsketch.com/creator-stories/arcane-fortiche/ | 381, 389 | 1389 | "instead of reinventing each shot" |
| A08 | Cartoon Brew, Netflix-sponsored Arcane Q&A; 2025-05-23. EXPERIENCE. Article read; video not watched. | https://www.cartoonbrew.com/presented-by-netflix/netflixs-arcane-creative-team-in-conversation-with-cartoon-brew-exclusive-video-247375.html | 405, 415 | 1399 | "until animation lock" |
| G01 | PlayStation Blog, 3 key God of War scenes; 2018-09-28. EXPERIENCE. Ordered framing and lighting; not a measured edit log. | https://blog.playstation.com/archive/2018/09/28/3-key-scenes-from-god-of-war-that-helped-define-its-incredible-cinematic-style | 141, 159, 205, 499 | 1429 | "The door 'wipes the shot,' revealing a body on the table." |
| G02 | PlayStation Blog, first boss behind the scenes; 2018-08-16. EXPERIENCE. Staging and playable phases. | https://blog.playstation.com/2018/08/16/fighting-a-god-behind-the-scenes-of-god-of-wars-first-boss-battle/ | 165, 179, 181, 207 | 1439 | "We needed the intro to move you from the front of the house" |
| G03 | Marc Laidlaw, "Writing For Half-Life"; 2016-10-03 (register). EXPERIENCE. Author-hosted recovered account; the linear-narrative claim is personal belief. | https://www.marclaidlaw.com/writing-half-life/ | 423, 499 | 1449 | "So we went first person all the way." |
| G04 | Combine OverWiki, Alyx developer commentary; 2020-11-12 (commentary release; mirror date not established). EXPERIENCE, secondary-hosted primary transcript. Commentators named in the register: Reidford (Citadel Vista), Emond (Greenhouse), Shaw (Strider), Rodkin (Refuge). Not checked against audio. | https://combineoverwiki.net/wiki/Developer_commentary/Half-Life:_Alyx | 187, 197, 199, 209 | 1459 | "This avoided the distraction problems" |
| G05 | Steam announcement, "Commentary Update"; 2020-11-12. VERIFIED. Confirms release, not every mirrored sentence. | https://steamcommunity.com/games/546560/announcements/detail/2795003923897250614 | 187, 209 | 1469 | "Developer Commentary Now Available in Half-Life: Alyx" |
| G06 | PlayStation Blog, Ragnarök NG+; 2023-04-05. VERIFIED. Skip feature only. | https://blog.playstation.com/2023/04/05/god-of-war-ragnarok-new-game-plus-is-available-now/ | 441, 465, 503 | 1479 | "the option to skip cinematics in NG+" |
| G07 | PlayStation, Ragnarök accessibility; undated living page, live-read. VERIFIED. | https://www.playstation.com/en-us/games/god-of-war-ragnarok/accessibility/ | 261, 443, 467 | 1489 | "Smooth out camera movement to reduce shake and sway" |
| G08 | Naughty Dog blog, TLOU Part II Remastered features; 2024-01-16. VERIFIED. No performance or retention claims. | https://www.naughtydog.com/blog/the_last_of_us_part_2_remastered_features_launch | 445, 469 | 1499 | "Speech to Vibrations and Cinematic Descriptions" |
| G09 | GameAnim, Cooper on Uncharted 4; 2018-03-09. EXPERIENCE. Indexed passages only; full page timed out. | https://www.gameanim.com/2018/03/09/interactive-cinematics-in-uncharted-4/ | 431, 501 | 1509 | "all cinematics from Uncharted 4 onwards are real-time in-game" |
| G10 | Blizzard news, "Animated Short Incoming: Dragons"; updated 2016-05-16. VERIFIED. Not evidence of an in-game cinematic. | https://news.blizzard.com/en-us/article/20122126/animated-short-incoming-dragons | 433, 501 | 1519 | "our third animated short: Dragons" |

## 16. Claims for the fact-check

Priority (studio rule): P1 = Roblox, engine or platform behaviour, or anything dated after 2026-06-01; P2 = a named practitioner's quote, date or production fact the skills may repeat; P3 = background. By that rule lines 1-507 hold no dated-after-2026-06-01 source and make no Roblox claim; the single P1 row is a pointer to what this part does NOT establish. Check each row against its source at the id, not against the paper. "live" = re-read the page.

| ID | Claim (paraphrase) | FP | Pri | Check against | Src date | Live | Why it matters |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FC-01 | Not a claim: any Roblox behaviour (late joiners, per-client camera, loading failure, skip sync) that skills derive from the contract MM-01 to MM-09 is unsupported by this part. The paper defers it to docs. | 475 | P1 | `knowledge/external/roblox-creator-docs/` and `knowledge/reference/roblox/whats-new.md` | n/a | n/a | Stops the contract from reading as Roblox fact |
| FC-02 | Fixed position: focal length changes angle of view / magnification, not perspective; same subject size across focal lengths needs a position change | 225 | P2 | F05 page and a second optics source | undated | live | Engine FOV advice will repeat it |
| FC-03 | 1917: Alexa Mini LF / Signature Primes; mostly 40 mm, 35 mm bunker, some river at 47 mm | 227, 239 | P2 | F06 interview text; publication date still unverified | undated | live | Numbers skills may quote |
| FC-04 | 1917 run: 50-foot Technocrane, 20-foot vehicle crane, rehearsed transitions | 247, 259 | P2 | F06 | undated | live | Production fact |
| FC-05 | Raiders take is reported as one unbroken 90-second take | 215 | P2 | F04 video; paper marks it EXPERIENCE in table but OPINION in register (X-30) | 2014-05-06 | no | Number plus tag conflict |
| FC-06 | Murch ranks emotion, story, rhythm above continuity; 51% for emotion is a priority, not a measurement; interview allows continuity sacrifice; gaze check | 267, 287, 301 | P2 | F09 interview text | 2020-02-10 | no | Frequently over-read |
| FC-07 | J cut = incoming audio before picture; L cut = outgoing audio over incoming picture | 289 | P2 | F10 | updated 2025-08-22 | live | Definition skills will state |
| FC-08 | 180-degree system keeps coverage on one side of the axis; bendable | 267, 277 | P2 | F08 | undated | live | Convention wording |
| FC-09 | Blade Runner 2049 desert colour via filtration, gels, gelled windows; 1917 flares and burning-church light, scale model | 343 | P2 | F11 (2017-09-14), F06 | 2017-09-14; undated | F06 live | Production facts |
| FC-10 | Godfather: music withheld until after the murders; train sound; about five returns | 397 | P2 | F12 | 2020-03-15 | no | Hedged count |
| FC-11 | Jaws discovery shot order (6 steps) incl. reported 180 pan and music change before the discovery | 63-73 | P2 | F01 text; the paper did not inspect footage | 2006; 2025 intro | no | Order is the lesson |
| FC-12 | Yojimbo eye, padlock, trunk order; Aronofsky's repeated-framing reading | 81-89 | P2 | F02 | 2006 | no | Reading is the commentator's |
| FC-13 | Fatal Attraction: nine listed items drawn from the 14-beat account; music at the reveal; no music before the resurgence | 95-111 | P2 | F03 | 2010 | no | Order and music timing |
| FC-14 | Feast: beat order, discarded storyboard cut and dialogue, six minutes / twelve years | 117-127 | P2 | A01 | 2014-11-13 | no | Reed's scope |
| FC-15 | Feast: light as food preference; camera held back until warranted; dinner list; one second per day | 129, 311 | P2 | A02 | 2014-09-08 | no | Experiment vs shot length |
| FC-16 | Spider-Verse: out-of-sync then coordinated; characters on twos, camera on ones | 135 | P2 | A04 transcript | 2019-03-22 | no | Frame-rate claim |
| FC-17 | God of War mother's knife: eight beats and cold / warm light assignments; continuous camera | 141-159 | P2 | G01 (Arazi) | 2018-09-28 | no | Light assignment is local |
| FC-18 | God of War first boss: six phases; spin / impact hides staging; closer camera and destruction sell threat | 165-181 | P2 | G02 (Yeh) | 2018-08-16 | no | Handoff example |
| FC-19 | Alyx: four-beat order; call moved because objects distracted; commentary released 2020-11-12 | 187-199 | P2 | G04 against game audio or the in-game commentary; G05 for the release | 2020-11-12 | no | Mirror unverified by the paper |
| FC-20 | Piper: fear to interest beats; playground-injury brief; composer brought in early; no grand orchestra | 367-377, 401 | P2 | A03 (the paper's text at FP:401 names the composer; check the name) | 2017-02-16 | no | Brief shape source |
| FC-21 | Arcane: at least one colorscript vignette per sequence; temp tracks; late final track | 347, 403 | P2 | A05 | 2024-12-30 | no | Process claims |
| FC-22 | Dragon finale: Deakins linked boards, layout, lighting; dawn across courtship shots; DeBlois objected to early composition lock | 349 | P2 | A06 (quote is DeBlois quoting Deakins) | 2020-01-08 | no | Second-hand attribution |
| FC-23 | Arcane S1: live-action reference plus keyframes, no mocap; reduce face expression | 381 | P2 | A07 (vendor-hosted) | 2021-12-08 | no | Season 1 only |
| FC-24 | Arcane: dialogue lock for recording; previous-episode ADR possible | 405 | P2 | A08 (Netflix-sponsored; paper did not watch the video) | 2025-05-23 | no | Sponsored source |
| FC-25 | Laidlaw: Half-Life avoided third-person cinematics; opening disaster kept first-person; dates 1998-11-09 / 2016-10-03 | 423 | P2 | G03 page | 2016-10-03 | no | 1998 date has no register anchor |
| FC-26 | Cooper: interactive cinematics distinguished; Uncharted 4 onward cinematics real-time | 431 | P2 | G09 full page (the paper had only indexed passages) | 2018-03-09 | no | Paper's own gap |
| FC-27 | Blizzard calls Dragons an animated short with a website premiere | 433 | P2 | G10 | updated 2016-05-16 | no | Label example |
| FC-28 | Ragnarök NG+ offers cinematic skip on replay | 441 | P2 | G06 | 2023-04-05 | no | Skip precedent |
| FC-29 | Ragnarök accessibility page: cinematic camera smoothing reduces handheld shake and sway; separate from gameplay sway | 261, 443 | P2 | G07 | undated | live | Comfort precedent |
| FC-30 | TLOU Part II Remastered documents cinematic descriptions and developer commentary | 445 | P2 | G08 | 2024-01-16 | no | Feature fact |

## 17. Contradictions and limits

### 17.1 Limits the paper states

| ID | FP | Limit | Handling for skills |
| --- | --- | --- | --- |
| X-01 | 13 | VERIFIED marks documentation, not that an artistic recommendation is proven. | Write "documented", not "proven". |
| X-02 | 17, 57 | UNKNOWN is not zero or a default. Scene lists are not edit lists; no timing, lens, height or speed unless stated. | Keep UNKNOWN as UNKNOWN in every skill. |
| X-03 | 55 | Only three of the eight principal cases rebuild published shot order; the rest are beats or reframings. | Do not present all eight as shot logs. |
| X-04 | 65 | The reported 180-degree pan is camera rotation, not an axis violation. | Do not cite Jaws as an axis break. |
| X-05 | 87, 89 | The Yojimbo third image is not confirmed as literal POV; the repeated-framing reading is Aronofsky's. | Attribute, do not assert. |
| X-06 | 113 | Lyne's recalled lens and frame rate are uncertain. | No specs from F03. |
| X-07 | 127 | Six minutes / twelve years is the whole film. | Never present as scene length. |
| X-08 | 135, 137 | Twos / ones is testimony, not a frame count; cannot justify a lower game frame rate. | Do not copy the frame-rate split. |
| X-09 | 141, 165, 187 | God of War items are real-time scene accounts, not frame logs; Alyx is an interactive sequence via a mirror not checked against audio. | Name the access scope when citing. |
| X-10 | 161, 205 | Warm / cold light roles are local to that scene; G01 gives no colour psychology. | No colour rules from this. |
| X-11 | 201 | VR staging does not transfer unchanged to phones. | Playtest on phone. |
| X-12 | 225, 231 | Perspective is not lens distortion; no angle or lens guarantees an emotion. | Keep every effect conditional. |
| X-13 | 227 | The 1917 millimetres are production examples; filmback must accompany. | Never state "40 mm feels X". |
| X-14 | 247, 259 | Crane gear is not a mood preset. | No equipment-to-emotion tables. |
| X-15 | 287 | The 51% is a priority, not a measure. | No numeric emotion scoring. |
| X-16 | 289 | J / L cut gives no overlap length. | No default overlap seconds. |
| X-17 | 293, 329 | No ideal intro, boss-intro, cutscene length, skip rate or attention limit is established; a bounded gap, not proof none exists. | Say "not established here". |
| X-18 | 311 | The one-second-per-day idea was an experiment. | Not a shot length. |
| X-19 | 331 | Laidlaw's linear-narrative preference is attributed opinion. | Attribute. |
| X-20 | 345 | "Red = anger, blue = sadness" is not supported. | Colour is a project convention. |
| X-21 | 349, 1387 | The A06 key quote is DeBlois quoting Deakins (register scope). | Do not call it a Deakins interview. |
| X-22 | 381 | A07 is Season 1 testimony via a vendor-hosted page. | Do not generalize to later productions. |
| X-23 | 397 | Five train returns is a hedged recollection. | Not a cue-count rule. |
| X-24 | 405 | A08 is a Netflix-sponsored Q&A report, the video not watched; a trade-off, not proof dialogue never changes. | Label sponsored. |
| X-25 | 423, 431, 433 | G03 is a writer's choices; G09 relied on indexed passages only; G10 is a short, not gameplay. | Label the delivery type (GC-06). |
| X-26 | 441, 443, 445 | G06 gives no skip rate or first-playthrough behaviour; G07 is not a Roblox spec; G08 has no retention claim. | Do not infer player behaviour. |
| X-27 | 461 | Replay is not a universal platform requirement without a platform source. | Offer as option. |
| X-28 | 475 | The multiplayer contract is not anyone's reported architecture; Roblox behaviour is to be checked in docs. | See FC-01. |
| X-29 | 495 | No universal majority-vote answer. | Pick per social contract. |

### 17.2 Gaps and tensions found by the extractor (not stated by the paper)

| ID | FP | Item | Handling for skills |
| --- | --- | --- | --- |
| X-30 | 215, 1241 | F04 is tagged "EXPERIENCE and analyst observation" in the section-1 table but OPINION in the register. | Use the weaker mark until resolved. |
| X-31 | 187 | The Alyx tag mixes marks (EXPERIENCE for the transcript, VERIFIED for the release notice). | Keep both; VERIFIED covers only the release. |
| X-32 | 473 | The subsection title promises "mobile", but the eight contract items contain no mobile-specific item. Phone claims are scattered: legibility (161), VR vs phone (201), still vs moving phone-size frame (271), phone attention UNKNOWN (329), grayscale thumbnails (379), delivery resolution (383), target-device captures (351). None is measured. | Treat mobile as an open test, not a finding. |
| X-33 | 47, 447-457, 489 | Rule 14 lists "interruption" as an ending, but the five requirements are skip, replay, pause, comfort, handoff. Interruption appears only inside the return-path item (death, disconnect, cancellation). | Define interruption as its own test; my reading, not the paper's. |
| X-34 | 41, 43 | Rules 11 and 12 have no body in lines 1-507; only a pipeline mention (5) and a previs limit (435). | Do not build skill text for them from this note. |
| X-35 | 95-111 | Nine list items stand for a 14-beat source account. | The 14 cannot be ticked off from the paper. |
| X-36 | 55 | The paper does not name the "three film cases"; I read them as Jaws, Yojimbo, Fatal Attraction (the three DGA-sourced studies). | Verify before stating. |
| X-37 | 365 | Piper is a supporting study under section 8, not one of the eight principal cases; the Arcane supporting study is outside this part. | Keep the two classes apart. |
| X-38 | 261 | A section-3 table row cites G07 (a console game's accessibility page) for "calmer treatment"; G07 is first described in section 10. | Cross-reference SK-02. |
| X-39 | 1181 | The paper's own caution about the Adobe shots page (F07) sits outside this part; section 2 cites F05 for geometry and F07 is not used here. | Do not import lens-number presets. |
| X-40 | 423, 1451 | G03's "original file 1998-11-09" appears only in the paper text; the register gives 2016-10-03 only. | Check the date on the page. |
| X-41 | 279 | The F09 row says "no automatic penalty score" for a continuity sacrifice; the register scope says Murch weights are explicitly nonempirical. The two fit, but the paper never gives the other priority weights. | Use only 51% as stated. |

## 18. Line coverage

Every text line from 1 to 507 is covered by at least one row. Headings and table header rows are not turned into rows.

| FP | Rows |
| --- | --- |
| 1-17, 51 | EM-01 to EM-07 |
| 19-49 | RU-01 to RU-15 |
| 53-57 | SC-00, SC-01 |
| 59-75 | SC1-1, SC1-2 |
| 77-89 | SC2-1 to SC2-3 |
| 91-113 | SC3-1, SC3-2 |
| 115-131 | SC4-1 to SC4-4 |
| 133-137 | SC5-1, SC5-2 |
| 139-161 | SC6-1 to SC6-3 |
| 163-183 | SC7-1 to SC7-4 |
| 185-201 | SC8-1 to SC8-4 |
| 203-219 | SC-02 to SC-06 |
| 223-241 | SH-01 to SH-08 |
| 245-261 | MV-01 to MV-05 |
| 265-281 | ST-01 to ST-06 |
| 285-305 | ED-01 to ED-07 |
| 309-337 | SU-01 to SU-08 |
| 341-359 | LC-01 to LC-06 |
| 363-391 | AC-01 to AC-05 |
| 395-417 | SN-01 to SN-07 |
| 421-445 | GC-01 to GC-07, SK-01 to SK-03 |
| 447-469 | SK-04 to SK-07 |
| 473-505 | MM-00 to MM-10 |
