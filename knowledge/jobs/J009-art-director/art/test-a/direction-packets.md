---
type: job
scope: game
status: draft
updated: 2026-10-21
source: "J009-T13 (lead brief); J003 pitch-set.md §3; skills art-direction, art-review, reference-images; test-a bibles, manifests, json/, diag/"
supersedes: []
---
> Author: art-director · claude-opus-5-5 · high · 2026-10-21

STATUS: needs-decision. Two directions are ready for the owner to pick by looking; I recommend B "Stormcut". No image reaches A yet (best: B-).

# Direction packets: Guard the Dragon Egg (J009-T13, direction test A)

Everything here is **PROPOSAL**. Nothing is approved; no anchors exist or were named. Look first: `side-by-side.png` in this folder (top row A, bottom row B; scene left, keeper right).

## 1. Brief restated
| Item | Value |
| --- | --- |
| Moment | night defence at the nest: keepers guard the giant glowing egg on a storm-swept ledge while sky thieves circle (J003 pitch §3, first image) |
| Must read first | (1) the egg, the heart of the camp; (2) the keepers, small but brave around it |
| Feeling | small but brave against the storm; night dangerous but readable |
| Camera | high three-quarter gameplay camera, about 45 degrees down (same CONCEPT LOCK text in both bibles) |
| Device | phone, landscape |
| Bible revision | explore-A rev 1 (`direction-a-bible.md`), explore-B rev 0 (`direction-b-bible.md`) |
| Anchors | none exist; none named; no anchor folder under `content/art/` (the tool attached 0 anchors on every call) |
| Excluded | 99 Nights in the Forest's look; franchise dragons; text |

## 2. What each direction changes (C2)
Both directions use the same subjects, the same identity text (`manifest-a.csv` and `manifest-b.csv` rows differ only by the direction letter) and the same camera clause. They differ on 5 of the 6 axes; camera reading is the same by design, for comparability.

| Axis | A "Hearthlight" | B "Stormcut" | Evidence |
| --- | --- | --- | --- |
| Proportion | chunky toy, about 3 heads tall, mushroom hood, mitten hands | lean heroic, about 5-6 heads, pointed hood, cape tails | silhouettes `diag/dragonegg-{a,b}-keeper.silhouette.png`; head counts by eye (approximate) |
| Material | soft and handmade: felt, knit, carved wood, copper; translucent porcelain egg | hard and carved: faceted slate slabs, plane-folded cloth, iron; pearl egg | the images |
| Density | high micro-detail: snow pillows, pebbles, knit patterns | larger calm planes: slab floor, bare stone | non-egg pixels at or above the egg's median luminance: A 0.37 × egg area, B 0.16 (`json/dragonegg-{a,b}-nest-competitors.json`) |
| Light | soft warm pool from the egg that spills onto pale snow | two temperatures: hard gold front light, cyan rim, indigo shadows | egg/ring median luminance ratio A 2.38, B 3.47 (`json/dragonegg-{a,b}-nest-value.json`) |
| Emotion | tender, cozy courage (a family keeping a baby warm) | mythic defiance (tiny heroes holding a line against a vast storm) | stances and faces in the images |
| World rule | all warmth on the mountain comes from the egg | the storm breaks everything into facets; only the egg (and what hatches) is smooth | bibles |

## 3. Packet A: "Hearthlight"
| Item | Content |
| --- | --- |
| Images | `content/art/refs/concept/dragonegg-a-nest.png` (try 2, 1536x1024) · `content/art/refs/character/dragonegg-a-keeper.png` (try 2, 1145x1374) |
| Gameplay problem it solves | makes guarding feel like caring: the egg is a hearth and the keepers are its family. Strong for young players and for the hatch payoff |
| Grayscale | `diag/dragonegg-a-nest.luminance.png`, `diag/dragonegg-a-keeper.luminance.png` |
| Phone thumbs | `diag/dragonegg-a-nest.thumb1170x540.png`, `.thumb844x390.png` (+ `-sheet.png`); keeper `diag/dragonegg-a-keeper.thumb1170x540.png`, `.thumb96x96.png` |
| Look-check JSON | `json/dragonegg-a-nest-value.json`, `-thumb1170x540.json`, `-thumb844x390.json`, `-competitors.json`; `diag/dragonegg-a-nest-p90-eggmask.json`; keeper `json/dragonegg-a-keeper-{value,silhouette,thumb1170x540,thumb96x96}.json` |
| Shape | everything round: rounded stones, snow pillows, a mushroom-hood keeper; the egg is set apart only by size, glow and its 3 cracks, not by shape |
| Value | the egg is the largest bright region (`p90` mask overlay), but the egg-lit snow in the bottom third is nearly as light as the egg (grayscale; competitors 0.0179 of the frame in the bottom third vs 0.0024 top) |
| Color roles | warm gold = egg and flames lit from it; cool blue-indigo = night; thieves dark against the clouds |
| Material | tactile felt and knit; porcelain egg reads warm and soft |
| Light | warm egg pool with cool fill; the warm rim on the keepers works |
| Hierarchy | 1 egg, 2 keepers (cream tunics on pale snow lose separation in grayscale), 3 torches and lanterns, 4 thieves |
| Appeal | the most likeable cast of the two; the keeper is charming and toy-like, and the ledge reads as a cozy diorama |
| Risks | (1) phone read: egg/ring ratio 2.09 at 844x390, snow competes; (2) felt, knit and fur micro-detail cannot survive on a phone (texture streaming lowers texture detail, platform-evolution-marketing.md §1.3), so the built game would fall far below this reference; (3) the look is a familiar animated-film / AI "cozy diorama" style, so "unmistakably its own" is hard to reach; (4) a 3-head body is far from players' own avatars if avatars are used |

