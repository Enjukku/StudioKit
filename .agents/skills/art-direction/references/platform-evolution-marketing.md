# Phones and Roblox rendering, evolving a style, marketing art, don'ts

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `art-direction`. Sources: `knowledge/reference/art-direction/03` §1.4, `04` §1-3, §4.6; fact-check `fact-check-a11y-ai-roblox.md` (FC-A). Roblox facts are dated snapshots: re-check the local docs mirror (`knowledge/external/roblox-creator-docs/`) before relying on one.

## 1. Stylization on Roblox phones
### 1.1 Who plays and on what
| Fact | Scope | Use | FC-A |
| --- | --- | --- | --- |
| FY2025 daily active users by platform: mobile 83 %, desktop 14 %, console 3 %; 127 M average DAU | Roblox annual report, fiscal-year average; "mobile" includes tablets; not one game's audience | phones are the default review device | confirmed FR01 (FY average; Q2 2026 reported 123 M DAU) |
| Age-checked cohort, 7 days to 2026-06-30: 35 % under 13, 38 % 13-17, 27 % 18+; 57 % of DAU age-checked | Q2 2026 shareholder letter, estimates; not comparable with older self-reported ages | state this game's audience separately; never infer a childlike look from a platform average | confirmed FR02 |
| Roblox's hardware guide: emulation cannot fully replicate real hardware; pick a low-end baseline that represents the audience | Creator Docs, undated live page | a real-phone capture before claiming "reads on phones" | confirmed FR03 (also: Android about 65 % of a typical game's users, mostly 2-4 GB RAM) |

Pick the baseline phone from the game's analytics when they exist; otherwise write the assumed cohort into the bible's technical envelope and revise after testing (04:AU5).

### 1.2 Screen space is measured, not assumed
- Every review image records rendered width × height, orientation, FOV, crop, safe-area and HUD state, input mode and gameplay distance (`art-review/references/look-check.md` §1). A big desktop shot never certifies a small phone view (04:SS1).
- Studio's Device Emulator and "Actual Resolution" preview UI at emulated resolutions; useful, not a substitute for a device (04:SS1, FR04).
- Safe areas: `ScreenInsets` options decide whether content may sit behind cutouts and core UI; review important UI against the safe region and keep full-bleed decoration apart from controls (FR05: `CoreUISafeInsets` is the recommended mode for interactive UI; `None` only for non-interactive content). Test silhouettes with the thumb controls visible.
- Orientation: the bible lists supported orientations and control layouts; do not silently require both (FR06: landscape by default; LandscapeSensor, Sensor, LandscapeLeft, LandscapeRight, Portrait).

### 1.3 Rendering facts the art director must know (snapshot, check FC-A)
| Area | What changes the delivered image | FC-A |
| --- | --- | --- |
| Lighting style | `LightingStyle` Realistic or Soft states the artistic intent (a renderer choice, not a quality grade); `PrioritizeLightingQuality` decides whether near lighting or view distance is kept as quality drops; `Lighting.Technology` / "Future" are superseded and not to be set; `ShadowSoftness` is documented for Realistic (Soft behavior untested) | FR07-FR11 (Unified Lighting fully live 2025-07-23) |
| Post effects | effects under Lighting are global, under Camera per player; some drop at lower quality; a tonemapper preset changes display color | FR12-FR13 (ColorGradingEffect works only under Lighting) |
| Emissive masks | surface glow is not a light on nearby geometry; "this glows" ≠ "this lights the room" | FR15 (2026-02-12) |
| Texture streaming | stored up to 8K is not rendered at 8K on a phone; some devices and texture classes stay lower; essential markings must not depend on fine texture | FR17-FR19: 4K via texture streaming only when the device has memory (about 3.5 GB on low-end Android and iOS); UI, terrain, sky and bundled materials not 4K at the 2026-03-23 snapshot |
| Distant models (SLIM) | far models may be replaced by lightweight stand-ins; compare landmark and silhouette reads near and far | FR20-FR23: SLIM is a Client Beta (no general release found 2026-10-21); models with a Humanoid and NPCs excluded; avatar SLIM is opt-in R15 only; debug tints show the state |
| Cost tools | Scene Analysis and MicroProfiler measure; their numbers need the target device | FR24-FR26 (Scene Analysis numbers need not match devices) |

