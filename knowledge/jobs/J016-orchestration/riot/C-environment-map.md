---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J016 transcript extraction (R02 environment art, R09 map design, R13 TFT environment); owner-supplied Riot transcripts in Downloads, not in git"
supersedes: []
---
> Author: research reader · claude-opus-5-5 · default · 2026-10-21 (J016 transcript extraction; lead spot-read)
# Riot transcripts C: environment art, map design, TFT environment asset

> Author: research reader · claude-opus-5-5 · default · 2026-10-21. Source transcripts are data; every point below is paraphrased with file:line.

**File key** (all in `C:\Users\Firew\Downloads\`):

| Key | File | Lines |
| --- | --- | --- |
| E2 | `Designing Envirnmental art ep 2.txt` | 996 |
| V9 | `Map design in valorant ep9.txt` | 1162 |
| Z13 | `riot artist design zilean forgotten shrine for tft ep13.txt` | 1064 |

Caveat for all three: they are demos, not shipped work. E2 is a personal piece unrelated to any game (E2:18). V9's lava site "would never ship" and is compressed from months into about an hour (V9:28-32, 68-70, 82-84). Z13 is not shipping, and its sketches and 3D scene were prepared in advance because the real process takes days (Z13:40-48, 444-446, 1046-1048). The process shown is real; the timing is not.

---

## 1. Speaker, role, team, what the episode covers

**E2.** Nate Rogers, senior environment artist, about 7 years at Riot (E2:14). He worked on the Summoner's Rift remake (Baron Pit pillars, done with another artist who did the ground plane) and was the primary environment texture artist on VALORANT for about 4.5 years, doing about 80% of its environment textures (E2:16, 40-46). He created the hidden "Tactibear" mascot (E2:46-48, 368-388). The episode: he hand-paints a premade low-poly fox statue on a pedestal with grass in 3D Coat and Photoshop, using Summoner's Rift techniques (E2:18-26, 52-54). Along the way he covers value hierarchy, detail clumping, scale cues, camera-distance budgeting, colour blindness and how environment art works with design and sound (E2:204-216, 396-412, 454-518, 806-836). He describes the job as wearing many hats: hand-painted and PBR texturing, plus world building, meaning taking "blank canvases" from design and telling stories in them (E2:28-40).

**V9.** Two people from the VALORANT maps team, which has 3D artists, concept artists, designers and producers (V9:6-8). Michelle is a 3D environment artist: Sunset bombsites, Abyss mid, owned a bombsite on a new map from start to finish (V9:6, 214-228). Diego is a game designer in the level-design subgroup. He used to be a modes designer (shipped TDM), did B-site updates on Sunset and Ascent, and did collision work on Corrode (V9:8, 208-214, 228-234). The episode: Diego greyboxes a bombsite in the Abyss theme with a made-up lava-pit hook, playtests it and hands it to Michelle. She then does references, composition, shells, textures, set dressing and borrowed VFX, checking with him at each step (V9:10-34, 1142-1156).

**Z13.** Phillip Zhang, Principal Environment Artist on Teamfight Tactics. About 6 years at Riot, starting on League (Earth Dragon rocks), and 12 years of hand-painted texturing (Z13:17, 137-146, 706-707). The episode takes one environment prop from concept sketches to a finished in-game 3D asset: a forgotten Zilean shrine buried in sand, for the Set 17 "Space Gods" theme (Z13:17-30). Tools: Photoshop for 2D, Maya for models, 3D Coat for texture painting (Z13:79-81). It covers choosing a sketch, painting the concept, projecting it onto the 3D model, painting the texture, a mid-production art review, the three production gates and the visual hierarchy (Z13:32-74, 663-697, 749-790, 806-856).

**Combined.** Two hand-painted environment artists (E2, Z13) and a level-designer plus 3D-artist pair (V9). E2 and Z13 show one artist working on one asset. V9 is the only one that shows two disciplines handing work back and forth live.

---

## 2. What great work looks like: checkable signs

**E2**
- **Gameplay first.** He calls gameplay "king" (E2:830). The best-looking art can still hurt play, so the artist has to hold back (E2:432-438). The team will accept work that makes their own piece look worse if the game gets better (E2:832-836).
- **Value ladder.** VFX get the brightest whites, characters the next range, and the environment is clamped to a limited value range so characters and VFX stand out (E2:806-818). This is a hard rule he checks all the time; going to black is a red flag (E2:818-822).
- **Reserved colours.** Design uses red for enemies, so environment red is used with care (E2:204-208).
- **Focal point by value.** All values lead to the subject, the highest value sits on its head, and the grass and pedestal stay secondary (E2:952-962). Lighter colours pull the eye to the centre (E2:76-80). A late gradient overlay makes the fox read "like a beam of light", even though it mutes other detail (E2:840-858).
- **Detail clumping.** Put detail in a few spots and leave "areas of rest" elsewhere so the eye moves (E2:428-430, 490-500). Moss goes only in chosen spots: "if everything is special, then nothing is special" (E2:774-778). Grass is soft clumps, not every blade (E2:422-430).
- **Scale cues.** Boxes and other player-sized objects tell the player how big things are. A standard reference figure ("refman") is placed next to work, and areas are walked in-engine to check scale (E2:502-518). Grass works as a scale cue for the statue (E2:514-518, 986-990).
- **Story and lived-in.** Statues are storytelling: Summoner's Rift has owls and stags as team identities, and a tablet shows five glyphs against five (E2:164-174, 274-278). Cracks show wear (E2:412-414). Without lived-in elements a space is not believable and players lose the sense of being there (E2:730-740).
- **One light source.** Light comes from the top down, which gives physicality and orientation (E2:130-134). Never change the light source mid-work (E2:748-756). On Summoner's Rift one baked light pass was the "North Star" (E2:756-760).
- **Forms and edges.** Edges are reinforced so forms do not look mushy, but not every edge is highlighted, because that looks fake (E2:566-580). Crack widths vary; a single width looks man-made (E2:672-674).
- **Colour variation.** Avoid monochrome: shift hue and value slightly, add cool colours in green shadows (E2:86-96, 444-452).
- **Style match.** Summoner's Rift is "grimsey" (grim plus whimsical), with knife-sharp shape language (E2:872-878). The statue is stylised, hinting at the animal rather than copying it (E2:222-228). New work stays within the scope of the rest of the environment (E2:948-950).
- **Detail budget from camera and speed.** If players run past fast, only the big picture matters (E2:396-402). On Summoner's Rift the camera is far back and fixed, so close detail and the backs of meshes do not matter (E2:402-412). At game distance, blurry detail reads as sharp (E2:786-790). His rule: look at it and add detail only where players will see it (E2:964-972).
- **Performance.** One 1024 texture for statue plus pedestal and one for the grass, keeping texel density even (E2:778-784).

**V9**
- **The map is a chess board.** Players should not notice it except at a few planned key moments; map mechanics stay in the background (V9:40-52).
- **Art serves play.** The art must look great and play great (V9:72-76). Bombsites carry the most intense play, so readability matters most there (V9:56-58).
- **No red, no fast motion.** Both are avoided because they distract (V9:60-62). Red is the default enemy outline and the colour of many abilities, so the environment stays neutral (V9:820-828). Corrode's brick runs from neutral beige at the bottom to saturated orange higher up, so enemies on the ground read cleanly (V9:828-834).
- **Controlled palette.** Environment materials sit in a set saturation and value range so player-related things are seen first (V9:628-636).
- **The site reads on first view.** Players should know where to smoke, plant and play after the plant (V9:438-442). Options to take the space (V9:452-454).
- **Layout.** Fixed orientation (attackers always have B on the left, A on the right) plus in-world pointers such as a worn parking sign where only the A survives (V9:136-154). Layouts face forward with no doubling back (V9:184-190) and stay simple, so fights come fast (V9:196-200). Maps are flat, with elevation only in specific spots and short ramps, because crosshair placement matters (V9:282-298). Each site has two entrances for each side (V9:482-496). "Cubes" are predictable, so players lose to the opponent, not the map (V9:498-508). Neutral space must not be too easy for one side (V9:508-514). Verticality must be intentional, since a surprise flick angle gets players killed (V9:1024-1046).
- **Landmarks and markers.** The focal tower was made taller because height matters most (V9:596-604). Site markers go outside the site, with a big one on the tower, the main thing attackers see on approach (V9:1082-1090). The bombsite floor gets a trim highlight (V9:702-706).
- **Guiding the eye.** Head-height indicators (trim lines, crates) help players aim (V9:638-648). Downward-flowing patterns point to where defenders come from (V9:648-654).
- **Areas of rest and detail.** The player space stays readable while detail guides the eye upward (V9:946-952). Floors stay readable for traps (V9:940-944).
- **Story in the space.** A lived-in place, such as leaves under trees (V9:456-474). If they made it for real, Michelle would show the lava's source and structure to explain why it is there (V9:1134-1142).
- **Lighting.** Baked static lighting, chosen for performance and for shadow control, because shadows affect readability (V9:662-666).
- **Clean geometry.** Clean collision and topology, because bullet penetration depends on clean meshes (V9:228-234, 894-900).

**Z13**
- **Recognisable in the first second.** He chose the "safe" sketch because players instantly read it as Zilean. The more unique shape could have been another champion's item (Z13:48-74).
- **Theme fit.** The sci-fi sketch was rejected as off-theme for whimsical space gods (Z13:52-54).
- **Hierarchy.** UI and VFX matter most, characters second, and the environment is the backdrop (Z13:131-135). The value and colour range per layer: environment avoids the darkest darks and lightest lights, characters get a bit more range, and UI and VFX can use full black to white (Z13:749-790). He credits his art director with stressing visual hierarchy (Z13:750).
- **Shape rules.** Contrast big, medium and small shapes, and avoid "half and half" shapes of equal size that compete (Z13:221-247, 945-959). Shape flow: lines and secondary shapes point at the focal point, at several levels (Z13:273-289, 321-329). Keep shapes and colours to the minimum (Z13:961-980).
- **Value before colour.** Check the value structure in greyscale; flashy highlights do not hold up without it (Z13:424-438).
- **Finish from edges.** Sharp edges read as polish, not added detail (Z13:495-517), balanced with soft edges (Z13:640-646). Small details are an illusion when zoomed out (Z13:309-319).
- **Scale cue.** A small element such as plants shows player scale and makes the focal point look bigger (Z13:388-404). Plants are backdrop: simple texture, strong gesture that reads in peripheral vision (Z13:404-420).
- **Story.** Centuries-chipped rocks, possible fossils, crystals in the sand to show "not Earth" (Z13:360-386). Treat the prop as a character with a personality, here a rigid old time-mage (Z13:927-945).
- **Colour.** Shadows are not just a darker local colour; TFT is proudly colourful (Z13:111-116). Cool sunlight and warm, juicy shadows (Z13:646-660).
- **Camera and performance.** The fixed camera allows "smoke and mirrors", such as painting over clipping edges (Z13:622-639). Low topology and small textures, because many players are on phones (Z13:628-633, 792-803).

**Combined: checkable signs all three agree on**

| Sign | Check | Evidence |
| --- | --- | --- |
| Environment is the lowest layer of the value and colour ladder | Environment values stay inside a clamped band; VFX and UI keep the extremes | E2:806-818; Z13:749-790; V9:628-636 |
| Gameplay colours are reserved | No enemy or danger colour (red there) used freely in the environment | E2:204-208; V9:60-62, 820-834 |
| Detail is clustered, with rest areas | Every view has quiet zones; detail sits near the focal point | E2:490-500, 774-778; V9:946-952; Z13:961-980 |
| One clear focal point per view | Highest value and contrast, shape flow and height point at it | E2:952-962; V9:596-604; Z13:273-289 |
| Scale cue present | A player-sized element is near every large form | E2:502-518; Z13:388-404; V9:640-644 |
| Detail matches what the camera sees | Judged from the game camera distance and player speed | E2:396-412, 964-972; Z13:299-319, 634-639 |
| Story and lived-in logic | Wear, cause and effect, a reason for every hazard | E2:730-740; V9:456-474, 1134-1142; Z13:360-378 |
| Reads in the first second | Subject identifiable at a glance from the gameplay camera | Z13:56-74; V9:438-442 |
| Budget kept | Low poly, small textures, even texel density, baked light | E2:778-784; Z13:792-803; V9:662-666 |

---

## 3. The steps they actually follow, in order

**E2 (one hand-painted asset, about a day to polish, E2:160-162)**
1. Low-poly model made in advance (E2:20-22, 52-54).
2. Block in the main colours as big blotches, with random hue shifts (E2:56-74, 84-96).
3. Bake ambient occlusion and curvature as a lighting and edge base (E2:98-118).
4. Paint top to bottom as if lit from above, staying broad (E2:130-154).
5. Medium shapes and turning the forms (E2:218-220, 240-246).
6. Bring every part to the same level before the next detail pass, then repeat (E2:262-268, 562-564). He catches himself over-working the grass and moves on (E2:544-546).
7. Paint a small sample of the stone first to set the recipe for the rest (E2:354-358).
8. Step back regularly (E2:392-394).
9. Edge pass (E2:566-580).
10. If the geometry falls short of the paint, change it in Maya and re-project the texture. He re-UVs uniquely for asymmetric detail (E2:142-146, 582-588, 636-668).
11. Detail: cracks, clumped moss, a few grass blades (E2:670-776).
12. Polish: gradient overlay for focus, sun glints (E2:840-870).
13. Review and critique: does it read in the play space and tell the right story (E2:162-164)?
14. Not done in the demo: grass cards, tightening, painting the back if the camera can rotate (E2:972-982).

**V9 (greybox to art pass)**
1. Design problem: a lava-pit volume as the hook, asking what gameplay comes from it (V9:20-28). Locking a real hook takes months (V9:68-70).
2. Files split into sublevels: design blockout, lighting, art (V9:114-130).
3. Greybox the spawn first, then bridge it to the bombsite, kept simple for the artist (V9:108-112, 136).
4. Lay out the attacker path, forward-facing (V9:184-200).
5. Plan with spawn barriers in mind, without building the map around them (V9:234-262).
6. Placeholder hazard: a red crate texture means "this deals damage"; art makes it look right later (V9:298-316).
7. Stay on the grid for broad strokes; add small details such as railings later (V9:332-342).
8. Play it at any moment; test chokes with smoke abilities (V9:202-208, 368-390, 874-878).
9. Iterate on cover, dead space and penetrable walls, then submit with a clear changelist name and hand off (V9:390-404, 444-454, 516-526).
10. Art: a reference board of the existing site, a map overview and lava photos (V9:536-550).
11. Composition talk with the designer: make the focal tower taller, and assign materials by penetration rules (V9:596-622).
12. Asset "zoo" ready: material cubes in the palette range, props, decals, VFX (V9:622-636, 840-846, 1056-1066).
13. Test a lighting bake (V9:660-662).
14. Import the approved blockout into Maya and snap to it on a matching grid (V9:668-680).
15. Building shells: kit pieces where possible, but VALORANT shells are mostly unique per location (V9:680-700).
16. Floor mesh, trim highlighting the site, UVs (V9:700-714).
17. Textures in, then a check with the designer on lava height and colour (V9:800-818).
18. Set dressing (secondary and tertiary detail): decals, vertex-paint blends, a "whisper" of grass cards (V9:836-866, 928-952).
19. VFX borrowed from another map, slowed down and placed with the designer (V9:1054-1080).
20. Site markers (V9:1082-1090).
21. Each side does its own retrospective (V9:1116-1142).

**Z13 (one prop, 2D concept to 3D)**
1. Theme and story prompt: Set 17 Space Gods, a forgotten Zilean shrine (Z13:21-30).
2. Three sketches; pick one for readability and theme fit (Z13:32-74). Sketches take 2-3 days in real work (Z13:46-48).
3. 2D concept, done for himself: block in light and shadow first ("step number one"), then cast shadows, lighting on the gold, then ground, rocks, plants and sand (Z13:85-93, 193-201, 203-205).
4. Merge the line work into the base and switch to value (Z13:249-259). Reference board alongside (Z13:331-341).
5. Greyscale value check; don't overspend in 2D (Z13:424-442).
6. Project the 2D concept onto the low-poly model in 3D Coat and fill the gaps (Z13:444-466).
7. Paint the texture beyond the concept, which is "a blueprint". Lock parts with paint objects, using separate asset groups from Maya (Z13:468-491).
8. Sharp-edge pass, with a hard and soft balance (Z13:495-517, 640-646).
9. Mid-production art review, answered by a 2D paint-over of a screenshot that is then applied in 3D (Z13:806-856).
10. Geometry pass: cut the geometry to match the painted detail. This is the last step before shipping (Z13:992-1013).
11. Re-export into 3D Coat for final touches (Z13:1014-1020). He would still need 3-4 more hours of edge cleanup (Z13:1050-1056).

**Combined order:** brief or hook, then greybox and play (design), then references, then concept (TFT: the environment artist's own sketches), then blockout or 3D base, then lighting test, then art pass from big to small, then set dressing, then VFX, then polish, then a late geometry and optimisation pass. V9 shows no concept step; concept artists exist on that team but are not shown (V9:6). Lighting is a separate specialty on VALORANT (V9:666-668).

---

## 4. References and research: when, what for

- **E2.** Research comes before any material type he has not painted before (moss, a kind of wood, birch). Without it you keep making the same textures (E2:360-366). Personal touchstones for composition, lighting and materials: Destiny, Blade of the Ruined King, Diablo III, Breath of the Wild, Pixar's Encanto (warm light, cool shadows) (E2:524-536, 598-606). The CS kitchen map "de_rats" is his example of a scale twist (E2:520-522).
- **V9.** The board is built before art starts: photos of the existing site's bold geometric shapes, overhangs and mixed materials, plus a map overview to keep the spatial logic in mind (V9:536-544). For lava, pick out the key features to copy (colour, oozy texture, smoke, glow) (V9:544-550). Reuse a similar existing asset from another map (V9:552-554). On the design side, a greybox can carry a theme (The Last of Us example) to help art, but VALORANT puts gameplay first, so art often inherits abstract shapes (V9:422-438).
- **Z13.** The board includes an existing Zilean skin with sand and gold, chosen to tie to the set's Ekko, plus colour and plant-shape references (Z13:331-341). What he shows is under 10% of what he normally gathers. Gather enough before starting, because your own visual library is small. Take ideas (shape language, colour, light), never copy a design (Z13:341-353).
- **Combined.** References come before concept or art, are per material or feature, and are used to pull out key features, not to copy. They also anchor to the game's existing assets (V9:536-554; Z13:331-353; E2:360-366).

---

## 5. Self-review: what they check before showing anyone

| Check | E2 | V9 | Z13 |
| --- | --- | --- | --- |
| Step back and zoom out to see the whole picture | E2:392-394 | V9:556-564 | Z13:299-301 |
| Values inside the allowed band | E2:818-822 | V9:628-636 | Z13:764-772 |
| Greyscale / value structure | (value talk) E2:728 | — | F1 greyscale hotkey, Z13:428-436 |
| Saturation (he is colour blind, so he checks the colour wheel and asks a colleague) | E2:192-196, 440-444 | — | — |
| Forms visible (wireframe overlay on flat shading) | E2:552-562 | — | — |
| Seen from the game camera and distance | E2:964-972, 786-790 | V9:1006-1018 | Z13:634-639 |
| Scale (refman, walk the space in-engine) | E2:510-514 | head-height checks "always", V9:640-648 | Z13:388-398 |
| Plays right (designer presses play and tests with abilities) | — | V9:202-208, 874-878 | — |
| Half-and-half shapes | — | — | Z13:945-955 |
| Concept against in-game result | — | — | Z13:470-472, 850-852 |
| Low against high detail setting | — | V9:954-960 | — |
| Same quality bar everywhere | E2:262-268, 564 | — | Z13:420-422 |

E2's self-check questions: does it look right in the play space, does it read, does it tell the right story (E2:162-164). The working artist in V9 asks the designer directly, "would this be okay?", before moving on (V9:806-818).

---

## 6. Collaboration: who gives what to whom, what must be agreed, who can veto

**E2**
- **From design to environment:** a greybox the environment must stay within so play stays competitive and readable. Going outside it makes the game "unfun" (E2:454-460).
- **Embedded designer:** a designer sat on the environment team. Artists checked in all the time on things like "I want to put this box here / this texture here" and got feedback on the high-level impact on play. Without those check-ins the game is "mediocre", because each person polishes their own piece in isolation (E2:460-470).
- **Environment and sound:** every texture has footsteps. A new material such as broken glass needs sound to agree. Sound may say there is no time and ask for a different material (E2:472-480).
- **Peers at playtest:** colleagues call out textures that are "way too crazy" after a playtest, and the artist tones them down (E2:822-828).
- **Design and art side projects:** a designer and the artist placed release Easter eggs together (E2:918-930). Hack weeks can produce things that later ship as map details (E2:370-386).
- **Accessibility:** he relies on colleagues for colour checks and pushed for colourblind settings (E2:182-196, 210-216).

**V9**
- **Designer to artist:** a blockout the designer has approved, handed over with a clear changelist name (V9:520-526, 668-670). The artist exports the designer's grid blocks and snaps the art to them exactly (V9:668-680).
- **Designer sets material rules:** surfaces players hide behind must be non-penetrable (concrete or metal). A back wall nobody shoots past can be any material, such as wood, which gives art freedom. Each region should be one material (V9:606-622). Material affects both penetration and sound (V9:408-420).
- **Artist asks the designer what they need to see:** answer, "how the lava looks", because whether it works for play is the big unknown (V9:574-584).
- **Artist asks for layout changes for composition:** make the focal tower taller, separate the pit. The designer agrees or adjusts (V9:354-358, 596-604).
- **Sound callouts limit set dressing:** too much grass would sound like grass. The designer offers to make the back area a separate sound zone (V9:848-856).
- **VFX:** effects are reused from another map's VFX work, then slowed and placed with the designer's input (V9:1056-1080).
- **Lighting:** separate lighting artists; the environment artist can do basic lighting (V9:666-668). Lighting bakes run inside the art pass (V9:660-662, 856-858).
- **Character team:** as the roster grows, distinct character colours can clash with old backgrounds or rule out new ones (V9:988-996).
- **File hygiene and parallel work:** sublevels per discipline, Slack to agree hand-over times, check files in for others (V9:114-134). Quads and tidy UVs so the next artist has a clean base. Work passes between artists, and a fresh artist often improves a tired one's piece (V9:738-754).

**Z13**
- **From art director and design director:** an art review after they playtest the new stage (Z13:806-808). Feedback given: more colour, too much like a desert world and not spacey enough, a single plant is boring (Z13:810-820).
- **The artist protects the core:** more colour elsewhere is fine, but the golden disk stays golden (Z13:822-824).
- **Concept to environment artist:** for 7-8 years he mostly painted from other people's concepts and had to interpret the unclear parts (Z13:565-587). Now he often makes his own concept (Z13:583-595).
- **Latitude on small details:** add new gear to a character and many people weigh in; add small story details to an environment and almost no one cares (Z13:372-378).
- **Giving feedback:** paint-overs, constructive, with a clear vision (Z13:233-235, 885-891).
- **Taking feedback:** the artist is the driver with passengers. Listen to some, not all (Z13:877-881).

**Combined: who can veto what**

| Decision | Owner or veto | Evidence |
| --- | --- | --- |
| Layout, boundaries, routes, cover, sight lines | Level design. Art stays inside the greybox | E2:454-460; V9:668-670 |
| Which surfaces are penetrable or blocking | Level design. Art picks the look within that rule | V9:606-622 |
| Hazard height and colour, VFX placement in play space | Negotiated. The designer has the last word on play impact | V9:812-818, 1068-1080 |
| Art readability breaking play (too busy, too saturated) | Playtest feedback wins. Art tones down | E2:822-836; V9:1000-1018 |
| New surface material | Sound can refuse for time or budget | E2:472-480 |
| Composition tweaks (taller landmark, separated pit) | Art proposes; design accepts if play is unchanged | V9:354-358, 596-604 |
| Big changes after the polish gate | The artist may decline ("next time") | Z13:681-697 |
| Core identity element of an asset | The artist defends it against feedback | Z13:822-824 |
| Small story details | Mostly the artist's call | Z13:372-378 |
| Colours that clash with characters | The character roster can force environment changes later | V9:988-996 |

---

## 7. Review and approval: who reviews when, what they look at, how many rounds

- **E2.** About a day of work, then review and critique on three questions: right in the play space, reads, right story (E2:160-164). Playtests catch readability problems, and peers report them directly (E2:822-828). The embedded designer reviews placement as it happens (E2:460-466).
- **V9.** Several quick loops between designer and artist:
  - The designer's own playtests while greyboxing (V9:202-208, 370-388).
  - The blockout is approved before art starts (V9:668-670).
  - A composition and materials talk (V9:596-622).
  - The first texture pass gets an "is this okay?" check and lava adjustments (V9:806-818).
  - A set-dressing check (V9:932-936).
  - A VFX placement check (V9:1068-1080).
  - Each side's retrospective lists what more iteration would fix (V9:1116-1142).
  
  After launch, player feedback reopens maps months later (V9:974-988).
- **Z13.** Three production gates (Z13:663-697):
  - **Blockout:** low-poly model, UVs, base texture, colours placed.
  - **Early production:** textures cleaned and shapes being finalised, but "super open" to feedback.
  - **Polish:** big feedback, such as "change the composition", is refused for this release.

  Reviewers: the art director and design director after a playtest (Z13:806-808). Feedback goes back as a screenshot, then a 2D paint-over, then changes in 3D, because 2D changes are cheaper (Z13:205-219, 826-832). Mid-production feedback happens about weekly (Z13:856-859).
- **Round count:** no transcript gives a fixed number of rounds. The cadence is constant small check-ins (E2, V9) plus gates with a feedback cut-off (Z13).

---

## 8. Order of work: what comes first, what runs in parallel, what locks when, going back upstream

- **Gameplay first, art later.** VALORANT designs for play first and thinks about art later, so art often inherits abstract shapes it must make architecturally believable (V9:430-438). The greybox is the contract (E2:454-460).
- **Hook before layout.** The lava hook drives the whole site. A real hook takes months to lock (V9:20-28, 68-70).
- **Spawn, then path, then site** inside the greybox (V9:108-112, 184).
- **Blockout approval before art export** (V9:668-670). Art snaps to the approved blocks on a shared grid (V9:342-346, 676-680).
- **In parallel:** design, lighting and art work in separate sublevels of the same map, coordinated in chat (V9:114-130). The artist prepares the asset zoo while design iterates (V9:622-626). A lighting bake is tested early in the art pass (V9:660-662).
- **Going back upstream** (art to design) happens by asking, not silently:
  - the artist asks for a taller focal pillar and a separate pit (V9:354-358, 596-604);
  - the designer moves the lava depth and colour for the art read (V9:812-818);
  - the designer changes sound callout zones to free up set dressing (V9:854-856);
  - sound sends a material back to art (E2:476-478).
- **Concept before 3D,** because changes are cheaper in 2D. Feedback after 3D still goes through a 2D paint-over (Z13:205-219).
- **Locks:** the polish gate closes big feedback (Z13:681-697). The geometry-to-texture pass is done last, because a later big texture change would mean redoing it (Z13:1008-1013).
- **Never locked forever:** maps are revisited after player feedback. Character roster growth can force background changes (V9:974-996). TFT features stay experimental from set to set (Z13:164-176).
- **Inside one asset:** big to small, bringing everything to the same level before the next pass (E2:56-58, 262-268; V9:556-564).

---

## 9. Mistakes they name and how they avoid them

| Mistake | Avoidance | Evidence |
| --- | --- | --- |
| Monochrome textures | Shift hue and value; cool colours in shadows | E2:86-96, 444-452; Z13:111-116 |
| Rendering every grass blade or detail everywhere | Clump detail, leave rest areas | E2:124-128, 424-436, 490-494 |
| Detailing one part (the head, a car's wheels) before the whole | Big to small; same level everywhere first | E2:154-160; V9:556-564 |
| Highlighting every edge; single-width cracks | Vary and remove some highlights; vary crack width | E2:576-580, 672-674 |
| Changing the light source midway | Pick one and stick to it | E2:748-756 |
| Values outside the environment band, called out at playtest | Constant value checks; tone down | E2:818-828 |
| Over-saturated reds (colour-blind artist) | Check the colour wheel, ask a colleague | E2:206-208, 440-444 |
| Stylised rocks too flat and cartoony | Enough material detail to stay believable | E2:538-544 |
| Spending effort where players speed past or the camera never sees | Budget by camera and speed | E2:396-412 |
| Working in isolation, skipping design check-ins | An embedded designer, constant check-ins | E2:466-470 |
| Gamey mechanics that take players' attention | Keep mechanics in the background | V9:36-52 |
| Red or fast-moving environment elements | Neutral palette; slowed VFX, partly hidden | V9:60-62, 1068-1080 |
| Too much detail combined with abilities, so effects get lost | Clean, flat play surfaces | V9:1000-1018 |
| Characters blending into backgrounds | Check against the full roster; revisit maps | V9:988-1000 |
| Unintended verticality that forces big flicks | Verticality only on purpose | V9:1024-1046 |
| A site too big, with dead space | More iteration and playtests | V9:516-520, 1124-1128 |
| A hazard with no visual reason | Show its source and structure | V9:1134-1142 |
| Breaking the build | Clear changelist names; help fix it | V9:524-530 |
| Messy topology and UVs blocking teammates | Quads, organised UVs | V9:738-752, 860-866 |
| A unique but unrecognisable design | Choose what players read in the first second | Z13:56-74 |
| Half-and-half shapes | Big, medium and small rhythm | Z13:221-247, 945-959 |
| Timid, repeated brushwork | Opaque hard brush, decide each stroke | Z13:11, 95-129 |
| Colour polish on a weak value structure | Check greyscale first | Z13:424-438 |
| All-sharp edges, so the piece looks stiff | Balance hard and soft | Z13:640-646 |
| Too many shapes and colours | Less is more | Z13:961-980 |
| Changing geometry late after texture work | Geometry and texture pass last | Z13:1008-1013 |
| Stuck designing a prop | Imagine it as a character with a personality | Z13:939-945 |
| Accepting every piece of feedback | Driver and passengers: pick what to act on | Z13:877-881 |

---

## 10. Lessons for our AI agents

Strength: **SP** = stated principle, **EX** = shown example, **PR** = passing remark. Roles use our names. "For us" notes are my inference for our studio, not claims from the transcripts.

| # | Lesson | Our roles | file:line | Strength |
| --- | --- | --- | --- | --- |
| 1 | The environment builds inside the game designer's layout. Any change to routes, cover or boundaries goes back to the game designer as a ticket, never silently. | environment-designer, game-designer, orchestrator | E2:454-460; V9:668-670 | SP |
| 2 | Keep the game designer "embedded" during an environment build: check every placement that could change play (a box here, a surface there) as it happens, not at the end. For us: a standing ticket channel during the build. | environment-designer, game-designer, orchestrator | E2:460-470; V9:596-622 | SP |
| 3 | Value ladder: UI and VFX get the full range, characters a narrower one, the environment a clamped band. Write the band into the art bible and measure it with look_check. | art-director, environment-designer, modeler, vfx-designer, ui-ux-designer | E2:806-818; Z13:749-790; V9:628-636 | SP (two independent sources) |
| 4 | Reserve gameplay colours (enemy, danger) for gameplay. The environment stays neutral near play surfaces and can saturate higher up, away from the players' eye line. | art-director, environment-designer, vfx-designer, ui-ux-designer | E2:204-208; V9:60-62, 820-834 | SP |
| 5 | Detail clumping: cluster detail at the focal point, leave rest areas, never spread detail evenly. | environment-designer, modeler, art-director, ui-ux-designer | E2:490-500, 774-778; V9:946-952 | SP |
| 6 | Budget detail by gameplay camera distance and player speed. Review from the real camera; skip detail players will not see. | environment-designer, modeler, performance-engineer | E2:396-412, 964-972; Z13:299-319, 634-639 | SP |
| 7 | Put a standard player-size reference model next to every new space and asset, and walk the space in play mode to feel scale. | environment-designer, modeler, game-designer, studio-operator | E2:502-518; Z13:388-404 | SP |
| 8 | Work big to small and bring every part to the same level before the next detail pass. A review packet at any stage shows the whole space at one level. | environment-designer, modeler, vfx-designer, ui-ux-designer | E2:56-58, 262-268, 562-564; V9:556-564 | SP (all three) |
| 9 | Choose the concept players recognise in the first second over the most original one, and say why in the hand-back. | art-director, modeler, marketing, ui-ux-designer | Z13:48-74 | SP |
| 10 | Sketch three options, reject each with a stated reason (off-theme, unreadable), and pick one. This matches our 2-3 directions rule. | art-director, game-designer, environment-designer | Z13:32-74 | EX |
| 11 | Fix in 2D before 3D: answer feedback on a built asset with a paint-over of a screenshot first, then change the model. For us: a ChatGPT edit or a marked-up capture before touching Blender or Studio. | modeler, environment-designer, art-director, ui-ux-designer | Z13:205-219, 826-832 | SP |
| 12 | Three gates with a feedback cut-off. Blockout and early production are open to feedback. At polish, big changes ("change the composition") go to the next release. For us: write "late big feedback = next version" into the gate rules. | orchestrator, all crafts | Z13:663-697 | SP |
| 13 | Prototype hazards with obvious placeholders (red means damage) and let art make them look right later. Do not polish a greybox. | game-designer, quick-builder, environment-designer | V9:298-316 | EX |
| 14 | The level designer presses play all the time and tests with the game's real abilities, not just walking. | game-designer, studio-operator, qa-lead | V9:202-208, 370-390, 874-878 | SP |
| 15 | Split one place into per-discipline layers (design blockout, lighting, art) so parallel agents never edit the same objects. Agree hand-over times. For us: separate folders or models per role, with one owner each. | orchestrator, environment-designer, architect, game-designer | V9:114-134 | EX |
| 16 | Use a shared grid. Art snaps exactly to the approved blockout, so measured play geometry survives the art pass. | game-designer, environment-designer, modeler | V9:332-346, 668-680 | SP |
| 17 | Surface materials carry gameplay meaning (blocking or penetrable, footstep sound zone). The designer sets which surfaces have which rule; art picks the look within it. | game-designer, environment-designer, sound-designer | V9:390-420, 606-622 | SP |
| 18 | A new surface type is a ticket to the sound designer (footsteps, callouts). Sound may say no for time, and art then reuses an existing material. Ground cover is limited where it would imply a wrong sound zone. | environment-designer, sound-designer | E2:472-480; V9:848-856 | EX |
| 19 | Map mechanics stay in the background and come forward only at planned key moments. Ask what player attention a mechanic costs. | game-designer, vfx-designer, environment-designer | V9:36-52 | SP |
| 20 | Environment VFX in play spaces: avoid fast motion and bright danger colours; slow them down and partly hide them; place them with the game designer. | vfx-designer, environment-designer, game-designer | V9:60-62, 1054-1080 | EX |
| 21 | Orientation conventions plus in-world pointers (signs, markers on the biggest landmark, floor trim at the objective) so players never ask "where is X". | game-designer, environment-designer, ui-ux-designer | V9:136-154, 702-706, 1082-1090 | SP + EX |
| 22 | The artist may ask for small layout changes for composition (a taller landmark, a separate pit) and must get the designer's yes. | environment-designer, game-designer | V9:354-358, 596-604 | EX |
| 23 | Before art starts, the artist asks the designer which open question the art must answer for play, and builds that first (here, how the hazard looks). | environment-designer, orchestrator (brief template), game-designer | V9:574-584 | EX |
| 24 | Shape flow: secondary shapes and lines point at the focal point, at several scales. Use it as a review item. | art-director, environment-designer, modeler, ui-ux-designer, film-director | Z13:273-289, 321-329 | SP |
| 25 | Avoid half-and-half shapes: one big, one medium, one small. It is the first thing the TFT artist fixes in others' paint-overs. | art-director, modeler, environment-designer, vfx-designer, ui-ux-designer, marketing | Z13:221-247, 945-959 | SP |
| 26 | Check values in greyscale before colour polish; highlights do not save a weak value structure. Run look_check in greyscale before any colour review. | art-director, environment-designer, modeler, ui-ux-designer, marketing | Z13:424-438 | SP |
| 27 | Finish comes from edge control (sharp where it matters, soft elsewhere), not more detail. Never highlight every edge. | modeler, environment-designer | Z13:495-517, 640-646; E2:566-580 | SP |
| 28 | Story in the space: lived-in cause and effect (leaves under trees, wear, cracks, fossils) and a visible reason for every hazard. | environment-designer, modeler, game-designer, film-director | E2:730-740; V9:456-474, 1134-1142; Z13:360-386 | SP (all three) |
| 29 | Design a prop or set as a character with a personality (the owner's trait shows in the space). Use it when stuck. | modeler, environment-designer, art-director | Z13:927-945 | SP |
| 30 | Less is more: the fewest shapes and colours that carry the idea. | art-director, all visual crafts | Z13:961-980 | SP |
| 31 | Fix one light direction early and keep it. Lock the place's lighting as the reference ("North Star"); baked or static lighting also gives shadow control and saves performance. | environment-designer, modeler | E2:748-760; V9:662-666; Z13:85-93 | SP |
| 32 | Warm and cool split between light and shadow. Direction depends on style: TFT uses cool sun and warm shadows; the Encanto example is warm light and cool shadows. Put the direction in the art bible; do not assume one. | art-director, environment-designer | Z13:646-660; E2:598-606 | EX |
| 33 | Gather enough references before starting (shown: under 10% of normal), per material or feature. Extract key features; never copy a design. Research any material you have not made before. | art-director, environment-designer, modeler, vfx-designer, all visual | Z13:341-353; V9:536-550; E2:360-366 | SP |
| 34 | Paint or test a small sample first (one stone patch) to set the recipe, then apply it to the rest. | modeler, environment-designer, vfx-designer | E2:354-358 | EX |
| 35 | Prepare a kit ("zoo") of approved materials in the palette band, props, decals and VFX before set dressing; reuse proven assets from other places. | environment-designer, modeler, vfx-designer, art-director | V9:552-554, 622-636, 840-846, 1056-1066 | EX |
| 36 | Modular kits help large spaces, but tight competitive layouts may need unique pieces. Choose per place. | environment-designer, modeler | V9:686-700 | EX |
| 37 | Mobile budget: low topology, small textures, even texel density across assets. | modeler, environment-designer, performance-engineer | Z13:628-633, 792-803; E2:778-784 | SP |
| 38 | A low-detail setting exists for performance and competitive clarity. Check the place still reads with detail stripped. | performance-engineer, environment-designer | V9:954-970 | EX |
| 39 | Places are never final. Player feedback and new characters reopen maps months later. Keep places editable and recorded. | live-ops-designer, environment-designer, art-director, analyst | V9:974-996; Z13:162-176 | SP |
| 40 | Clean hand-off files (quads, organised UVs, clear change names) because work passes between artists; a fresh artist often improves a tired one's piece. For us: a second agent pass on stale work. | modeler, environment-designer, orchestrator, all builders | V9:524-530, 738-754 | SP + PR |
| 41 | Taking feedback: the driver listens to some passengers, protects the asset's core identity, and says what will not change. | all crafts, orchestrator | Z13:822-824, 877-881 | SP |
| 42 | Giving feedback: paint-overs with a clear vision, constructive. For us: the art director's review files include marked-up captures. | art-director, reviewer, game-designer | Z13:233-235, 885-891 | SP |
| 43 | Playtest feedback overrides art: a peer telling the artist to tone down a texture after a playtest is normal and expected. Playtests check art readability, not just play. | qa-lead, environment-designer, orchestrator | E2:822-836 | EX |
| 44 | The art review happens after the reviewers (art director and design director) have playtested the stage, not from stills alone. | orchestrator, art-director, game-designer | Z13:806-808 | EX |
| 45 | Model from a best guess, then change the geometry where it fails the painted read and re-project. Marry geometry to texture as the last step, because it locks the texture layout. | modeler | E2:582-588; Z13:992-1013 | SP |
| 46 | Accessibility: no gameplay information by colour alone; push for colourblind options; check saturation with a tool or second opinion. | ui-ux-designer, vfx-designer, art-director | E2:204-216, 440-444 | SP |
| 47 | Plants and ground cover: strong gesture, simple texture, readable in peripheral vision; ground blends integrate props. | environment-designer, modeler | Z13:404-420, 850-854; E2:422-430 | SP |
| 48 | Level layout for competitive play: spawn first, forward-facing paths, flat with intentional elevation, two entries per objective, balanced neutral space, predictable "cubes" so players lose to the opponent. Genre-specific; do not apply to obbies or exploration games, which V9 itself contrasts (V9:190-196). | game-designer | V9:108-112, 184-200, 282-298, 482-514 | SP (competitive genre) |
| 49 | Keep play floors readable for ground-placed abilities and traps. | environment-designer, vfx-designer | V9:940-944 | PR |
| 50 | In polish, push the focal point (a gradient or light that dims everything else) even at the cost of detail elsewhere. For us: local light or atmosphere on the landmark. | environment-designer, film-director | E2:840-858 | EX |
| 51 | Under a fixed camera, cheat ("smoke and mirrors"): paint over clipping edges and skip unseen backs. Under a free camera, finish all sides. | environment-designer, modeler | Z13:634-639; E2:408-412, 978-980 | SP |
| 52 | No concept artist needed: the TFT environment artist makes his own rough concept, and says that doing so improved his 3D work. For us: the environment designer and modeler make and paint over their own ChatGPT references under the art bible. | environment-designer, modeler, art-director | Z13:203-209, 583-595 | SP |

---

## Gaps (not in these transcripts)

No QA test plans, engineering hand-offs, performance profiling or formal sign-off documents. Concept artists are named on the maps team but not shown (V9:6). There is no round count for reviews. The TFT gates are the only formal stage names (Z13:663-697).
