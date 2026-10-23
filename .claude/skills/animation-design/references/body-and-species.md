> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-design`. Rebuilt by J018 maker animator · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Evidence: animation paper notes `knowledge/reference/animation/01-*.md` §5 (body parts, species, motion profile, face and secondary); the craft library `knowledge/reference/craft/riot/` (character-design, exaggeration, weight-timing, references-ideation). The rigger's side of the same facts: `rigging-design/references/motion-needs.md` and `creatures-mechanisms-faces.md`. All "typical frames" are unknown in the sources; none are given here. Roblox joint facts were checked in the docs mirror (`characters/index.md`, `FaceControls.yaml`). Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021): outside method for read-carrying clips.

# Body parts, species families, the motion profile

## 1. Study before moving
- One record per visible part: what it is, what carries it, whether it bends, what movement is meant. The multi-view study includes the underside where it matters; lengths are measured, never read off names. Unclear or missing structure goes to the rigger as a question first.
- Keep three layers apart: **observed** (read from the file: transforms, lengths, weights, limits), **inferred** (tail_03 is probably a tail segment: store evidence and confidence), **authored or unknown** (mass, centre of mass, stiffness, personality, safe range, gait). Never derive kilograms from bone length, bounding box or vertex count.
- Support and balance are working guesses: mark planted contacts, the support area and a centre-of-mass proxy. A pelvis proxy is not the whole-body centre of mass when a big tail, wings or a tool is present. A pose outside the support area can be explained by momentum, a second contact, lift or a stylized break.
- Ask which force starts and redirects the action and what leads next; do not assume hips always lead and the head always trails.
- **Body shape predicts movement.** A heavy silhouette stomps; a slim one darts. Read the model's black-fill and write how it would move; when it disagrees with the brief, ask before keying.
- **Anatomy first.** When a motion is hard, go back to the bones and muscles (the wind-up before a throw, which joint can take a stretch). Believable joints and masses read alive; know which joints can be pushed, held long or smeared without looking broken.
- **Stress the costume, not only the body.** S1 stress poses include arms up, head turn, crouch and the signature attack, so collars, scarves, armour and hair near a joint are tested before the final model.

## 2. Body parts
| Part | Driven by | Decide |
| --- | --- | --- |
| Root / whole body | travel, acceleration, braking, support, impulses | root path and contact schedule match; the root control is not the centre of mass |
| Pelvis, trunk, shoulders | actuation, balance, load transfer, expression | no blanket lead order; the shoulders supply the energy and range of a jump or throw (they lift and tighten first), the hips tilt with every weight shift and let a pose sink. A standard Roblox body has no collarbone joints (they exist only on advanced R15 rigs): push that energy into the upper torso and upper arm instead |
| Neck and head | gaze target, stabilization, deliberate reaction | the task drives the head; it is not always a lagging copy. In a look-turn the eyes lead, then the head, then the body. In a spin or fast body turn the head can hold its world direction, then turn late and fast. Gaze direction is part of the pose from blocking; the face never fights the posture |
| Arms, hands, held prop | reach, grip, leverage, release | a fixed grip ties hands and object into one system; elbows drag behind; energy flows out to the fingertips at the top of a move; fingers splay on contact and drag on falls. Finger joints exist only on advanced R15 rigs (up to 15 per hand): without them, use bigger hand-pose changes or a hand-mesh swap |
| Legs and feet | stance, unloading, swing, touchdown, recovery | each contact is planted, rolling, sliding or released; a deliberate skid is not a foot-lock error; feet stay down a frame or two longer on a push-off |
| Passive tail or strap | base acceleration, flexibility, damping, gravity, collision | lags and settles from its base; attachment changes the result |
| Active tail | counterbalance, support, steering, signalling | may lead and turn the body [V] |
| Bird wing + tail | takeoff, cruise, braking, landing, fold, glide | stroke plane, body attitude and tail work together [V]; glide is not a frozen flap [V] |
| Bat wing | extension, membrane, flap, manoeuvre | asymmetric retraction turns the body [V] |
| Insect wing | species stroke amplitude, pitch, frequency | very fast beats need a blur, sub-frame or proxy plan, not a slowed bird flap [V] |
| Ears | intent, sensory response, passive tissue | can move before the head; left and right separate [V] |
| Antennae | active search, contact, passive deflection | contact changes sampling and the next step [V] |
| Hair, cloth, soft tissue | attachment, stiffness, wind, collision, art direction | keep contact and silhouette; no single delay for all materials; animate a mass, then offset each segment; heavy hair is springy, not fluid |
| Eyes and face | intention, attention, reaction | dynamic heads move eyes, lids and brows through FaceControls channels (for example LeftEyeClosed); a decal face cannot blink without a texture swap; brows carry identity and read at game size when pushed |
| Fins | propulsion, steering, braking | separate jobs; rays need not bend as one paddle [V] |
| Long axial body | ground traction or fluid + travelling wave | curve, travel and muscle activation are three things [V] |
| Mechanical hinge, piston, gear | actuator, linkage, hard stop | hold the linkage; flex only if designed |

## 3. Species families
- **Legs:** 4-leg gaits were measured on horses only; a 6-leg tripod in fruit flies at steady straight speed; 8-leg coordination is speed- and pair-dependent [V]. Treat each as a starting hypothesis. Per leg log contact state, touchdown position, stance fraction and cycle phase; stance feet stay put in world space. A machine may use an authored step schedule if its support logic is written.
- **Slither and swim:** body-ground contact and weight spread drive progress, not a sine outline [V]; swimming changes with the medium [V].
- **Floating:** buoyant fluid, orbit or free fall, ballistic flight and magical hover are four different cases; a generic up-down sine is none of them; magical hover needs an authored force rule. Weightless is not massless [V].
- **Heavy tools:** heavier hammers changed joint loads and phase durations in one lab study [V]; heavy lifting is taught through motivation, load-bearing poses and recovery, not a fixed anticipation count. Heavy describes the feel, not a mass you invent.
- **Hybrid and invented creatures:** build from real anatomy: name which animal supplies which body part and its motion reference, and where invention takes over; never mix pigeon angles, bat roosting and bee frequency into one "measured" profile. Real parts carry belief in a strange combination.
- **Scale:** a giant moves slowly, with long settles and ground-shaking contacts; a small creature is quick. A semi-human creature meant to be scary turns silly easily: keep its motion deliberate and its proportions threatening; check the threat reads in black-fill.

## 4. Face and secondary
- Start with intention and attention: what the character notices, wants, hides. Then align eyes, lids, brows, mouth, head, neck and body. A set of face channels is not an acting plan.
- At gameplay distance gaze and head attitude matter more than lip detail; in close-ups judge eyes and mouth with the body. In a look-turn the eyes arrive first, then the head, then the body; the face never fights the posture. Eyes act: they close in a fast spin or on a fast head turn, widen on a fall, look from under the brows on an intense beat.
- **Key** when timing, silhouette, contact, comedy, dialogue or gameplay information must repeat exactly; **procedural** when input keeps changing and the result can be bounded and tested; **hybrid** when authored intent sets the base and a bounded layer reacts. A tail that points, grips or balances cannot be a free spring.
- A procedural layer needs on record: target, local frame, rest state, damping and stiffness form, timestep dependence, collision scope, limits, reset on teleport and interruption, off-screen and throttled behaviour, determinism, authority. No sourced spring value exists.
- Never apply secondary motion twice (a lag baked into the clip plus a runtime spring).

## 5. The motion profile (template `templates/anim/motion-profile.md`)
Fields: identity and purpose · topology (semantic inventory) · scale and axes · mass and inertia (supplied or UNKNOWN) · support and contacts · active drivers · secondary response · personality · timing (phases, sourced durations, event positions) · limits and exceptions · runtime (rig type, priority, blending, replication, budget test) · review evidence.
Also write, under identity and personality: the feel words with their visible change, the 2-5 identity anchors and hook shapes that must stay visible at key poses (and the side the camera sees), whether the body shape agrees with the motion, and costly parts with their cheap fallback.
Reject the profile when: an identity or task is ambiguous, a moving part is unmapped, kilograms are invented, a contact has no driver, a part's motion has no cause, every appendage is a delayed sine wave, an unsupported number is shown as evidence, or an extreme exceeds verified rig reach.

## 6. Reference
- **Order:** our game's approved clips and anchors first (gesture, timing language), then real-world motion; for a clip that carries the read (a tell, a signature move, an emote), one reference chosen from the job's target-experience sentence (the mover or field that makes a viewer feel that), with the method taken as an action ("stills before the strike"), never its look; combine; take ideas (mechanics, timing, silhouette change), never copy a clip or a design. When a brief fuses two ideas (a samurai who fishes), gather reference for the overlap (how a fishing cast and a sword draw feel alike), not for each idea alone.
- Choose reference for matching anatomy, action, speed, camera, load and intent, not looks. Keep the file, source, date, frame rate (and whether it varies), edits and occlusions. A re-encoded social clip is not a timing measurement. Use only reference the studio may use. Real observation adds what invention misses; gather more than you show.
- **A new motion style** (a genre's combat feel the game has not used): study 2-3 successful clips of it structurally (beat gaps in frames, pose count, hold lengths, where the accent sits), then change the result toward our feel words and anchors. It keeps the learned structure and differs visibly in poses; never copy a clip or its look.
- Decide the event before measuring (first preparation, first motion of the striking surface, first contact, apex, return to rest). Store measured data apart from the retiming proposal.
- **Act it out on paper:** agents cannot film themselves, so write the performance beat by beat (motion direction and driver, time, a sound word, the subtext) and find the felt timing in it: how two weighted sticks would swing, how weight leaves one foot before it lifts. When no reference shows the pose, make one: a posed Blender mannequin with the rig's proportions at the game camera, a keyed test pose in Studio, or a `pose` reference image.
- Pose to pose from reference: pick the storytelling poses from the reference, put them on the timeline with frame numbers, and review them as stills before any in-betweens.
