---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J009-T01, Art_Director_Research_Paper.txt lines 1-358"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Art direction paper part 1: evidence rules, 15 rules, studio precedents (Deadlock, TF2, Dota 2, League of Legends, 8 short cases, teaching sources) (lines 1-358)

Paraphrased notes. The paper (AP) stays outside git. Every row cites `AP:<line>`. Nothing here is fact-checked yet: claims are the paper's, listed in section 13 for the fact-check pass. The paper is dated 2026-10-21. It is strong evidence, not gospel: its own limits are kept in section 14.

## 0. How to read

| Key | Meaning |
| --- | --- |
| AP:n | line n of `Art_Director_Research_Paper.txt`. One paragraph = one line. Source register = AP:1013-1695 (only cited entries resolved here, section 12). |
| Tag | The paper's tag. VERIFIED = published data, a measured study, or an explicitly documented platform or tool capability. EXPERIENCE = a studio's, artist's or director's account of its own process. OPINION = the paper's interpretation, proposed process or authored example. A documented capability does not prove artistic quality. A studio's success does not make a universal rule (AP:15). |
| O00 | The paper's own label for its authored recommendations, readings and fictional examples (dated 2026-10-21). Not an external study (AP:13, 1015). |
| Prov | Who is speaking. **S-DOC** = the studio published it (product page, announcement, official guide). **DEV-ACC** = an artist or developer account of their own process (interview, dev blog, press kit, individual's post). **PAPER** = the paper's interpretation, transfer or invented example. Prov is my label for a skill writer; the paper uses only Tag. |
| Src | The paper's source id, resolved in section 12 with its date. "undated, acc 2026-10-21" = the source shows no date; the paper only read it on that day. Access is not publication (AP:15). |
| Row IDs | EC evidence contract, RU rule, DL Deadlock, TF Team Fortress 2, DO Dota 2, LL League of Legends, SC short case, TS teaching source, N number, CG comparison, FC claim to check, X contradiction or limit. |
| Rule of use | Treat every PAPER row as a proposed check, never as a rule the studio published. Never write "Valve does X" or "Riot requires X" from a PAPER row. |

## 1. Evidence contract (AP:1-17)

| ID | AP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| EC1 | 7 | The art director's product is a coherent set of visual decisions, not a pile of attractive assets. Link the designer's intended experience to shape, color, value, light, motion and presentation, and keep that link as assets grow. | OPINION | O00 |
| EC2 | 7 | Good art can be wrong for this game. Three examples the paper gives: an effect so nice it hides a threat; an environment so impressive it flattens character readability; a thumbnail that promises a fantasy the game does not deliver. | OPINION | O00 |
| EC3 | 9 | Reference flow: every model reference image starts in ChatGPT's image system. A generated image is not an anchor until reviewed and approved. The art bible holds verbal locks, concrete approved images, and a list of what may vary. | OPINION | O00 |
| EC4 | 9 | A good lock constrains a relationship (example: dangerous projectiles keep a recognizable shape and value treatment). It does not force the same colors or detail on every object. | OPINION | O00 |
| EC5 | 15 | Source ids resolve to dated records, short key quotes and URLs at the end. Living docs with no date are marked undated with an access date. | contract | O00 |
| EC6 | 17 | What the research did NOT do: generate or benchmark reference images, build a Roblox scene, run a player study, measure a submitted screenshot. All procedures here are proposed checks to run on the real project. | OPINION | O00 |
| EC7 | 17 | Numbers keep their original task, model, game, device and measurement scope. Where no defensible universal threshold exists, the paper says so and gives a method to choose and test one. Deliberate artistic choices are allowed and are not scientific constants. | OPINION | O00 |

## 2. The fifteen rules (AP:21-49)

Each rule carries the paper's tags. When a VERIFIED source is listed, the source backs only the capability named in the register (section 12), not the whole rule. The art-director step is the OPINION part.

| Rule | AP | Rule in my words | Tag | Src |
| --- | --- | --- | --- | --- |
| RU01 | 21 | Turn the player fantasy and gameplay priorities into a visual direction before approving production assets. | OPINION | O00 |
| RU02 | 23 | Keep the owner's decision authority. Propose, compare, review. Never quietly change the creative brief. | OPINION | O00 |
| RU03 | 25 | A reference is approved evidence of the intended style, not automatically correct generator output. | VERIFIED A02 (undated, acc 2026-10-21); OPINION O00 | A02, O00 |
| RU04 | 27 | Keep a small set of meaningful locks and say what may vary. Cohesion is not uniformity. | OPINION | O00 |
| RU05 | 29 | Review the gameplay camera and a crowded scene before judging isolated beauty renders. | OPINION | O00 |
| RU06 | 31 | Give visual emphasis by what the player decides now, not by each specialist's wish for prominence. | EXPERIENCE R01 (2021-03-12); OPINION O00 | R01, O00 |
| RU07 | 33 | A measured visual difference is not automatically an artistic failure. A metric needs a task and an approved tolerance. | VERIFIED A13 (2026-03-01); OPINION O00 | A13, O00 |
| RU08 | 35 | Grayscale, silhouette, palette and thumbnail tests are complementary diagnostics, not an automatic taste score. | VERIFIED A06 (undated, acc 2026-10-21); OPINION O00 | A06, O00 |
| RU09 | 37 | Use redundant visual meaning (more than color alone) where color alone would hide an important state. | VERIFIED A08 (undated, acc 2026-10-21); OPINION O00 | A08, O00 |
| RU10 | 39 | Keep a studio's art language separate from its implementation or platform budget. | OPINION | O00 |
| RU11 | 41 | Feedback = prioritized discrepancy + its consequence + a visible acceptance condition. The specialist picks the craft solution. | OPINION | O00 |
| RU12 | 43 | Judge combinations (UI, effects, motion, sound), not assets alone. | EXPERIENCE R01/R02 (2021-03-12 / 2021-04-09); OPINION O00 | R01, R02, O00 |
| RU13 | 45 | Version anchors, prompts and locks so a style update does not silently invalidate approved work. | OPINION | O00 |
| RU14 | 47 | Marketing stays faithful to the playable fantasy and current visual identity. | OPINION | O00 |
| RU15 | 49 | Require real project captures and device evidence before claiming the direction reads and runs on phones. | VERIFIED P03/P05 (both undated, acc 2026-10-21); OPINION O00 | P03, P05, O00 |

## 3. Deadlock (Valve) in depth (AP:53-107)

Owner's top reference. Section 3.1 is what Valve published or said. Section 3.2 is the paper's own reading. Do not mix them.

### 3.1 What the sources document (Prov S-DOC unless noted)

| ID | AP | Fact (paraphrase) | Prov | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| DL-01 | 57 | "City Never Sleeps" update presents an occult New York. Three named lanes: Broadway, Greenwich, York. Four named districts: Theater, Chinatown, Haunted Lot, Plaza. Neutral creatures redesigned as "Haunts". Themed landmarks include an occult university and Wall Street warlocks. | S-DOC | VERIFIED | V01, 2026-09-29 |
| DL-02 | 57 | Same update changes health bars and status presentation, adds a parry indicator near the reticle, and lets players adjust enemy UI color. | S-DOC | VERIFIED | V01, 2026-09-29 |
| DL-03 | 57 | Sunken Plaza: sound from outside is muffled, and the place drains stamina (sound and gameplay tied to a place). | S-DOC | VERIFIED | V01, 2026-09-29 |
| DL-04 | 57 | Paper's caution: these are product features, not evidence that every player reads them well. | PAPER | VERIFIED+limit | V01 |
| DL-05 | 65 | "Old Gods, New Blood" overhauls Patrons, bases, troopers and defensive abilities. Hidden King is described through skyscraper shadow, boarded housing and the city's cracks. Archmother is described through glass, steel, stone, order and power. | S-DOC | VERIFIED | V02, 2026-01-22 |
| DL-06 | 73 | Baba's official introduction ties the Central Park pigeon-lady premise to tea, birds, yarn, and a bench that becomes mobile in combat. | S-DOC | VERIFIED | V04, 2026-10-06 |
| DL-07 | 77 | Solomon's official introduction maps chess-piece names to tactical roles: bishop offense, knight protection or retreat, rook advance, queen lockdown. | S-DOC | VERIFIED | V05, 2026-10-09 |
| DL-08 | 81 | Violet's official introduction links her artist identity to Living Ink, Flow State, Still Life and Abstract Landscape (abilities). | S-DOC | VERIFIED | V06, 2026-10-16 |
| DL-09 | 87 | Valve says it put remaining core-game work ahead of older-hero polish, built several systems in parallel, and left Midboss, Guardians and Walkers for later. Hero remodels were expected later because other core parts needed work first. Speculative features depend on playtesting. | DEV-ACC (studio note) | EXPERIENCE | V03, 2026-09-29 |
| DL-10 | 93 | A Valve-area artist's post credits the original Professor Dynamo concept art to colleague Vasili Zorin. It supports that one credit only, not that Zorin owns Deadlock's art direction. | DEV-ACC (individual post) | EXPERIENCE | V07, undated (relative timestamp only; acc 2026-10-21) |
| DL-11 | 95 | NOT FOUND by the paper's searches: a complete public Deadlock art bible, palette count, gray-value bands, silhouette pixel minimum, review quota, target phone budget, or full internal production account. The paper says this is a limit of what it found, not proof they do not exist. | PAPER (research limit) | OPINION | O00, searches to 2026-10-21 |
| DL-12 | 95 | Fan redesigns and recruitment portfolio posts are not Valve-approved concepts. Community aesthetic labels and the paper's own readings must not become "Valve rules". The paper does not reconstruct unseen footage or shader settings. | PAPER | OPINION | O00 |

### 3.2 The paper's reading and the checks an art director can run (Prov PAPER)

| ID | AP | Paper's reading (not Valve's rule) | Check or step | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| DL-13 | 59 | Useful direction in V01 = a generative world rule: familiar urban institutions changed by one supernatural premise. It can produce architecture, characters, props, terms and behavior without making assets identical. | Write one causal rule (the paper's invented example: a seaside repair town runs on bottled weather). Then require every craft to show what the rule changes. A pretty place plus unrelated icons and generic spells does not count. | OPINION | V01 (motive), O00 |
| DL-14 | 61 | A district needs a navigational identity and a gameplay reason, not only a different hue. | Per district give: approved landmark silhouette, material family, spatial function. Give VFX and audio the related state cues. Test that the landmark survives the real phone camera and UI overlap. Do not read "4 districts" as a map-size recommendation. | OPINION | V01 (motive), O00 |
| DL-15 | 67 | V02 is better reference than "one faction blue, one red": the shared city is the parent constraint, and each faction's relationship to it drives smaller choices. | Fix common construction tech in the bible. Separate factions by upkeep, massing, surface treatment, sound character, ceremony. The paper says Valve did NOT publish these smaller rules; they are extrapolations. | OPINION | V02 (motive), O00 |
| DL-16 | 69 | Workflow for faction work. | Ask for a paired faction sheet (same prop function, camera, scale, lighting). Ask which differences show allegiance and which are random output. Test an unlabeled in-game crop. Creative director approves identity. The AD reports uncertainty and does not invent symbolism from visual resemblance. | OPINION | O00 |
| DL-17 | 75 | Baba's bench shows a signature object shaping silhouette, movement, interaction and sound together. | Propose one signature tool or companion whose identity survives with surface detail stripped. Do not copy the bench; do not assume heavy machinery is needed. | OPINION | V04 (motive), O00 |
| DL-18 | 79 | A motif works when it organizes the action vocabulary, not only decoration. | Ask whether names, icon shapes, animation accents and gameplay roles tell compatible stories. Test the signifiers without assuming players know the cultural reference (here, chess). | OPINION | V05 (motive), O00 |
| DL-19 | 83 | Define a family resemblance across an ability set but keep distinct state and danger cues. "All magic looks like ink" fails if friendly trails, harmful zones and decorative splashes look alike. | Review at real gameplay scale with overlapping actions, on phone. Do not approve from a full-size illustration alone. | OPINION | V06 (motive), O00 |
| DL-20 | 89 | A mixed-fidelity public build is not proof of missing direction (paper's reading of V03). | Track asset status: current target / approved legacy / temporary placeholder / scheduled migration. Do not reject a working placeholder with final-marketing criteria. Do not silently turn a placeholder into an anchor. Each approved anchor carries its style version and intended use. If the lighting target changes, run a cross-craft regression sheet before regenerating everything. | OPINION | V03 (motive), O00 |

Paper table (AP:97-105), numbers and limits:

| ID | AP | Rule | Number | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| DL-21 | 99 | Treat district count as this update's content, not a target. | 4 | VERIFIED | V01, 2026-09-29 |
| DL-22 | 101 | Couple world motif to several crafts. | no validated count | OPINION | analysis of V01-V06, 2026 |
| DL-23 | 103 | Separate temporary assets from final anchors. | no Valve quota found | OPINION | based on V03, 2026-09-29 |
| DL-24 | 105 | Deadlock visual thresholds. | unknown | research limit | sources located through 2026-10-21 |

## 4. Team Fortress 2 (Valve) (AP:109-135)

| ID | AP | Statement (paraphrase) | Prov | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| TF-01 | 111 | The 2007 rendering paper by Mitchell, Francke and Eng reports early commercial-illustration references and art/engineering teamwork. The nine class silhouettes were validated with no internal shading; proportions, equipment and clothing helped tell them apart. It favors cutting high-frequency detail, cool (not black) shadows, rim highlights that stress silhouette, and restrained repeating environment pieces. RED/BLU architecture contrasts warm, natural, angular with cool, industrial, orthogonal. The paper calls this a coordinated aesthetic system, not just "cartoon shading". | S-DOC (studio paper) + DEV-ACC | EXPERIENCE | V08, 2007 |
| TF-02 | 113 | Half-Lambert scale 0.5, bias 0.5, exponent 1 (the source paper contrasts with an older exponent 2). Implementation parameters only: not luminance targets, contrast ratios, or Roblox lighting controls. | S-DOC | VERIFIED | V08, 2007 |
| TF-03 | 117 | TF2 briefly explored claymation, rejected it for higher product goals, kept the idea of simulating artistic materials. Biographies and repeated artist/team talks guided Demoman exploration. The post gives no required number of concepts or meetings. | DEV-ACC | EXPERIENCE | V10, 2008-08-28 |
| TF-04 | 121 | Alpine theme answered desert fatigue, kept character compatibility, reused structures. Cooler foliage and rock colors widened the palette; mountain and valley sides separated the map. | DEV-ACC | EXPERIENCE | V09, 2008-08-19 |

Transfer checks (Prov PAPER, tag OPINION, Src O00):

| ID | AP | Check or step |
| --- | --- | --- |
| TF-05 | 115 | Ask the modeler for an untextured silhouette contact sheet from gameplay-relevant views (not one flattering orthographic pose). Same camera and scale for all candidates. Label role-recognition failures and likely confusions. Do not approve on foreground area or outline-difference scores alone: they do not show a new player understands the role. Keep a clean "decision layer" in crowded scenes; allow detail where it does not compete. |
| TF-06 | 119 | Exploration must answer a product question. Show competing target images with explicit differences (mood, scale readability, fabrication, player fantasy). Log what was rejected and why. Do not invent a "Valve uses exactly three directions" rule. A lock is a resolved decision with a reason, not every incidental mark of an early image. |
| TF-07 | 123 | A biome can be added without changing identity. Review a new biome with existing characters, effects, UI. Approve exceptions as extensions of a parent grammar; do not force new images to match an old background's literal colors. A newly beautiful render is not a reason to change all approved materials without a migration decision. |

Paper table (AP:125-133): TF2 silhouette validation spans the original class roster, 9 classes, EXPERIENCE, V08 2007 (AP:127). Half-Lambert settings are renderer-specific, 0.5 / 0.5 / 1, VERIFIED, V08 2007 (AP:129). Exploration and feedback counts: not published, research limit, V10 2008-08-28 (AP:131). A biome extension can keep old characters and structures, no numeric rule, EXPERIENCE, V09 2008-08-19 (AP:133).

## 5. Dota 2 (Valve) (AP:137-149)

| ID | AP | Statement or check | Prov | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| DO-01 | 139 | The current Workshop Character Art Guide: gameplay view outranks loadout display. Silhouette should carry identity and orientation; changed silhouettes are fine if identity stays legible. Darker lower body to lighter upper body is a default, not absolute. Primary, secondary, tertiary key colors may be blended with intermediates and grays (not a three-color pixel limit). Rest areas balance detail; prominent contrast and saturation support focal areas. Evaluate in game context, not the isolated asset. Discouraged extremes apply to its own rendering context, not all graphic design. | S-DOC (official guide; paper tags EXPERIENCE) | EXPERIENCE | V11, undated, acc 2026-10-21 |
| DO-02 | 141 | Make the bible operational: next to each style rule put target camera, background samples, approved exception, failed example, pass criterion. Keep identity cues stable across cosmetics without freezing every contour. Check orientation and role at intended distance; check color against map and effects together. A palette extractor shows dominance and drift, but lighting, shading and antialiasing add colors, so raw unique-color counts are not a compliance gate. | PAPER | OPINION | O00 |
| DO-03 | 143 | Test spec: keep the native-resolution gameplay capture. Make a grayscale version, an isolated silhouette, and a nearest-confusion pair with identical transforms. Report target bounding-box width and height in pixels, overlap or occlusion, and camera, device and UI state. Compare with approved examples. Thresholds must come from the project's own recognition tests: the Valve sources give no universal silhouette size, success percentage or grayscale contrast ratio. | PAPER | OPINION | O00 |
| DO-04 | 147 | TF2's silhouette proof and Dota's allowance for changed cosmetic silhouettes do not conflict: both protect recognition, one for foundational class design, one for variations of existing heroes. "Never change silhouette" misreads Dota. Dota's value gradient does not ban dark-headed characters. Aim firm, means conditional, unless the creative director locks the means. | PAPER | OPINION | V08/V11, O00 |
| DO-05 | 149 | Deadlock's temporary asset variety and TF2's compatibility need are different production situations, not permission for drift. Status-aware reviews protect speed; final target scenes still need cross-craft coherence. | PAPER | OPINION | V03/V09, O00 |

## 6. League of Legends (Riot) in depth (AP:167-187)

Owner's top reference. Rows LL-01 to LL-08 are Riot's accounts as the paper reports them (Prov DEV-ACC, all tagged EXPERIENCE). Rows LL-09 onward are the paper's reading unless stated.

| ID | AP | Statement (paraphrase) | Prov | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| LL-01 | 171 | Riot's 2021 account defines clarity around comprehension and response. Three priorities: communicate gameplay, keep the importance hierarchy, limit unnecessary noise. | DEV-ACC | EXPERIENCE | R01, 2021-03-12 |
| LL-02 | 171 | A champion should keep one identity-bearing silhouette feature, show facing direction, and suggest its source of power. | DEV-ACC | EXPERIENCE | R01, 2021-03-12 |
| LL-03 | 171 | Animation can reinforce recognition but becomes a constraint when it carries most of the identity (the article's example: Lee Sin). | DEV-ACC | EXPERIENCE | R01, 2021-03-12 |
| LL-04 | 171 | Spell emphasis is ranked by consequential properties: damage, crowd control, dodgeability, and changes to how opponents must play. Key quote: "the amount of attention an ability grabs should match its level of importance." | DEV-ACC | EXPERIENCE | R01, 2021-03-12 |
| LL-05 | 171 | A large telegraph that implies a real chance to dodge when there is little can miscommunicate, even if it looks good. | DEV-ACC | EXPERIENCE | R01, 2021-03-12 |
| LL-06 | 171 | Skin changes across model, animation, VFX and audio share one clarity allowance. Maxing every discipline together can erase recognition. | DEV-ACC | EXPERIENCE | R01, 2021-03-12 |
| LL-07 | 171 | Riot aims for base-versus-skin clarity parity: cosmetics must not give a competitive advantage. | DEV-ACC | EXPERIENCE | R01, 2021-03-12 |
| LL-08 | 185 | Skins art director compared two Blitzcrank skins. Space Groove Blitz+Crank kept recognizable hands, head and shoulder shapes, so it could have a floatier but still jerky walk. Lancer had already changed other cues (hands, shoulder treatment), leaving less room for animation change. Riot admits the earlier decision predated the clearer framework. Key quote: "we had to pull back in other places." | DEV-ACC | EXPERIENCE | R02, 2021-04-09 |
| LL-09 | 173 | PAPER translation: write a semantic priority contract before approving single effects. Record: what the player must recognize; which event matters now; what identity survives cosmetic variation; which craft owns each cue. Review the combined screen, not six impressive sheets. A design can be coherent in style yet fail because the eye goes to the wrong event. A modest material or simple projectile can be right if it sits correctly in the hierarchy. The paper says these are proposed questions, not Riot numeric thresholds. | PAPER | OPINION | R01 (motive), O00 |
| LL-10 | 177 | Summoner's Rift (2014 Riototown article, found as a named later reprint): a painterly yet graphic magical forest; welcoming foliage against harder rock shapes. Hierarchy: environment behind champions, effects above, restrained UI on top. Landscape as a common stage for a broad cast, not one mood for all characters. Shape and value simplification and directional composition aid navigation. Painted edges and selective alpha disguised economical geometry. Charts show relative constraints; no exact value bands or palette counts were measured by the paper. Key quote: "It should clarify game space, not clutter it." | DEV-ACC (via third-party reprint) | EXPERIENCE | R04, reprint 2014-11-11; provenance limit stated |
| LL-11 | 179 | Later Riot engineering retrospective: the map update had to improve presentation without raising the minimum hardware spec. Fog of war that was fine on the old map looked visibly poor against the new look. Lesson (paper's): an art update changes the judgment of neighboring systems. | DEV-ACC | EXPERIENCE | R05, 2016-05-13 |
| LL-12 | 181 | PAPER transfer for Roblox: define a common stage that supports the whole cast: quiet fighting surfaces, deliberate landmarks, room for effects, one material and edge grammar. Do NOT copy the environment-champion-VFX-UI order as a law. A puzzle clue, dialogue face, construction preview or cutscene reveal can be the focal subject. State the current interaction and derive the hierarchy from it. Keep crowded screenshots as approval anchors beside clean ones. | PAPER | OPINION | O00 |
| LL-13 | 187 | PAPER on feedback without micromanaging: say which recognizability cues a costume has spent and which must remain. Ask for alternatives: restore a shape, keep a motion signature, cut secondary spectacle, or revise the theme. The AD explains the constraint and compares; the animator picks the craft solution. | PAPER | OPINION | R02 (motive), O00 |

Checks for the art director (each from a row above):

| ID | From | Check |
| --- | --- | --- |
| LL-C1 | LL-04 | For each effect, rank it by damage, crowd control, dodgeability, and effect on opponent play; then check its screen attention matches that rank. |
| LL-C2 | LL-05 | Does the telegraph size or brightness promise a dodge window the mechanic does not give? If yes, fix the picture, not the rule. |
| LL-C3 | LL-02 | For every character/tool: name the silhouette feature that must survive, the facing cue, the power-source cue. |
| LL-C4 | LL-03 | If animation carries most of the identity, mark animation as a constraint on cosmetic variants. |
| LL-C5 | LL-06 | Give each cosmetic one shared clarity allowance across model, motion, VFX, audio; do not max all four. |
| LL-C6 | LL-07 | Compare base and skin at gameplay scale. A skin must not make the player easier or harder to read. |
| LL-C7 | LL-11 | When art changes, re-check neighbor systems (fog, UI, effects) against the new look. State the hardware floor before the art pass. |

## 7. Eight short cases (AP:189-255)

Accounts (Prov DEV-ACC, all tagged EXPERIENCE by the paper):

| ID | AP | Account (paraphrase) | Src, date |
| --- | --- | --- | --- |
| SC-OW | 191 | Overwatch concept artists Daryl Tan and Qiu Fang: art solves gameplay problems. A Talon "Shield Guy" concept piled up shield, beam and heavy armor without a clear role; role overlapped other enemies, the beam failed in playtests, the silhouette lacked recognition. Fix was to revise the role, not decorate. Skins must keep recognition and fit animation. Honeydew Mei swaps to summer clothes but keeps identity; her drink-inspired weapon still had to look made in-world. Large shapes read from far, small details reward closeness. An Ana coat needed concept, modeling and rigging to agree on shape without clipping. Sigma's gravity premise was shown across animation, audio, effects, gameplay. | C01, undated, acc 2026-10-21 |
| SC-HD | 199 | Hades art director Jen Zee: Supergiant is game-design-led; art ideas stay disposable until gameplay and narrative are clearer. A preproduction tone change moved the look from painterly to pen-and-ink (influences Mike Mignola, Fred Taylor), described as more efficient for the large art volume. An early Zagreus sketch and a color script gave anchors; the color script showed the journey's color relationships. Reported shipped output: 59 portraits, 68 models, 194 boon icons, 1,400 environment textures, 32,494 effects-animation frames, 942,489 character/enemy-animation frames (not concept or staffing numbers). | C02, 2021-06-07 |
| SC-S3 | 207, 209 | Nintendo: the series culture shifts (first game mischievous street culture, second more sophisticated urban, third counterculture). Splatoon 3's "chaos" followed the last Splatfest of the previous game. Story, art and sound were planned together; a geographic map helped relate cities. Props: Stringer from fishing gear, Splatana Stamper from a date stamp; fictional makers, lockers, collectibles and an in-world card game widen what inhabitants do. Goal: a Splatoon weapon, not a firearm. Key quote: "look like a Splatoon weapon, without making it look like a firearm" (C04). | C03 + C04, both 2022-09-07 |
| SC-MW | 217 | Nintendo devs changed Mario's model for what the player sees: face readable while keeping a useful movement direction, so it can look odd from other angles. Joints and animations more than doubled vs the previous title (no absolute counts given). Pipe sound timing follows the visible action, not the button press. Elephant Mario served gameplay (bigger body, sideways interaction, water spray). Open online meetings anyone could join. Koji Kondo recalls unified direction appearing in the last six months to a year after wide idea exploration (a retrospective, not a schedule). | C05, 2023-10-17 |
| SC-FN | 225 | Epic: Lumen changed indoor lighting and material response in Fortnite; physically driven results made interiors too dark and caused big exposure swings. Artists used Indirect Lighting Intensity 2.0, added Skylight Leaking and Diffuse Color Boost instead of more shadow lights, and used Local Exposure to keep detail in bright and dark areas. Technical account: 60 fps console target, 4 ms budget for global illumination plus reflections. Settings and budget belong to that implementation. The article notes screenshots cannot show all temporal behavior. | C06, 2023-01-26 |
| SC-ST | 233 | Rare, Sea of Thieves Ravenwood set: concept jam of ravens plus assassin; the costume anchored related ship, item and presentation choices. Three costume stages give different role-play looks, not one "better" final. Shared iridescence exposed material differences between character and props. Artists compared assets under actual in-game lighting and tuned material controls (too metallic = too dark; too little = effect lost). A face-conforming mask needed iteration across pirate faces. Credits internal artists, external collaborators, an outsourced animator, editorial contributors. Paper read this via search-index text after the direct page gave a 403. | C07, 2023-03-03 |
| SC-HS | 241, 243 | Blizzard effects artist Hadidjah Chamberlin: class-specific visual vocabulary (Priest slime keeps light, gold, magic; Druid lunar and Mage astronomical need different identities). Floop's persistent effect shrank from full screen toward the hero area so it would not hide a combo. Magnetic's small arrows became a simpler, larger beam; too much spectacle risked implying the highlighted move was always correct. Gameplay is put before visual spectacle; iterated with UI. Sound team separately: emotional interpretation over literal simulation, whimsical link to Warcraft, recognizable spell identity, timed card events. | C08, 2018-10-26; C09, 2023-06-09 |
| SC-BS | 251 | Supercell calls its 2025 Brawl Stars logo change an evolution, not a rebrand. Old hierarchy stressed "Stars" over the more distinctive "Brawl"; complexity hurt across sizes; app icon did not match the logo. Kept: skull, color identity, lettering style. Reports testing several directions and picking the strongest positive response across groups. No sample sizes, scores, controls or revenue effect published. | C10, 2025-08-24 |

Lessons (Prov PAPER, tag OPINION, Src O00). Column "Check" = a step an art director can run. Column "Do not copy" = the paper's own warning.

| ID | AP | Check | Do not copy |
| --- | --- | --- | --- |
| SC-OW-L | 193, 195 | Write an identity contract before skins: silhouette features that cannot vanish, visible equipment that signals the role, movement needed for the role. Compare skins at gameplay distance, not portraits. Reject a design with an unreadable gameplay role even if assets are polished. One creative premise should yield consistent animation, sound, effect notes. | Overwatch's costume shapes; the idea that a humanoid hero pipeline fits every Roblox avatar system. Copy the recognition contract and cross-craft review only. |
| SC-HD-L | 201, 203 | Make a compact emotional color script for the whole player journey and tie each asset request to a place in it. Keep an early "why this look?" record. Separate design intent from its implementation (the same intent can survive a cheaper shader, outline or texture process). | Dense linework as a universal premium look. Pen-and-ink as always cheaper. The output counts as productivity targets. Judge efficiency by measured time in the project. |
| SC-S3-L | 211, 213 | Build a short "culture generator": what residents value, make, repair, find cheap, which brands exist, what they collect. Derive signs, gear, clothing, UI decoration, reward objects from it. Gives independent AI asset sessions one source of decisions. | "Chaos" is a fictional culture, not permission for clutter. Keep readable relation between environment and actionable info. Do not lift Splatoon's ink, type, or prop transformations as a ready identity. |
| SC-MW-L | 219, 221 | Review the real camera before demanding physically correct geometry. Fixed or side cameras may justify tailored proportions. For free cameras, check the full visible range. Sync sound, effects, motion to the player-visible action, not the code event. | A camera-specific cheat on a freely rotating avatar. Nintendo's late convergence as an excuse to delay decisions: keep an approved current target and the conditions to reopen it. |
| SC-FN-L | 227, 229 | A target render must show playable space is visible, not just moody. Compare indoor/outdoor transitions, moving-camera exposure, object readability against bright windows. Author materials and lighting together (a new light model can break a good surface). Record intentional departures from realism as art-direction decisions so later agents do not "correct" them. | 2.0, 4 ms, the console target, or Unreal settings in Roblox or a phone profile. Translate the purpose; measure the Roblox implementation. |
| SC-ST-L | 235, 237 | Approve every outsourced or AI-made item beside related assets in a representative scene. Give one accepted reference material and one accepted silhouette, not only adjectives ("iridescent", "pirate"). When assets disagree, find whether the cause is spec, shader, lighting or geometry before commissioning a full remake. | Costume complexity for the whole game from a cosmetic set. Invented counts of concept-jam days or rejected masks. |
| SC-HS-L | 245, 247 | Give each effect one semantic job: availability, confirmation, danger, success, rarity, celebration. Check that brightness and motion do not imply urgency or "best move" that the mechanic lacks. Recurring UI effects get less visual demand than short decisive events. Write audio direction beside visual direction. | Turn-based timing freedom. Copy the signal-to-meaning match, not the length or density of the sequences. |
| SC-BS-L | 253, 255 | Review icon, thumbnail, title treatment, loading screen and in-game UI as one family at real display sizes. Name the recognition anchors that must survive a refresh. Ask if the most prominent word, shape or character is the one players should remember. Keep one marketing sheet using approved production assets and vocabulary. | A claim that Brawl Stars rebuilt its in-game style, or that a redesign lifts click-through. Test the project's own marketing assumptions. |

## 8. Supplemental teaching sources (AP:257-277)

| ID | AP | Statement (paraphrase) | Prov | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| TS-LU | 261 | Pixar's Luca production notes: rounded underwater forms contrast with Portorosso's more rectilinear structures. Leaning, sagging, twisting buildings tie to age and history, not random distortion. Graphics direction keeps environment and signage contrast below character contrast. Warm/cool choices were coordinated; cooler local colors were adjusted when warm light muddied the result. Cited especially PDF pages 27-31. Key quote: "The characters should have the highest contrast" | DEV-ACC (press kit) | EXPERIENCE | C14, 2021 (file revision 2021-06-04) |
| TS-LU-L | 263 | PAPER: use deformation to express construction, age or culture, not as a random "stylized" filter. Separate a color's intended emotional role from the raw texture value that makes it under a light; check the lit result. Film controls framing; Roblox players often control the camera, so test hierarchy across reachable viewpoints, not one frame. | PAPER | OPINION | O00 |
| TS-GU | 267 | James Gurney: color-wheel masking limits the available color region to organize an image; the mask admits some colors and excludes others. A separate demo uses nine swatches as an example of the exercise, not a rule of nine colors. | DEV-ACC (artist blog) | EXPERIENCE | C11, 2022-05-05; C12, 2011-09-16 |
| TS-GU-L | 269 | PAPER: define the dominant gamut for an area; reserve out-of-gamut colors for deliberate emphasis. Local palettes may shift with story and light under one global identity. Count role assignments and exceptions before swatches: a few swatches still compete if every object gets equal saturation and contrast. No universal palette count is set by these sources. | PAPER | OPINION | O00 |
| TS-GU-S | 271 | Scope: the public posts were read, not the full text of Gurney's "Color and Light". They support only the masking discussion; no invented quotes or page refs. | PAPER | VERIFIED | C11-C12 |
| TS-MM | 275 | Design Studio Press lists "Framed Ink" by Marcos Mateu-Mestre: 128 pages, August 2010, ISBN 978-1-933492-95-7; publisher says it covers composing images and visual storytelling. The book itself was not read. | S-DOC (publisher page) | VERIFIED | C13, book Aug 2010; page acc 2026-10-21 |
| TS-MM-L | 277 | PAPER: further reading on staging and narrative composition. Not authority for Roblox interface sizes, camera settings or contrast percentages. | PAPER | OPINION | O00 |

## 9. Number register (AP:1-358)

Every number with scope, the paper's "legitimate use" and "invalid inference" (AP:289-309). Extra rows carry numbers that appear only in the prose.

| ID | Value | Scope (source, game, what it counts) | AP | Legit use (paper) | Invalid inference (paper) | Tag | Src, date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| N01 | 59 portraits; 68 models; 194 boon icons; 1,400 environment textures | Hades, reported shipped output | 199, 293 | Show breadth of coordinated production | Minimum asset counts for a successful Roblox game | EXPERIENCE | C02, 2021-06-07 |
| N02 | 32,494 effects frames; 942,489 character/enemy animation frames | Hades, reported shipped output | 199, 295 | Attribute reported production volume | Convert to runtime duration without playback information | EXPERIENCE | C02 |
| N03 | "more than doubled" joints and animations | Mario Wonder vs previous Mario title; no absolute counts | 217, 297 | Report an explicit relative change | Invent the absolute count | EXPERIENCE | C05, 2023-10-17 |
| N04 | final six months to a year | Mario Wonder, when unified direction became clear (retrospective) | 217, 299 | Describe that production | A mandatory schedule for all projects | EXPERIENCE | C05 |
| N05 | Indirect Lighting Intensity 2.0 | Fortnite Ch4, Epic's Lumen setup | 225, 301 | Show an intentional non-physical adjustment | A Roblox Lighting property or a universal multiplier | EXPERIENCE | C06, 2023-01-26 |
| N06 | 60 fps; 4 ms for GI plus reflections | Fortnite Ch4, console target | 225, 303 | Explain one project's tradeoff | A mobile Roblox budget | EXPERIENCE | C06 |
| N07 | three costume stages | Sea of Thieves Ravenwood set | 233, 305 | Explain intentional variation | A standard number of cosmetic tiers | EXPERIENCE | C07, 2023-03-03 |
| N08 | nine swatches | Gurney demonstration | 267, 307 | Reproduce that teaching exercise | A universal palette limit | EXPERIENCE | C12, 2011-09-16 |
| N09 | 128 pages; August 2010 | Framed Ink publisher metadata (ISBN 978-1-933492-95-7) | 275, 309 | Accurate reading reference | Proof the book was read | VERIFIED | C13, acc 2026-10-21 |
| N10 | 4 districts (plus 3 lanes) | Deadlock City Never Sleeps content | 57, 99 | This update's shipped content | An optimal or recommended map size | VERIFIED | V01, 2026-09-29 |
| N11 | 9 class silhouettes validated | TF2 original roster, no internal shading | 111, 127 | Scope of that validation | That a novice understands roles from silhouettes; a Roblox target | EXPERIENCE | V08, 2007 |
| N12 | Half-Lambert scale 0.5, bias 0.5, exponent 1 | TF2 renderer | 113, 129 | Renderer-specific settings | Luminance targets, contrast ratios, Roblox lighting values | VERIFIED | V08, 2007 |
| N13 | "not published" counts of explorations and meetings | TF2 Demoman post | 117, 131 | None needed | A "three directions" rule | EXPERIENCE | V10, 2008-08-28 |
| N14 | none established: Deadlock palette count, gray bands, silhouette pixels, review quota, phone budget | Deadlock searches to 2026-10-21 | 95, 105 | Mark as unknown | Treat as proof none exist, or invent them | research limit | O00 |
| N15 | none established: universal silhouette pixel size; contrast ratio; quality score; style-guide pages; rejected sketches; approval headcount; outsourcing rounds | Valve, Riot, and others | 143, 313, 353 | Mark as unknown; set project policy and label it proposed | Present project targets as studio facts | OPINION | O00 |
| N16 | no exact value bands or palette counts | Rift visual style charts | 177 | Relative constraints only | Reading hard bands | EXPERIENCE | R04 |
| N17 | no sample sizes, scores or revenue effect | Brawl Stars logo test | 251 | Direction only | A conversion guarantee | EXPERIENCE | C10, 2025-08-24 |

## 10. Game comparison: what to learn, what not to copy (AP:151-159, 317-339)

The paper says the table is OPINION O00 grounded in the studio reports. It is not a ranking and does not claim another studio's implementation is available in Roblox (AP:317). "Prov of the lesson" is PAPER in every row.

| ID | AP | Game (studio) | What to learn | What not to copy | Src |
| --- | --- | --- | --- | --- | --- |
| CG-DL | 153, 321 | Deadlock (Valve) | A premise linking places, factions, characters, actions, presentation | Unverified internal rules or shader recipes; fan concepts as authority; desktop complexity unchanged on phones | V01-V06 (VERIFIED descriptions), OPINION transfer |
| CG-TF | 155 | TF2 (Valve) | Readable silhouettes; limited visual noise; art and tech serving direction together | Source-engine equations as Roblox settings; specific copyrighted characters | V08 (EXPERIENCE/VERIFIED), OPINION transfer |
| CG-D2 | 157 | Dota 2 (Valve) | In-context readability; rest and detail hierarchy; explicit exceptions | A rigid three-color cap; a universal light-upper-body rule; approval from close-ups only | V11 (EXPERIENCE), OPINION transfer |
| CG-LL | 323 | League of Legends (Riot) | Keep identity and event importance across model, motion, VFX, sound | Every craft at max spectacle; the historical hierarchy as an absolute | R01-R04 (the paper's table lists R01-R04; R05 is cited in prose) |
| CG-OW | 325 | Overwatch (Blizzard) | Solve gameplay role and recognition before decorative polish | Specific costumes; an assumed universal hero-pipeline budget | C01 |
| CG-HD | 327 | Hades (Supergiant) | Tie visual anchors and color script to design and production needs | Dense linework as a premium look; output counts as productivity targets | C02 |
| CG-S3 | 329 | Splatoon 3 (Nintendo) | Derive props, brands, environments from a shared culture | Literal weapon forms; a rule that every game needs chaotic surfaces | C03/C04 |
| CG-MW | 331 | Super Mario Bros Wonder (Nintendo) | Compose character action for the real gameplay camera | Anatomical distortion without a camera and readability purpose | C05 |
| CG-FN | 333 | Fortnite Chapter 4 (Epic) | Balance stylized identity with selective physically based effects | Unreal-specific features or high-end lighting as Roblox defaults | C06 |
| CG-ST | 335 | Sea of Thieves Ravenwood (Rare) | Check outsourced materials and shapes in the engine | Assuming an approved handoff image guarantees the final shader result | C07 |
| CG-HS | 337 | Hearthstone (Blizzard) | Make emphasis and feedback express the real gameplay choice | Flashiness that signals the wrong priority | C08 |
| CG-BS | 339 | Brawl Stars (Supercell) | Evolve marketing identity with the product, deliberately | Treating a reported marketing test as a conversion guarantee | C10 |

## 11. From attractive work to coherent direction (AP:343-355) and the feedback example (AP:161-165)

| ID | AP | Statement | Prov | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| CO-1 | 345 | Art direction asks whether work belongs, what it should say, and how it relates to everything else the player meets. The AD needs a stable statement of the game's visual promise and a way to settle conflicts. Unexplained taste is not an instruction for an AI specialist. | PAPER | OPINION | O00 |
| CO-2 | 345 | Step: turn a preference into a comparison: which feature of the approved reference is missing, what player impression changes, what must stay untouched. | PAPER | OPINION | O00 |
| CO-3 | 347 | Do not build a style as a collage of prestige names. "Valve clarity, Riot polish, Pixar appeal" can be a research agenda, not a brief. Name the relationships to transfer: which shapes carry identity, where contrast is reserved, how materials separate at the camera, which details are cut, how much exaggeration the fantasy needs. A source game's exact costume, silhouette, interface or world identity is no substitute for an original direction. | PAPER | OPINION | O00 |
| CO-4 | 351-355 | Paper table: coherent system has no universal quality score (OPINION, O00, 2026-10-21); cross-craft gameplay recognition has no universal silhouette pixel size (EXPERIENCE, R01/R02, 2021-03-12 / 2021-04-09); use primary Deadlock evidence only within its scope, no complete public art bible established (OPINION, O00, 2026-10-21). | PAPER | mixed | R01, R02, O00 |
| FB-1 | 163, 165 | Feedback template (invented example): Priority; Evidence (named capture); Required outcome; who checks what (modeler proposes silhouette change, animator checks cue survives poses); returns (same-camera before/after sheet plus in-scene crop); what stays (approved material family); who decides (creative director). The capture "EXAMPLE-CAPTURE-17", the repair character and the enemy collector are hypothetical, written by the paper. It states an outcome, names the craft, and avoids vertex-edit orders and the untestable "looks less premium". | PAPER (invented example) | OPINION | O00 |

## 12. Source ids used in lines 1-358 (resolved from AP:1013-1695)

Key quotes are the register's own, 15 words or fewer, attributed to the source. "acc" = accessed by the paper.

| ID | Source | Date and limits | AP (register) | Paper tag | Key quote (register) |
| --- | --- | --- | --- | --- | --- |
| O00 | The paper's own proposed workflow, authored examples and synthesis | 2026-10-21; not an external study | 1015 | - | - |
| V01 | Valve, Deadlock "City Never Sleeps: major update" | 2026-09-29 | 1017-1023 | VERIFIED | "The neutrals you know have been replaced by a variety of creatures with new behaviors." |
| V02 | Valve, "Old Gods, New Blood" | 2026-01-22 | 1025-1031 | VERIFIED | "Glass, steel and stone... Order and power where once there was none..." |
| V03 | Valve, "City Never Sleeps: development note" (Steam announcement) | 2026-09-29 | 1033-1039 | EXPERIENCE | "core game itself before we moved onto more polish phases" |
| V04 | Valve, "Mind the Birds!" (Baba, Steam announcement) | 2026-10-06 | 1041-1047 | VERIFIED | "her trusty bench comes to life with a creak of metal" |
| V05 | Valve, "Make Your Move." (Solomon) | 2026-10-09 | 1049-1055 | VERIFIED | "he approaches the city as if it's one giant chessboard" |
| V06 | Valve, "Paint the Town" (Violet) | 2026-10-16 | 1057-1063 | VERIFIED | "wielding Living Ink that both empowers her bullets" |
| V07 | Jamaal Bradley, LinkedIn post, Professor Dynamo concept art | undated, relative timestamp only; acc 2026-10-21 | 1065-1071 | EXPERIENCE | "Original concept art of Professor Dynamo by my super talented colleague Vasili Zorin" |
| V08 | Mitchell, Francke, Eng, "Illustrative Rendering in Team Fortress 2" (Valve PDF) | 2007 | 1073-1079 | VERIFIED and EXPERIENCE | "High frequency detail is omitted where possible" |
| V09 | Eng, "Alpine Art Style" (teamfortress.com) | 2008-08-19 | 1081-1087 | EXPERIENCE | "without being so different that the characters felt out of place" |
| V10 | Eng, "A Grim Bloody Fable" (teamfortress.com) | 2008-08-28 | 1089-1095 | EXPERIENCE | "constant meetings between the artists and feedback from the team" |
| V11 | Valve, Dota 2 Workshop Character Art Guide | undated current guide; acc 2026-10-21 | 1097-1103 | EXPERIENCE | "give this view higher priority than how items look in the loadout" |
| R01 | Riot, "Clarity in League" | 2021-03-12 | 1105-1111 | EXPERIENCE | "the amount of attention an ability grabs should match its level of importance." |
| R02 | Riot, "Ask Riot: Let's Talk Clarity" | 2021-04-09 | 1113-1119 | EXPERIENCE | "we had to pull back in other places." |
| R04 | "Defining the Rift's Visual Style", MOBAFire reprint of a Riototown article | reprint 2014-11-11 | 1129-1135 | EXPERIENCE | "It should clarify game space, not clutter it." |
| R05 | Riot, "A Story of Fog and War" | 2016-05-13 | 1137-1143 | EXPERIENCE | "without increasing the minimum required hardware spec." |
| C01 | Blizzard, "What It's Like to Work on Overwatch as a Concept Artist" | undated; acc 2026-10-21 | 1265-1271 | EXPERIENCE | "finding visual solutions to gameplay problems" |
| C02 | MCV, "Behind the art of Hades" | 2021-06-07 | 1273-1279 | EXPERIENCE | "we're first and foremost a game design-led team" |
| C03 | Nintendo, Ask the Developer Vol. 7 Splatoon 3, Part 1 | 2022-09-07 | 1281-1287 | EXPERIENCE | "we depicted the world based on street culture" |
| C04 | Nintendo, Ask the Developer Vol. 7 Splatoon 3, Part 2 | 2022-09-07 | 1289-1295 | EXPERIENCE | "look like a Splatoon weapon, without making it look like a firearm" (cut from the register quote to stay under 15 words) |
| C05 | Nintendo, Ask the Developer Vol. 11 Mario Wonder, Part 2 | 2023-10-17 | 1297-1303 | EXPERIENCE | "we had to find the right balance" |
| C06 | Epic, "Lumen Brings Real-Time Global Illumination to Fortnite Battle Royale Chapter 4" | 2023-01-26 | 1305-1311 | EXPERIENCE | "prevent indoor areas from becoming too dark for gameplay purposes" |
| C07 | Rare, "From Concept to Cosmetic: The Ravenwood Set" | 2023-03-03; read via search-index text after direct page 403 | 1313-1319 | EXPERIENCE | "Keeping a good silhouette and maintaining good colour was vital here" |
| C08 | Blizzard, "Hearthside Chat: Visual Effects" | 2018-10-26 | 1321-1327 | EXPERIENCE | "gameplay always comes first" |
| C09 | Blizzard, Hearthstone sound team feature | 2023-06-09 | 1329-1335 | EXPERIENCE | "what's the emotional impact of this card?" |
| C10 | Supercell, "Brawl Stars Logo Is Changing!" | 2025-08-24 | 1337-1343 | EXPERIENCE | "This change is an evolution of our logo, not a rebranding." |
| C11 | Gurney, "Color Wheel Masking Basics" | 2022-05-05 | 1345-1351 | EXPERIENCE | "The mask reveals only the colors we want in the picture" |
| C12 | Gurney, "Part 3: The Gamut Masking Method" | 2011-09-16 | 1353-1359 | EXPERIENCE | "a set of nine swatches" |
| C13 | Design Studio Press, "Framed Ink" | book Aug 2010; page acc 2026-10-21 | 1361-1367 | VERIFIED | "drawing and composing a single image" |
| C14 | Pixar/Disney press kit, "Luca Production Notes" | 2021; PDF filename revision 2021-06-04 | 1369-1375 | EXPERIENCE | "The characters should have the highest contrast" |
| A02 | OpenAI, image generation guide | undated live doc; acc 2026-10-21 | 1385-1389 | VERIFIED | "the model may occasionally struggle to maintain visual consistency" |
| A06 | W3C WCAG, relative luminance definition | undated live; threshold corrected May 2021; acc 2026-10-21 | 1417-1421 | VERIFIED | "normalized to 0 for darkest black and 1 for lightest white" |
| A08 | Microsoft, Xbox Accessibility Guideline 103 | undated live; acc 2026-10-21 | 1433-1437 | VERIFIED | (long; see register) |
| A13 | "Can Vision Language Models Assess Graphic Design Aesthetics" | 2026-03-01 | 1473-1477 | VERIFIED | "highly subjective aspects of design, such as creativity, are not included" |
| P03 | Roblox Creator Docs, Test on hardware | undated live; acc 2026-10-21 | 1529-1533 | VERIFIED | "emulation can't fully replicate what happens on real hardware" |
| P05 | Roblox Creator Docs, Implement designs in Studio | undated live; acc 2026-10-21 | 1545-1549 | VERIFIED | "select Actual Resolution" |

R03 ("Scouting out Teemo", 2024-09-23) is in the register but not cited in lines 1-358.

## 13. Claims for the fact-check

Prioritized: Deadlock first, then League, then other Valve, then numbers, then the rest. Fact-check against the source at the id, not against the paper. "Why" says what breaks if the claim is wrong.

| ID | Claim (paraphrase) | AP | Src | Src date | Why it matters |
| --- | --- | --- | --- | --- | --- |
| FC01 | V01 lists 3 lanes (Broadway, Greenwich, York) and 4 districts (Theater, Chinatown, Haunted Lot, Plaza) | 57, 99 | V01 | 2026-09-29 | Names and counts feed the "district" lesson and the number N10 |
| FC02 | V01: neutral creatures redesigned as "Haunts"; occult university and Wall Street warlock landmarks | 57 | V01 | 2026-09-29 | Anchors the "recognizable institution + one premise" reading |
| FC03 | V01: health bars and status presentation changed; parry indicator near reticle; enemy UI color adjustable | 57 | V01 | 2026-09-29 | Used as proof that presentation is part of the world rule and that color needs redundancy |
| FC04 | V01: Sunken Plaza outside sound muffled and drains stamina | 57 | V01 | 2026-09-29 | Only cited example of sound/gameplay tied to a place |
| FC05 | V02: Hidden King described via skyscraper shadow, boarded housing, city's cracks; Archmother via glass, steel, stone, order, power; Patrons, bases, troopers, defensive abilities overhauled | 65 | V02 | 2026-01-22 | Basis for the faction-contrast lesson; check wording is Valve's description, not fan reading |
| FC06 | V04: Baba = Central Park pigeon lady; tea, birds, yarn; bench mobile in combat | 73 | V04 | 2026-10-06 | Basis for the signature-object lesson |
| FC07 | V05: Solomon's chess names map to bishop offense, knight protection/retreat, rook advance, queen lockdown | 77 | V05 | 2026-10-09 | Basis for the motif-organizes-actions lesson; mapping must be exact |
| FC08 | V06: Violet's Living Ink, Flow State, Still Life, Abstract Landscape tied to artist identity | 81 | V06 | 2026-10-16 | Basis for the ability-family lesson |
| FC09 | V03: core work before polish; several systems in parallel; Midboss, Guardians, Walkers later; hero remodels expected later; speculative features depend on playtests | 87 | V03 | 2026-09-29 | Basis for asset-status review; check "remodels" and the later items |
| FC10 | V07: post credits Professor Dynamo concept art to Vasili Zorin; poster is a colleague | 93 | V07 | undated | Credit only; check the poster's role and the claim it is not Valve-wide attribution |
| FC11 | No complete public Deadlock art bible, palette count, gray bands, silhouette minimum, review quota or phone budget exists | 95, 105 | O00 | 2026-10-21 | If one exists, many "unknown" rows change; owner relies on Deadlock most |
| FC12 | R01: clarity priorities (communicate gameplay, importance hierarchy, limit noise) | 171 | R01 | 2021-03-12 | Core of the League lesson |
| FC13 | R01: champion needs identity silhouette feature, facing, source of power | 171 | R01 | 2021-03-12 | Basis for LL-C3 |
| FC14 | R01: animation can become a constraint when it carries identity (Lee Sin) | 171 | R01 | 2021-03-12 | Check that Lee Sin is the article's own example |
| FC15 | R01: spell emphasis ranked by damage, crowd control, dodgeability, change to opponent play | 171 | R01 | 2021-03-12 | Basis for LL-C1; check exact list |
| FC16 | R01: large telegraph implying a dodge chance that is not real miscommunicates | 171 | R01 | 2021-03-12 | Basis for LL-C2 |
| FC17 | R01: shared clarity allowance across model, animation, VFX, audio; base-versus-skin parity | 171 | R01 | 2021-03-12 | Basis for LL-C5, LL-C6 |
| FC18 | R02: Space Groove Blitz+Crank kept hands/head/shoulders and can walk floatier; Lancer changed other cues; earlier decision predated the framework | 185 | R02 | 2021-04-09 | Model for feedback without micromanaging; check skin names and the admission |
| FC19 | R04: Rift visual style: painterly yet graphic forest, foliage vs rock, environment < champions < effects < UI, painted edges and alpha to disguise geometry | 177 | R04 | 2014-11-11 (reprint) | Original date and author unseen; reprint provenance |
| FC20 | R05: map update had to improve visuals without raising the minimum hardware; fog of war looked poor on the new map | 179 | R05 | 2016-05-13 | Basis for the neighbor-systems lesson |
| FC21 | V08: 9 TF2 class silhouettes validated without internal shading | 111, 127 | V08 | 2007 | Number with scope; note paper tags EXPERIENCE here and VERIFIED for the next claim |
| FC22 | V08: Half-Lambert scale 0.5, bias 0.5, exponent 1 (older exponent 2 in the source) | 113, 129 | V08 | 2007 | Exact parameters; check what "older exponent 2" refers to |
| FC23 | V08: cool shadows not black, rim highlights, reduced high-frequency detail, restrained repetition, RED/BLU warm natural vs cool industrial contrast | 111 | V08 | 2007 | TF2 aesthetic summary used for transfer |
| FC24 | V09: Alpine theme answered desert fatigue; reused structures; cooler foliage/rock colors | 121 | V09 | 2008-08-19 | Basis for the biome-extension lesson |
| FC25 | V10: claymation tried and rejected; Demoman by biography and meetings; no counts | 117 | V10 | 2008-08-28 | Check the claymation/material-simulation statement |
| FC26 | V11: gameplay view over loadout; darker lower to lighter upper default; key colors blended; rest areas; in-context evaluation | 139 | V11 | undated | Guide is undated; confirm current wording; paper tags a Valve guide EXPERIENCE |
| FC27 | C02 Hades counts: 59 portraits, 68 models, 194 boon icons, 1,400 textures, 32,494 effects frames, 942,489 animation frames | 199, 293, 295 | C02 | 2021-06-07 | Large exact numbers |
| FC28 | C02: tone change from painterly to pen-and-ink (Mignola, Taylor) judged more efficient | 199 | C02 | 2021-06-07 | Check who made the efficiency claim |
| FC29 | C05: joints and animations more than doubled; unified direction in last 6-12 months (Kondo) | 217, 297, 299 | C05 | 2023-10-17 | Relative number and timeline scope |
| FC30 | C06: Indirect Lighting Intensity 2.0; 60 fps console; 4 ms GI plus reflections; Skylight Leaking; Diffuse Color Boost; Local Exposure | 225, 301, 303 | C06 | 2023-01-26 | Exact engine numbers and names |
| FC31 | C07: three costume stages; Ravenwood details | 233, 305 | C07 | 2023-03-03 | Read via search-index text after a 403; verify on the real page |
| FC32 | C08/C09: Hearthstone effect and sound statements (Floop, Magnetic, Priest, emotion over literal) | 241, 243 | C08, C09 | 2018-10-26; 2023-06-09 | Names and decisions |
| FC33 | C01: Overwatch concept details (Shield Guy, Honeydew Mei, Ana coat, Sigma) | 191 | C01 | undated | Source undated |
| FC34 | C03/C04: Splatoon 3 culture shifts, Stringer, Splatana Stamper, weapon-not-firearm quote | 207, 209 | C03, C04 | 2022-09-07 | Quote and prop origins |
| FC35 | C10: Brawl Stars logo is an evolution; no test numbers published | 251 | C10 | 2025-08-24 | "No sample sizes" claim must be checked |
| FC36 | C14: Luca notes (rounded vs rectilinear, aging buildings, environment contrast below character contrast), pages 27-31 | 261 | C14 | 2021 | Page range |
| FC37 | C11/C12: Gurney masking; nine swatches is only a demo | 267 | C11, C12 | 2022-05-05; 2011-09-16 | Number scope |
| FC38 | C13: Framed Ink 128 pages, Aug 2010, ISBN 978-1-933492-95-7 | 275 | C13 | Aug 2010 | Exact bibliographic data |
| FC39 | A02: image model may struggle to keep visual consistency | 25 | A02 | undated | Backs rule 3; check what it says |
| FC40 | A13: VLM aesthetics paper excludes subjective aspects such as creativity | 33 | A13 | 2026-03-01 | Backs rule 7 |
| FC41 | A06: relative luminance definition (0 to 1) | 35 | A06 | undated | Rule 8 cites a definition only |
| FC42 | A08: Xbox guideline 103 on multiple sensory channels | 37 | A08 | undated | Backs rule 9 |
| FC43 | P03/P05: emulation does not fully replace real hardware; Studio "Actual Resolution" | 49 | P03, P05 | undated | Backs rule 15 |

## 14. Contradictions and limits

### 14.1 Where the paper says its sources qualify each other (AP:279-287, 145-149)

| ID | AP | Item | Handling for skills |
| --- | --- | --- | --- |
| X01 | 281 | No proven "finish the style first" order. Hades stresses adapting art to gameplay and story; Mario Wonder's retrospective describes late convergence. Not controlled competing methods (paper's interpretation of C02 and C05). | Warn against both early rigidity and endless undocumented change. Keep an approved current target plus recorded reasons to reopen it. |
| X02 | 283 | Fortnite lighting and Mario's camera-facing deformation are both deliberate non-literal choices. They do not license ignoring all physical or geometric consistency (interpretation of C05-C06). | Any exception needs a named benefit in the final player view. |
| X03 | 285 | Shared direction is not identical treatment. Splatoon cultures evolve, Hearthstone classes differ, Ravenwood varies within a set (interpretation of C03-C04, C07-C08). | Cohesion = consistent relationships among differences. Do not flatten all to one palette. |
| X04 | 287 | Marketing evidence is thinner than craft evidence. Supercell gives no numeric impact (interpretation of C10). | Keep recognition and test alternatives; never promise revenue. |
| X05 | 147 | TF2 silhouette proof vs Dota silhouette allowance; Dota value gradient vs dark-headed designs. Same objective, conditional means (V08/V11). | Treat aim as firm, means as conditional unless the creative director locks them. |
| X06 | 149 | Deadlock temporary-asset variety vs TF2 compatibility need (V03/V09). | Status-aware reviews; final scenes still need coherence. |
| X07 | 185 | R02 itself says the Lancer decision predated the clearer framework. | Do not present Riot's clarity framework as applied uniformly to older skins. |

### 14.2 Limits on the evidence (Deadlock, League, others)

| ID | AP | Limit | Handling for skills |
| --- | --- | --- | --- |
| X08 | 95 | No complete public Deadlock art bible, palette count, gray bands, silhouette minimum, review quota, phone budget, or full production account found. Fan redesigns and portfolio posts are not Valve-approved. | Cite Deadlock only for DL-01 to DL-10. Never say "Valve's rule is...". Mark every other Deadlock statement as proposed. |
| X09 | 57 | V01 items are documented features, not proof that players read them correctly. | Documented does not equal effective. |
| X10 | 67 | The faction sub-rules (upkeep, massing, surface, sound, ceremony) are the paper's extrapolation, not Valve's. | Label as PAPER. |
| X11 | 59, 163 | "Seaside repair town runs on bottled weather" and "EXAMPLE-CAPTURE-17" are the paper's invented examples. | Never treat as data or as studio material. |
| X12 | 93 | V07 is one individual's post, undated, supports one credit only. | Do not use for direction claims. |
| X13 | 87-89 | V03 is a studio note about priorities; "mixed fidelity is not absent direction" is the paper's reading. | Keep asset status in reviews. |
| X14 | 113 | Half-Lambert numbers are renderer parameters, not light targets. | Never transfer to Roblox. |
| X15 | 139 | V11 is an undated live guide; the paper tags it EXPERIENCE. Its limits apply to its own rendering context. | Re-read the live guide before quoting. |
| X16 | 143, 313 | No universal silhouette size, success percent, contrast ratio, count of sketches or approvals in the sources. | Project thresholds must be labeled proposed policy and tested. |
| X17 | 173 | Priority-contract questions are not Riot thresholds. | Label as PAPER. |
| X18 | 177 | R04 comes from a third-party reprint of a Riototown article; provenance limit stated; no value bands or palette counts measured. | Cite as reprint. Do not state hard bands. |
| X19 | 181 | The environment-champion-VFX-UI order is not an unconditional law; the focal subject depends on the interaction. | Declare the current interaction first. |
| X20 | 179 | R05 is an engineering retrospective; the art-update lesson is the paper's reading. | Use as a reminder to re-check neighbor systems. |
| X21 | 233 | C07 was read through search-index text after the direct page returned 403. | Re-verify before relying on details. |
| X22 | 225 | Fortnite screenshots cannot show temporal behavior (C06's own note). | Test moving-camera exposure. |
| X23 | 261, 263 | Luca is a film with controlled framing; Roblox players control the camera. | Test reachable viewpoints. |
| X24 | 271, 275 | Gurney's book and Framed Ink were not read; only public posts and publisher metadata. | No book-level claims. |
| X25 | 251 | Brawl Stars post has no sample sizes, scores, controls or revenue effect. | No conversion promise. |
| X26 | 217 | Mario: absolute joint counts not given; Kondo's timeline is a retrospective. | Do not invent counts or schedules. |
| X27 | 35 | Rule 8 cites A06, a relative-luminance definition. The register quote backs only the 0-to-1 definition, not the "complementary diagnostics" advice (extractor's note). | Treat the diagnostic advice as OPINION. |

### 14.3 What the paper says it did not do (AP:17, 313, 345-347)

| ID | AP | Not done or unknown |
| --- | --- | --- |
| X28 | 17 | Did not generate or benchmark reference images, build a Roblox scene, run a player study, or measure a submitted screenshot. Every procedure is a proposed check. |
| X29 | 17 | Where no defensible universal threshold exists, it gives a method, not a number. |
| X30 | 313 | Does not establish a standard number of rejected sketches, style-guide pages, outsourcing feedback rounds, approvers, or exact universal contrast ratios. Team targets must be labeled proposed policy and tested on the game. |
| X31 | 95 | Does not reconstruct unseen footage or shader settings for Deadlock. |
| X32 | 347 | "Valve clarity, Riot polish, Pixar appeal" is a research agenda, not an executable brief. |
