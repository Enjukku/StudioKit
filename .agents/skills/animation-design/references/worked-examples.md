> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-design`. One worked example per kind of moving object. These show the **decisions**, not presets: every length is a gameplay window, a measured reference or a PROPOSAL the owner can change. Rebuilt by J018 maker animator · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Evidence: animation paper notes `knowledge/reference/animation/01-*.md`, `02-*.md`; technique facts `fact-check-techniques.md` (RT, TC ids) and `fact-check-roblox-runtime.md` (RA ids); the craft library `knowledge/reference/craft/riot/`.

# Worked examples, one per kind

Every example answers the same questions: **read** (what the player must understand, and who must react), **drivers** (what pushes, supports, follows), **technique** (and why), **poses and phases**, **spacing**, **events** (timing list), **checks**. Key clips also show the plan stages: beat sheet, options, pick.

## 1. Character: an emote that shows two sides of one character
A tough brawler's victory emote: a heavy kneel that rises into a friendly double thumbs-up. Third-person camera, phone, seen for about two seconds.
- **Read:** "tough, then sweet": two sides of one character in one move; maximum expression for a two-second read.
- **Beat sheet:** (1) lands in a low kneel, fist down, "THUD", wants to look scary; (2) holds, glances at the camera, "...", decides to break character; (3) springs up, "hup", (4) lands on both thumbs, grin, "ta-da", wants to be liked. Times are PROPOSALs until the owner sees the blocking.
- **Options:** three black-fill key-pose pairs at the game camera: a straight stand-up, a spin into the thumbs-up, a hop that kicks one leg back. The hop wins: its kicked leg and raised thumbs make the clearest outline at phone size; the spin hid both arms behind the body for three frames.
- **Drivers:** the centre of gravity first; weight comes off the front foot before it lifts; the shoulders lift and tighten before the spring. In the glance (beat 2) the eyes reach the camera first, then the head, then the chest; if the hop turns the body, the head holds its world direction and turns late and fast.
- **Technique:** keyed clip on the rig (acting must repeat exactly).
- **Poses:** the two key poses from the character's identity anchors; a breakdown "storytelling pose" can look ugly alone and still carry the motion; the apex of the hop tucks the legs into a V.
- **Spacing:** the first pose held a few frames (PROPOSAL: about 5 at 30 fps) so it registers; rough timing on shared whole-body frames first; then keys broken apart so actions start at different times; the feet stay down a frame or two longer for the push-off; a short coiled hold before the spring; a small overshoot on standing; one foot lands a frame after the other.
- **Secondary:** last. A hood string or ponytail as one mass, then offset per segment; a blink on the fast head turn; eyes open wide on the grin.
- **Checks:** weight shift before every foot lift; no twinning; black-fill of both key poses at the game camera names "tough" and "friendly"; the identity anchor (a giant glove) stays in the outline; shown for 2 s at phone size, the intent reads.
- **Promo still (when marketing briefs one):** the premise in one sentence, "the toughest brawler in the arena is secretly sweet"; the pose is the thumbs-up key frame of this clip, set on the rig, not a new pose; staged at the marketing camera with the giant glove forward. Check: its black-fill at the game camera overlaps the clip's key frame (`silhouette --compare`), and a fresh read of the still names the premise.

## 2. Character: a light melee attack inside a gameplay window
- **Read:** "a quick jab is coming from the right, and it lands now". The player is the attacker: the move answers the input at once.
- **Drivers:** the gameplay window (startup, active, recovery, cancel) comes from the feature contract; the animator never changes it.
- **Technique:** keyed clip; upper body layered over locomotion if the game lets the player move while attacking (priority Action over Movement; key only the upper-body joints).
- **Phases:** a short, tight tell inside startup (the player's own move); the accent pose sits at `active_start`; recovery reads as committed and returns to a pose that blends into idle and run.
- **Spacing:** snap into the strike (fewer frames between keys is faster); no default ease on the impact; ease only the settle; one peak frame.
- **Attempt vs outcome:** the jab plays on input and stays small; the target's reaction and any hit-stop play only when the server confirms the hit, sized by its strength; the freeze frame is the extended-fist pose with the fist clear of the body.
- **Events:** `windup_start`, `active_start`, `contact_candidate`, `recovery_start`, `cleanup`. Damage is the server's; a trail may start before contact; the sound transient lands on the contact frame or up to about 40 ms after it.
- **Checks:** with VFX hidden the hit still reads; the threat's direction is visible before the player must react; the clip ends where the next state starts; a rejected hit plays no confirmed reaction.

## 3. Held item: a heavy two-handed sword swing
- **Read:** "this blade is heavy and committed; once it starts, it follows through".
- **Drivers:** feet organize force and braking; torso and arms together accelerate the blade; the primary hand owns the grip, the secondary hand follows a solved contact. Heavy is the feel, not an invented mass, and never slow playback. The blade is carried close to the body when loaded (close reads heavy); a wider, lower stance adds weight.
- **Beat sheet:** load (drag the blade back, shoulders rise, "hnnn"), accelerate ("WHUM"), impact ("KRANG"), decelerate, recover; the subtext: the knight commits everything to this blow.
- **Technique:** keyed on the character rig, the sword on a grip socket (`rig-pipeline`: grip anchors, impact surface). The item's own parts (a chain, a tassel) are keyed or bounded secondary motion; they never pass through the floor or detach the grip.
- **Phases:** load, accelerate, impact, decelerate, recover, with cancel rules from design. Lengths: the gameplay window; inside it, a longer load and a longer follow-through and a very short acceleration give the heavy feel (a lab study shows a heavier tool lengthening phases: measured context only, not a preset).
- **Spacing:** the tip draws a clean arc (trace it); a small change near the shoulder throws a long blade tip far off its arc; the counter-arm or the back foot braces against the swing.
- **Events:** `swing_accel` (whoosh, trail start for VFX), `contact_candidate` (blade reaches the target zone), `follow_through_end`, `cleanup`. Trails and impact flashes are VFX, on these ids.
- **Checks:** both grips hold (contact metric); the tip arc is smooth from the game camera; the blade is the clearest shape at contact in black-fill; impact reads with effects off; recovery shows the weight.

## 4. Creature action: a heavy beast's pounce
- **Read:** "it is going to leap at me: I can see it coming and dodge". The player must react: the tell is information.
- **Drivers:** a quadruped body; the hind legs load and push, the front legs reach and catch; the tail counterbalances in the air (an active part); ears and jaw carry intent; a big beast moves with slower beats and heavier contacts than a dog.
- **Technique:** keyed clip on a skinned rig with AnimationController + Animator (no Humanoid needed); creature LOD variant if many are on screen.
- **Phases:** crouch-load (the tell: a distinct pose, held for the designer's reaction window), launch, flight, land-catch, recover. Landing: contact fast, the catch follows; hang time at the top and a fast fall if the style is cartoony.
- **Spacing:** a hold at the deepest crouch (energy tightening); a parabolic flight path for the body; no stall in the air.
- **Events:** `telegraph_start` (sound and UI may cue danger), `launch`, `land_contact` (dust VFX, impact sound), `recover_end`.
- **Checks:** the tell silhouette reads at phone size from the player's camera with VFX off; its frame count covers the reaction window; stance feet stay planted while loading (contact metric); the landing does not scoot; every pounce of this creature uses the same tell.

## 5. Pet: idle with attention and a catch-up
- **Read:** "it is alive, it likes me, it is not a machine".
- **Drivers:** attention (the owner, nearby things), comfort, curiosity; motivated holds instead of a uniform oscillation; the feel words (for example "soft, curious, loyal") each get one visible change.
- **Technique:** keyed idle loop + a few one-shot attention gestures; head look-at as a bounded procedural layer if the owner moves; follow and catch-up driven by the controller with in-place locomotion.
- **Phases:** attention / optional gesture / return; correction behaviour after the pet is teleported.
- **Checks:** loop seam (pose and velocity); one clear accent per loop (an ear flick, a glance), not every part bobbing; many pets on screen do not twin (phase offsets); off-screen throttling does not break the next visible pose.

## 6. Door (no rig): open on interaction
- **Read:** "it unlocked, it swings open, I can pass". Personality: "heavy, old, grinding" or "light, cheap, rattly".
- **Drivers:** a hand or a mechanism on a hinge line along the door edge, never the mesh centre (`rigging-design` mechanisms). Phases unlock / accelerate / travel / stop.
- **Technique:** code-driven on the client (a tween of the door CFrame about the hinge pivot; the docs' doors example tweens CFrame between targets) for the cosmetic swing, or a hinge servo whose target the server sets once per state change; the server owns "open" and collision (a server tween replicates every frame). No rigger step. The animator writes `templates/anim/motion-spec.md`; a builder writes the code. A second tween cancels the first and leaves the door mid-way: the spec says which end state wins.
- **Curves:** a small latch rattle first (the door gives: its anticipation); out-ease into the travel for a heavy door, a quicker start for a light one; a hard stop with a small settle, or a soft stop on a damped hinge. Name each EasingStyle and direction and why.
- **Events:** `unlock_click`, `swing_start`, `door_stop` (sound).
- **Checks:** pivot correct from two views; the open end state reads in a still; a late joiner sees the open state, not a replay; triggering again mid-swing is defined.

## 7. Drawbridge: heavy, slow, chained
- **Read:** "something huge is coming down; wait for it".
- **Drivers:** a winch or counterweight lets out chains; gravity does the work; the bridge pivots at its base hinge.
- **Technique:** code-driven rotation on the hinge for the deck (one axis, rigid); chains as a short keyed clip or a texture scroll if they read only as detail; physics only if players can stand on it while it moves (then the physics owner decides).
- **Curves:** slow start (the counterweight overcomes friction), speeding up as gravity takes over, a heavy landing with a small bounce and dust; no ease-in-out on the whole travel (that reads as a lift motor).
- **Events:** `release` (chain rattle starts), `land_contact` (thud, dust, camera shake if the game uses it), `walkable` (gameplay, server-owned).
- **Checks:** the bridge is not walkable before `walkable`; the motion reads as heavy from the player's position at the far side.

## 8. Chest, egg reveal, lever, elevator, trap (props and mechanisms)
| Object | Read | Technique (why) | Key decisions |
| --- | --- | --- | --- |
| Chest | "something good is inside" | code-driven lid on its hinge, or a short keyed clip when lid, lock and contents all move | a small anticipation rattle; the lid opens fast then settles; the reveal peak sits on an event VFX and sound share; reward outcome is server-owned |
| Egg or crate bought with currency | "what did I get?" | keyed clip or code sequence; the result comes from the server first | one windup for every result (same beats, length and poses up to the result frame); no near-miss wobble or rarity tint before the result; tier flourishes start after the result frame, more layers for rarer tiers; a result worth less than its cost is not celebrated (`platform-policy`) |
| Lever | "I pulled it, something changed" | keyed hand contact on the character + code-driven lever on its pivot | the hand holds the grip through the pull; the lever has a hard stop; the change it triggers has its own event |
| Elevator / moving platform | "it is safe to ride; it will start and stop gently" | code or physics; occupancy and collision server-owned | gentle start and stop for riders; a clear arrival; never moves while a door is open |
| Trap (swinging axe, spikes) | "danger, now; safe, now" | code-driven pendulum or keyed clip; the active window from the game-designer | the tell reads before the active window; danger and safe poses are distinct silhouettes; the danger pose ends when the danger ends; the pendulum keeps a constant period (a mechanism, not a character) |

## 9. Vehicles and mounts
- **Vehicle (cart, car):** the body's motion comes from the vehicle controller or physics; animation adds what reads: wheel spin matched to ground speed (no sliding wheels), suspension and body roll that follow turns and bumps, a driver clip. Wheel and suspension links come from the rig plan.
- **Mount (horse, beast):** the mount's gait carries the rider; the rider's hips follow the saddle, the upper body balances and leads intent. Gait patterns are species-specific hypotheses; stance feet stay planted in world space; mount and rider share events (`mount_start`, `stride_contact` for hoof sounds).
- **Checks:** wheel or foot contact speed against ground speed (slide metric); rider hands stay on the reins (contact metric); in-place clips with the controller owning travel.

## 10. Buildings and large structures: build-up, transformation, collapse
- **Read:** "it is being built / it changed / it fell" with a clear end state.
- **Drivers:** a chosen sequence: pieces arrive in an art-directed order with eased rotation and a separate drag, while collision stays untouched.
- **Technique:** a code-driven or keyed sequence of rigid pieces for build-up and transformation; debris and collapse are physics or VFX, decided with the destruction / physics owner and the environment-designer; the gameplay state (blocked, walkable, destroyed) is server-owned and never waits on the show.
- **Spacing:** each piece has a readable arrival and settle (reaching most of its travel fast, easing into place); drag explains travel, never ornamental wobble; stagger arrivals so the eye follows the order; a collapse shows stress first.
- **Events:** `build_start`, per-stage `stage_n_complete`, `complete` (VFX flash, sound), `collapse_start`, `rubble_settled`.
- **Checks:** end state matches collision; the sequence reads at the gameplay distance; cost of moving pieces measured when many build at once.

## 11. World decoration and ambient loops (many copies)
- **Read:** "the world is alive", without pulling the eye from gameplay.
- **Flag:** a short looped clip on a few bones on a client Animator (bones deform the mesh, not collision; client tracks do not replicate, which is wanted), or a code sway of a rigid flag; a static or flipbook stand-in far away. Global wind does **not** move flags or meshes, only grass, clouds and particles. Vary phase per copy so a row of flags does not wave in step.
- **Windmill, water wheel:** constant rotation in one client loop for all copies (`PivotTo` or `Motor6D.Transform`), or a hinge motor if it must physically push things. A mechanism at steady speed has no ease inside the loop; speed linked to its cause (wind, water).
- **Plants, signs:** a gentle sway with irregular timing that follows the plant's own curve; a hanging sign can be a local physics hinge (reacts to players, may differ per client) or a code sway (identical for all, never reacts); state which. Ambient motion stays slower and smaller than anything near a sightline.
- **Scale:** cost per copy × copies on screen decides, and no per-copy cost is documented: measure at the peak count on the floor phone (`animation-craft` §6). Animated models get no far LOD; client motion restarts on stream-in at a believable phase; offer a still or slow variant for reduced motion.
- **Checks:** copies out of step; only decorative axes vary; loop seam clean; never the fastest motion near the play space; measured cost at the peak count on the target phone (or BLOCKED without a phone).