### 1.4 Style as a cost decision
- "Premium" is not maximum detail: spend complexity where it changes recognition, material impression or emotion (04:SP1).
- Under a performance cut, protect in this order: identity silhouettes, distinguishing proportions, interaction affordances, color roles; microdetail goes first. Each cut states which visual role survives (04:SP2, PF3; P, a policy to test).
- No universal phone triangle budget, light count, palette size, simultaneous-effect cap or frame target exists; set them with the owner and engineering and measure on the baseline phone (04:PF3; `performance` skill).
- The art director owns the visual-cost conversation (what must survive), not a triangle-to-fps formula (04:PF2).

## 2. Evolving a visual style
1. Name the problem the change solves (inconsistency, unreadability, dated proportions, new camera or audience, stronger fantasy, production limit). Separate the identity players recognize from the implementation that may change (04:EV1).
2. Write a transition packet and test old and new assets in one scene (`art-review/references/art-bible.md` §6) (04:EV2-EV3).
3. Version identity locks apart from implementation; review a representative family, not one new asset; a rig or pose change can break an approved costume, so revisit motion and gameplay views (04:TS2; Riot's 2024 Teemo update reconciled inconsistent costume parts while keeping chosen older charm, S 04:TS1).
4. Across platforms the fantasy and recognition locks stay; controls, framing, feedback scale and density may be redesigned for the real interaction (Riot's Wild Rift adaptation kept a champion's fantasy and changed a hard-to-use mobile interaction, S 04:WR1; transfer P 04:WR2).
5. Dated style descriptions go stale: a 2014 description of a map's look does not describe its 2026 variants (04:TS3).

## 3. Marketing art that matches the game
| Surface | Job | Check |
| --- | --- | --- |
| Experience icon | identity at its real small size | square, upload at least 512×512; check at the small display size Roblox documents (150×150 example) with `tools/art/thumb_check.py` (the marketing agent's wrapper over `look_check.py`) (FR28) |
| Thumbnail | an activity or situation the game really has | 16:9, ideally 1920×1080; essential content clear of the bottom area metadata may cover; video thumbnails must show real in-game content (FR29) |
| Key art | composition and story of the fantasy | composed camera and light allowed; same identity and promise as the game |
- Marketing may compress and dramatize the fantasy but never invents another product; review it against the current game, not only the bible, and link each approved marketing anchor to the game version it shows (04:MK1-MK3).
- Name the recognition anchors that must survive any refresh (title word, shape, character, color). Review icon, thumbnail, title treatment, loading screen and in-game UI as one family at real sizes (Supercell's 2025 logo evolution, S 01:SC-BS; no conversion data was published).
- Click-through is not proof of better art direction; never borrow a competitor's image because it tested well (04:MK6).
- Marketing icons and thumbnails made with the image tool may ship as final images; the owner reviews every one before it ships (owner J009-D8). Game assets stay built, never shipped as images.

## 4. Don't
1. Call a generated reference consistent because it looks polished; check its views and construction.
2. Treat histogram similarity, palette count or edge density as proof of quality; a metric only locates a discrepancy tied to a task.
3. Apply an accessibility contrast ratio to world-art pixels outside its scope.
4. Make all assets equally saturated, bright, detailed or animated "for consistency".
5. Prescribe a specialist's technique when the need is a visual outcome.
6. Read a still as evidence of sound, motion, transitions or performance.
7. Use one attractive capture to claim support for all phones.
8. Silently replace an approved anchor or let a rejected concept become a reference.
9. Label a fan or paper reading as Valve's or Riot's production rule.
10. Market a different fantasy from the game players will get.
Source: paper do-not list (04:DN01-DN10, OPINION).