**Grades (art-review feedback-briefs.md §1b; calibration: egg shop C-, anime summon B-; when unsure, the lower letter):**
| Image | Grade | One line |
| --- | --- | --- |
| dragonegg-a-nest | **C+** | egg reads first and the scene is cohesive and warm, but the finish is a generic AI cozy-diorama look, the foreground snow competes with the egg, it has 5 torches not 6, and the ground micro-detail cannot be built |
| dragonegg-a-keeper | **B-** | appealing, finished tactile materials and a strong round-hood silhouette (spear and lantern clear at 96 px); the face is a familiar animated-film type, not its own style |

## 4. Packet B: "Stormcut"
| Item | Content |
| --- | --- |
| Images | `content/art/refs/concept/dragonegg-b-nest.png` (try 2, 1672x941) · `content/art/refs/character/dragonegg-b-keeper.png` (try 1, 1024x1536) |
| Gameplay problem it solves | makes the egg read first by shape as well as light (the only smooth form among facets), so the hierarchy survives without bloom and at low quality; makes guarding feel heroic |
| Grayscale | `diag/dragonegg-b-nest.luminance.png`, `diag/dragonegg-b-keeper.luminance.png` |
| Phone thumbs | `diag/dragonegg-b-nest.thumb1170x540.png`, `.thumb844x390.png` (+ `-sheet.png`); keeper `diag/dragonegg-b-keeper.thumb1170x540.png`, `.thumb96x96.png` |
| Look-check JSON | `json/dragonegg-b-nest-value.json`, `-thumb1170x540.json`, `-thumb844x390.json`, `-competitors.json`; `diag/dragonegg-b-nest-p90-eggmask.json`; keeper `json/dragonegg-b-keeper-{value,silhouette,thumb1170x540,thumb96x96}.json` |
| Shape | faceted slabs, shard rocks around the nest, pointed hoods and cape tails; the egg's outline is the one smooth curve (faint facet lines remain on its shell) |
| Value | the egg is the brightest mass; its median luminance (0.510) is above the frame's 95th percentile (0.459); keepers are dark against lit stone in grayscale |
| Color roles | gold = egg and flames only; indigo-violet = night and stone; white-cyan = lightning only (held in the image) |
| Material | carved slate and folded-plane cloth; painterly gradients inside planes |
| Light | two temperatures (gold front, cyan rim, indigo shadows); the clouds are soft volumes, not the flat shapes the lock asks for |
| Hierarchy | 1 egg, 2 keepers (dark silhouettes in ready stances), 3 six torches, 4 thieves (dark against the clouds) |
| Appeal | heroic and graphic; the strongest game-screen read of the two; the slab floor looks playable |
| Risks | (1) the keeper is a generic realistic "hooded ranger" (fixed in the draft CHARACTER LOCK, untested); (2) faceted low-poly worlds are common on Roblox, so the identity rests on the smooth-egg rule and the two-temperature light; resemblance to 99 Nights not checked (no stills of it in this task); (3) the try-2 thieves are hooded and caped like the keepers (ally/enemy confusion at night; CREATURE LOCK in the draft); (4) a 5-6-head body is far from players' own avatars if avatars are used |

**Grades:**
| Image | Grade | One line |
| --- | --- | --- |
| dragonegg-b-nest | **B-** | clearest phone read, with its own grammar (faceted stone vs the glowing smooth egg) and all counts right; but faint facets on the egg, soft painterly clouds, hooded thieves and a slightly stock mobile-splash finish keep it from B |
| dragonegg-b-keeper | **C+** | strong pointed silhouette and faceted cloth that survive at 96 px, but the face and costume are a generic fantasy ranger; plain next to A's keeper |

