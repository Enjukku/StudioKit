> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit reference: universal. J008. Sources: environment paper notes `knowledge/reference/environment/01-place-guidance-scale-light.md` (rows RU06-RU07, K02, K07, L, A) and `03-pipeline-performance-review.md` (W06, PF11); property facts checked in `fact-check-lighting.md` (LF, LX rows). Values and recipes live in `environment-craft/references/studio-light-air.md`. Tags: **V** VERIFIED, **E** EXPERIENCE, **O** OPINION, **U** UNKNOWN.

# Light and air: what they must do

Light and atmosphere do two jobs at once: they set the **mood** of the art target and they keep the place **readable** for play. When the two fight, readability wins and the conflict goes to the art director.

## 1. Light
| ID | Practice | Evidence |
| --- | --- | --- |
| LA-01 | **Light is composition.** It draws the eye to the focal point and the next route choice. | RU06 O; G04 O |
| LA-02 | **Light supports a route; it never creates one.** A mandatory route, hazard or exit stays readable when optional light, shadows or post effects are gone (low quality, weak phone). Light makes it nicer; shapes make it possible. | L07 O (from P03 V) |
| LA-03 | **Leading light must end somewhere useful.** Lamps that lead to the exit help; an equally strong row that leads to a dead wall competes. A bright cave mouth pulls the eye and can hide what is behind it; whether that is right is the game designer's pacing call. | G04 O |
| LA-04 | **Every light has a visible reason.** Match the light's shape to its fixture (a lamp radiates, a spot aims, a window face spills). Record each light's position, range and shadow state in the scene manifest. | L09 O; L08 V |
| LA-05 | **Interiors must not go too dark.** Dark interiors and big exposure jumps at doors are common failures when lighting gets more physical. Prefer cheap global controls (ambient, environment light, exposure) before many shadowed local lights. | K01-b E (Riot); K07-a E (Epic) |
| LA-06 | **Accept lighting across every state, not one sunny angle.** List the outdoor-to-indoor thresholds, doors, time of day, weather and events that change readability, and capture each one. | K07-c O |
| LA-07 | **Review at the supported graphics tiers.** Quality level changes draw distance, shadows, textures, particles and post effects, and the exact behavior depends on the device. Compare captures at low and high quality, and on a real phone; one editor beauty shot proves nothing. | L06 V; RU06 O; PF11 V; DN09 O |
| LA-08 | **Pick the lighting style from the art target, then test it.** Neither the soft style nor the realistic style is automatically "the phone setting". Approve the value structure and silhouettes first; spend on costly shadow detail after. | L10 O |
| LA-09 | **No light-count rule exists.** No source gives a universal number of lights or shadow casters for phones. Approve the look and the degraded readability; budget lights from a phone measurement. | L13 O; BT06 U; LF31 |

## 2. Atmosphere, fog, sky, post effects
| ID | Practice | Evidence |
| --- | --- | --- |
| LA-10 | **Depth haze is not information fog.** Haze may suggest distance and mood; it must never hide something the player needs (a route, an enemy, an edge). A true gameplay boundary stays crisp even when the air is soft. | RU07 O; K02-b E (Riot); K02-d O |
| LA-11 | **Sky, atmosphere and clouds are one palette and one horizon.** Compose them together. Cloud cover does not mean rain, wind audio or a weather state unless the shared environment state says so. | A05 O |
| LA-12 | **Post effects are seasoning.** They can change or vanish at low quality, and they affect everyone unless they are per camera. The art direction must survive without them. | A08 V; AS3 V+O |
| LA-13 | **Tutorial values are experiments, not presets.** Official samples (a cool morning, a warm evening, a hazy cabin) worked in one scene with its own geometry and sky. Start from them if useful, re-derive each value against the art bible, and check on a phone. Keep `source_recipe` apart from `project_approved_settings` in the manifest. | A09 V/O; A11 O; W06 O |
| LA-14 | **No biome presets exist.** There are no validated fog, light or post values for "mountain", "swamp", "cave" or "storm". They come from this stage's geometry, navigation needs and art target. | A12 U; RC5 U |

## 3. Diagnosing a lighting problem (classify before fixing)
**Who decides what:** the art director sets the look target and style limits; the environment designer owns the lighting craft that reaches it. When the art director proposes a technique ("add more lights"), ask for the target it serves (what should read first, what mood) and answer with captures and the cause; pick the technique yourself. A real conflict goes to the owner.

When a stage drifts from the target, decide which layer is wrong before changing anything: wrong large shape, right shape badly framed, wrong value hierarchy, inconsistent material response, or a different camera, exposure or graphics tier. Fixing the wrong layer breeds compensating errors (a darker texture hides an over-strong fill light and ruins the material elsewhere) (CO07 O).
