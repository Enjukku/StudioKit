> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-design`. Sources: animation paper AP:180-345 (notes `knowledge/reference/animation/01-*.md` §5: BO, BP, SP, TP, PF, RF), AP:500-521 (face and secondary, FS). The rigger's side of the same facts: `rigging-design/references/motion-needs.md` and `creatures-mechanisms-faces.md`. Tags as in SKILL.md. All "typical frames" are UNSPECIFIED in the sources; none are given here.

# Body parts, species families, the motion profile

## 1. Study before moving (AP:184-198)
- One record per visible part: what it is, what carries it, whether it bends, what movement is meant. Unclear or missing structure goes to the rigger as a question first.
- Keep three layers apart (AP:572-578): **observed** (read from the file: transforms, lengths, weights, limits), **inferred** (tail_03 is probably a tail segment: store evidence and confidence), **authored or unknown** (mass, centre of mass, stiffness, personality, safe range, gait). Never derive kilograms from bone length, bounding box or vertex count (AP:188).
- Support and balance are working guesses: mark planted contacts, the support area and a centre-of-mass proxy. A pelvis proxy is not the whole-body centre of mass when a big tail, wings or a tool is present. A pose outside the support area can be explained by momentum, a second contact, lift or a stylized break (AP:190).
- Ask which force starts and redirects the action and what leads next; do not assume hips always lead and the head always trails (AP:198).

## 2. Body parts (AP:200-220)
| Part | Driven by | Decide |
| --- | --- | --- |
| Root / whole body | travel, acceleration, braking, support, impulses | root path and contact schedule match; the root control is not the centre of mass |
| Pelvis, trunk, shoulders | actuation, balance, load transfer, expression | no blanket lead order; clavicles supply energy and range ("the eyebrows of the body") [E] A:394-410; hips let a pose sink in [E] A:652-654 |
| Neck and head | gaze target, stabilization, deliberate reaction | the task drives the head; it is not always a lagging copy; a head can stay locked through a turn [E] A:944-948 |
| Arms, hands, held prop | reach, grip, leverage, release | a fixed grip ties hands and object into one system; elbows drag behind; fingers matter even when small [E] A:904-928 |
| Legs and feet | stance, unloading, swing, touchdown, recovery | each contact is planted, rolling, sliding or released; a deliberate skid is not a foot-lock error |
| Passive tail or strap | base acceleration, flexibility, damping, gravity, collision | lags and settles from its base; attachment changes the result |
| Active tail | counterbalance, support, steering, signalling | may lead and turn the body [V] gecko tails (AP:228) |
| Bird wing + tail | takeoff, cruise, braking, landing, fold, glide | stroke plane, body attitude and tail work together [V] pigeons (AP:234); glide is not a frozen flap [V] (AP:238) |
| Bat wing | extension, membrane, flap, manoeuvre | asymmetric retraction turns the body [V] (AP:236) |
| Insect wing | species stroke amplitude, pitch, frequency | very fast beats need a blur, sub-frame or proxy plan, not a slowed bird flap [V] (AP:200-220, AP:1106) |
| Ears | intent, sensory response, passive tissue | can move before the head; left and right separate [V] cat ears (AP:200-220) |
| Antennae | active search, contact, passive deflection | contact changes sampling and the next step [V] (AP:200-220) |
| Hair, cloth, soft tissue | attachment, stiffness, wind, collision, art direction | keep contact and silhouette; no single delay for all materials; animate a mass, then offset each segment [E] A:984-1024 |
| Fins | propulsion, steering, braking | separate jobs; rays need not bend as one paddle [V] (AP:200-220, AP:258) |
| Long axial body | ground traction or fluid + travelling wave | curve, travel and muscle activation are three things [V] (AP:200-220, AP:254-256) |
| Mechanical hinge, piston, gear | actuator, linkage, hard stop | hold the linkage; flex only if designed (AP:200-220) |

## 3. Species families (AP:222-264)
- **Legs:** 4-leg gaits were measured on horses only; a 6-leg tripod in fruit flies at steady straight speed; 8-leg coordination is speed- and pair-dependent [V] (AP:244-248). Treat each as a starting hypothesis. Per leg log contact state, touchdown position, stance fraction and cycle phase; stance feet must stay put in world space. A machine may use an authored step schedule if its support logic is written (AP:250).
- **Slither and swim:** body-ground contact and weight spread drive progress, not a sine outline [V] (AP:254); swimming changes with the medium [V] (AP:256).
- **Floating:** buoyant fluid, orbit or free fall, ballistic flight and magical hover are four different cases; a generic up-down sine is none of them; magical hover needs an authored force rule (AP:260-262). Weightless is not massless [V] (AP:260).
- **Heavy tools:** heavier hammers changed joint loads and phase durations in one lab study [V] (AP:264); heavy-lift teaching stresses motivation, load-bearing poses and recovery, not a fixed anticipation count [E] (AP:264). Heavy describes the feel, not a mass you invent.
- **Hybrid creatures:** write which animal supplies which reference and where invention takes over; never mix pigeon angles, bat roosting and bee frequency into one "measured" profile (AP:240).

## 4. Face and secondary (AP:500-521)
- Start with intention and attention: what the character notices, wants, hides. Then align eyes, lids, brows, mouth, head, neck and body. A set of face channels is not an acting plan (AP:504).
- At gameplay distance gaze and head attitude can matter more than lip detail; in close-ups judge eyes and mouth with the body (AP:506). Blinks have a reason: people blink when the head turns fast [E] A:1028-1046.
- **Key** when timing, silhouette, contact, comedy, dialogue or gameplay information must repeat exactly; **procedural** when input keeps changing and the result can be bounded and tested; **hybrid** when authored intent sets the base and a bounded layer reacts. A tail that points, grips or balances cannot be a free spring (AP:508).
- A procedural layer needs on record: target, local frame, rest state, damping and stiffness form, timestep dependence, collision scope, limits, reset on teleport and interruption, off-screen and throttled behaviour, determinism, authority. No sourced spring value exists (AP:510).
- Never apply secondary motion twice (a lag baked into the clip plus a runtime spring) (AP:512).

## 5. The motion profile (template `templates/anim/motion-profile.md`; AP:266-282)
Fields: identity and purpose · topology (semantic inventory) · scale and axes · mass and inertia (supplied or UNKNOWN) · support and contacts · active drivers · secondary response · personality · timing (phases, sourced durations, event positions) · limits and exceptions · runtime (rig type, priority, blending, replication, budget test) · review evidence.
Reject the profile when: an identity or task is ambiguous, a moving part is unmapped, kilograms are invented, a contact has no driver, a part's motion has no cause, every appendage is a delayed sine wave, an unsupported number is shown as evidence, or an extreme exceeds verified rig reach.

## 6. Reference (AP:332-338)
- Choose reference for matching anatomy, action, speed, camera, load and intent, not looks. Keep the file, source, date, frame rate (and whether it varies), edits and occlusions. A re-encoded social clip is not a timing measurement. Use only reference the studio may use.
- Decide the event before measuring (first preparation, first motion of the striking surface, first contact, apex, return to rest). Store measured data apart from the retiming proposal.
- Act it out: two people with weighted sticks find how a weapon swings [E] A:632-636; stand on both feet and try to lift one to feel the weight shift [E] A:460-466. When stuck, go back to anatomy [E] A:308-312.