## 5. Egg reads first at phone size (C3, diagnostics)
Phone check: each image fit by height into a landscape viewport, keeping aspect (Roblox `Camera.FieldOfView` is vertical, default 70, `knowledge/external/roblox-creator-docs/_api-reference/classes/Camera.yaml:265-269`, so a wider phone shows more world at the sides, not less height). The padding at the sides stands for world the image does not have. Sizes: 1170x540 (the brief's example) and 844x390 (iPhone-class landscape in points, closer to the physical size; a stress view). Filter: Lanczos (tool default). Egg mask: measured, never drawn (`diag/egg_masks.py`: seed = largest connected region of luminance ≥ the image's own p98, grown into connected pixels ≥ p90, holes filled); overlays `diag/dragonegg-{a,b}-nest-p90-eggmask-overlay.png` checked by eye. A's mask leaves out one dimmer upper-left patch of shell, which then counts as ring, so A's ratio is a low estimate. Ring: 8 px.

| Measure (no project tolerance exists: diagnostics only) | A full | A 1170x540 | A 844x390 | B full | B 1170x540 | B 844x390 |
| --- | --- | --- | --- | --- | --- | --- |
| egg / ring median luminance ratio | 2.38 | 2.09 | 2.12 | 3.47 | 3.06 | 3.14 |
| egg median luminance (WCAG Y) | 0.481 | 0.481 | 0.480 | 0.510 | 0.510 | 0.509 |
| egg bbox at the viewport (px) | — | 225x229 | 162x166 | — | 213x233 | 153x168 |
| egg area / frame | 0.070 | | | 0.057 | | |
| share of the frame's brightest 1 % inside the egg | 0.68 | | | 0.66 | | |
| egg = largest bright connected region (p98 seed) | yes (17,557 px; next 2,240) | | | yes (21,802 px; next 1,825) | | |
| non-egg pixels ≥ egg median, as a share of egg area | 0.37 (mostly bottom third: snow) | | | 0.16 (small: torches, lanterns, moon, lightning) | | |

Reading: in both images the egg is the largest bright region and holds about two-thirds of the brightest 1 % of pixels, so it reads first at both phone sizes. B separates the egg from its surround about 1.5 times more strongly than A at every size, and has less bright competition. These are measurements of two generated images, not of the game: a Studio capture at the real camera, lowest quality, busiest night is NOT REVIEWED.

