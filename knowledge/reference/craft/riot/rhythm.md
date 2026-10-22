---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [animator, vfx-designer, sound-designer, film-director, ui-ux-designer, game-designer, marketing, art-director, modeler, reference-images, reviewer]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Rhythm

Cadence and sequence: how beats are spaced, offset and ordered in clips, effects, sound and even stills.
RH-01 and RH-02 vary the beat (uneven cadence, no twinning). RH-03 orders an effect into beginning, middle and end. RH-04 is a blocking technique for holds. RH-05 brings motion into still images.
Related: timing gaps in `weight-timing.md` (WT-13, WT-21), size rhythm in `shape-silhouette.md` (SS-07), spacing of contrast in `value-contrast.md` (VC-15).

### RH-01 Vary the cadence: fast and slow beats, never metronomic
- principle: Motion on an even cadence feels predictable; a varied, "jazzy" rhythm of fast and slow beats is exciting.
- why: Viewers feel rhythm like music; sameness lowers attention.
- apply: Vary the gaps between key beats (not every key N frames apart). Same for VFX bursts, UI animation sequences and sound hits in a combo.
- check: List the frame gaps between the main beats of a clip or effect: they are not all equal. Play with sound off and tap along: if the beat is metronomic, vary it.
- mistake: "everything is on the exact same cadence becomes predictable" (R04:360-362).
- examples:
  - R04: "swoop up and then she needs a little down", retimed by feeling the rhythm; "ka-du-doom dah" (R04:354-366).
- roblox_fit: No change.
- roles: animator, vfx-designer, sound-designer, film-director, ui-ux-designer
- also: weight-timing
- sources: R04-F15 (R04:354-366)

### RH-02 No twinning: offset paired parts for two reads
- principle: Avoid twinning (paired limbs identical or moving on the same frame). Make poses asymmetric and offset the timing; a second foot landing a little later gives two reads: hitting the ground and catching the weight.
- why: Symmetry and simultaneity look boring and predictable; offsets create interest and separate events the eye can catch.
- apply: Offset paired limbs by 1-3 frames [inference] and vary their angles. Same for paired VFX elements, props in a set and spawned items.
- check: Compare left and right limb keys: they do not share every key frame or mirror angles exactly; key-pose silhouettes are not mirror-symmetric.
- mistake: "twinning ... can like look really visually boring or specifically it feels really predictable" (R04:544-548); arms "doing the exact same thing on both sides" (R04:700).
- examples:
  - R04: the feet made less symmetrical; one foot delayed so it "is not hitting the exact timing as the other foot" (R04:540-552, 696-700, 714-724, 748-750).
- roblox_fit: No change.
- roles: animator, vfx-designer, modeler, reference-images, reviewer
- also: shape-silhouette, weight-timing
- sources: R04-F25 (R04:540-552, 696-700, 714-724, 748-750)

### RH-03 Every effect tells a beginning, a middle and an end
- principle: An effect is a short story: a beginning (build), a middle (peak, the hit) and an end (result, resolve). This lesson "put my effects farther than they could have gone" (R06).
- why: A clear sequence (cause, peak, result) lets players understand what happened.
- apply: Write each effect as a three-beat story in the brief (for example: clouds swirl in, lightning goes unstable, burst, candy rains and piles on the floor). Sound cue cards and animation follow the same three beats; celebrations and UI reward sequences too.
- check: Capture the effect and label the three beats with start times: each beat is visible and distinct; no effect simply appears and stops.
- mistake: An effect with no build or no resolve.
- examples:
  - R06: cotton-candy clouds swirl in, electricity from instability, burst, candy rain covering the floor (R06:204-210, 229, 292-295).
- roblox_fit: Script the beats as timed Emit calls or Enabled toggles; Enabled false stops new particles but existing ones live on (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:490).
- roles: vfx-designer, animator, film-director, sound-designer, game-designer, ui-ux-designer
- also: vfx-reads-timing, weight-timing
- sources: R06-F20 (R06:204-210, 229, 292-295)

### RH-04 Block holds as copied key pairs, not stepped keys
- principle: Make a hold by duplicating the key a few frames later ("copied pairs") instead of stepping all keys; the real timing stays visible while blocking.
- why: Stepped keys hide in-between timing; copied pairs make the pause clearly a pause while the motion still plays.
- apply: In Blender by Python, copy all channels of a key to a later frame to make a hold. Use stepped (constant) interpolation only for a quick pose review.
- check: Holds show as two identical keys with a flat curve between; preview with normal interpolation, not stepped.
- mistake: Relying only on stepped keys and losing the sense of timing (R04:278).
- examples:
  - R04: "I will duplicate the key that I previously had to create a hold" (R04:266-284).
- roblox_fit: Roblox's equivalent of stepped is PoseEasingStyle Constant (knowledge/external/roblox-creator-docs/_api-reference/enums/PoseEasingStyle.yaml:29-33).
- roles: animator
- also: weight-timing, pipeline-production
- sources: R04-F12 (R04:266-284)

### RH-05 Put motion into a still with a few committed flow lines
- principle: Show wind and movement in a still image with a few swirling, purposeful lines (wind lines, cloth, a fishing line) that run through the focal point; pick a couple and commit to them.
- why: Curved flow lines imply direction and speed, give dynamism, and the eye follows them.
- apply: Key art, icons and thumbnails ask for 2-3 sweeping motion lines through the focal point. In Roblox scenes use Trail or Beam for the same curves.
- check: Trace the main lines on the render: they form one continuous flow through the focal area and do not cross each other chaotically; count them (2-3).
- mistake: Too many uncommitted lines (R10:545-547: "I'm just gonna try to commit to a couple").
- examples:
  - R10: swirling wind lines and the fishing line around Yasuo (R10:132-134, 144-146, 543-547).
- roblox_fit: Trails and Beams render curves cheaply; count them against the effect budget on phones [unverified numbers].
- roles: marketing, vfx-designer, animator, art-director, film-director, ui-ux-designer
- also: composition-focus, vfx-reads-timing
- sources: R10-F05 (R10:132-134, 144-146, 543-547)