## 6. Generated-image review (exploration.md §5)
| Image | Try | Views / construction | Counts and positions | Light | Substitution | Text / franchise | Reads small | Lock clauses broken | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a-keeper | 1 | ok | ok (lantern left hand, spear right) | ok | — | none | ok | head about 1/5 of height vs lock "1/3" (by eye) | rejected → `content/art/refs/character/_rejected/dragonegg-a-keeper-try1.png`; lock made explicit (explore-A rev 1) |
| a-keeper | 2 | ok | ok | ok | — | none | silhouette 1 component; hood, spear, lantern survive at 96 px | none seen | kept |
| b-keeper | 1 | ok | ok | ok | drifting toward a stock hooded ranger | none | 1 component; hood point and cape tails survive at 96 px | none (the face lacks stylization: lock tightened in the draft) | kept |
| a-nest | 1 | ok | 5 torches (asked 6) | ok | thieves drawn as dragons | none | — | egg crack network spends the crack-state ladder; ground and sky busy | rejected → `content/art/refs/concept/_rejected/dragonegg-a-nest-try1.png`; identity fixed for both (smooth egg, exactly 3 cracks, torch positions, thieves "not dragons") |
| b-nest | 1 | ok | 5 torches | ok | thieves drawn as dragons | none | — | egg faceted (B's key clause) | rejected → `content/art/refs/concept/_rejected/dragonegg-b-nest-try1.png` |
| a-nest | 2 | ok | 3 keepers in the named positions; 2 thieves; **5 torches** (counted by eye: upper left, left, upper right, right, front) | ok (egg key, moon fill) | fixed | none | yes (§5) | snow competes; torch count | kept (retry spent) |
| b-nest | 2 | ok | 3 keepers in place; 2 thieves; 6 torches (2 front, 1 each side, 2 behind) | ok (egg key, moon and lightning rim) | thieves hooded like keepers | none | yes (§5) | faint facet lines on the egg; soft cloud volumes | kept (retry spent) |
Counts and positions were made by eye on the full images; treat them as approximate (vision limits, art-review R-02). Regenerations: one per image for 3 of 4 images (a-keeper, a-nest, b-nest); b-keeper none. Total generation calls: 7.

## 7. What works (keep in whichever direction wins)
- The egg in the middle third, glowing from inside, with the keepers ringed around it: both images read "guard this" at phone size.
- Gold only for the egg and flames lit from it; cool night everywhere else (both).
- The thieves as dark winged shapes at the top edge, outside the egg's light: the threat reads without competing (both try-2 images).
- A: the round-hood toy keeper's appeal. B: the slab floor and shard nest, which already look like playable, buildable geometry.

## 8. Recommendation: B "Stormcut" (PROPOSAL)
- **Why:** it puts the egg first by two channels, shape (the only smooth form) and value, so the hierarchy holds on a phone without relying on glow (measured ratio 3.1-3.5 vs 2.1-2.4; bright competition 0.16 vs 0.37 of egg area). Its world rule gives every craft a job (facets for storm and threat, smooth curves for the egg and the hatchling). Faceted planes with gradients are a look Roblox can build from geometry, without fine textures that phones may not load, so the built game can stay close to the reference.
- **Trade-off:** A's keeper is the more likeable character, and A's tenderness suits the care-and-hatch fantasy and younger players. B gives that up for heroism.
- **What would change my view:** if the owner weighs character appeal over phone read, pick A. A then needs its snow and ground darker outside the egg's pool and less micro-detail (a lock change), and a built test to see how much of the felt look survives on a phone.
- **Path to A for B:** a stylized keeper face and costume (draft CHARACTER LOCK), thieves with their own wing-and-mask silhouette (draft CREATURE LOCK), a facet-free egg and flat graphic clouds (draft WORLD STYLE LOCK), then one regenerated pair of images under the draft bible at Gate 2.

## 9. Owner decisions needed
| # | Question | Options | Default if no answer |
| --- | --- | --- | --- |
| 1 | Which direction? | A "Hearthlight" · B "Stormcut" · B's world with A's chunkier keeper (one more keeper image) | B |
| 2 | Do players appear as their own Roblox avatars or in a keeper body? It decides whether CHARACTER LOCK proportions apply to players at all | own avatar + keeper gear · keeper body | open question to the game designer; locks scoped to NPCs and gear until answered |
| 3 | Anchor a01 (B nest image, composition and light only) | approve · wait for the rev-0 regeneration | wait: regenerate under the draft bible first, then propose anchors |
| 4 | Egg/ring value ratio as a project tolerance | set one after a Studio capture · none | none: diagnostics only |

## 10. Could not check
| Item | Needed | Who |
| --- | --- | --- |
| In-engine read at the real camera, lowest quality, busiest night | Studio captures (manifest per art-review look-check.md §1) | lead → environment-designer / Studio operator, after the pick |
| Real phone | device capture | lead |
| Resemblance to 99 Nights in the Forest | owner-supplied stills or captures to compare | owner / lead |
| Motion, sound, thief wind-up at night | clips and cue cards | NOT REVIEWED (no artifacts) |
| Player recognition of keeper vs thief | unlabeled identification test | not run |

```text
<spec>
coverage:
  - direction-a-bible.md: done (explore-A rev 1)
  - direction-b-bible.md: done (explore-B rev 0)
  - manifest-a.csv, manifest-b.csv: done
  - 4 images (2 per direction): done; 3 retries used (a-keeper, a-nest, b-nest)
  - image review (exploration.md §5): done, §6
  - phone check (value + thumb) per image: done, 1170x540 and 844x390 for scenes, 1170x540 and 96x96 for keepers
  - direction-packets.md: done (this file)
  - art-bible-draft.md (rev 0, direction B): done
  - Studio / device / motion / sound checks: not done (out of scope, no artifacts)
checks: {C1: pass (4 images in content/art/refs/{concept,character}/, 3 try-1 images in _rejected/, all reviewed §6), C2: pass (5 axes, §2), C3: pass as diagnostics (egg = largest bright region, ratio 2.09-3.47 at phone sizes, §5 JSON paths), C4: pass (python tools/art/art_refs.py --bible knowledge/jobs/J009-art-director/art/test-a/art-bible-draft.md print knowledge/jobs/J009-art-director/art/test-a/manifest-a.csv → exit 0; 12 families, 13 locks)}
decisions_made: [directions A Hearthlight / B Stormcut, same camera in both, keeper image attached as input to its own scene, thieves added to the scene as masked glider raiders (placeholder design), phone fit by height (vertical FOV), measured egg mask p98 seed + p90 grow]
proposals: [both world rules, all locks, anchor a01 candidate, color roles, cross-craft contracts in the draft]
questions: see §9
</spec>
```
