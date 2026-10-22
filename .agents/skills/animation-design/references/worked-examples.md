> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-design`. One worked example per kind of moving object. These show the **decisions**, not presets: every length is a gameplay window, a measured reference or a PROPOSAL the owner can change. Sources: animation paper notes `knowledge/reference/animation/01-*.md`, `02-*.md` (AP:<line>); Riot ep4 A:<line> and core series R:<line> (`03-riot-first-game.md`); technique facts `knowledge/reference/animation/fact-check-techniques.md` (RT ids) and `fact-check-roblox-runtime.md` (RA ids). Tags as in SKILL.md.

# Worked examples, one per kind

Every example answers the same seven questions: **read** (what the player must understand), **drivers** (what pushes, supports, follows), **technique** (and why), **poses and phases**, **spacing**, **events** (timing list), **checks**.

## 1. Character: weight shift between two attitudes (the principle case)
Riot's K/DA Akali demo: a tough hip-hop kneel to a sweet finger-heart, about 3 h in Maya [E] A:38-56.
- **Read:** two sides of one character in one move (A:42-52).
- **Drivers:** the centre of gravity first; weight must come off a foot before it lifts (A:92-100). Head and shoulders held in world space through the spin give balance (A:132-146).
- **Technique:** keyed clip on the rig (acting must repeat exactly).
- **Poses:** the two key poses from the character's concept and in-game actions (A:520-536); a breakdown "storytelling pose" can look ugly alone and still carry the motion (A:950-968).
- **Spacing:** rough timing for the whole body on shared frames first, so it stays easy to move (A:434-438); then break keys apart so actions start at different times, feet stay down a frame or two longer, the push-off sharpens (A:594-606); a short hold before the spring tightens energy (A:450-454); a small overshoot on standing (A:376-382).
- **Secondary:** last. Hair as one mass, then offset per segment; eyes close in the fast spin and widen on the way down (A:984-1046).
- **Checks:** weight shift before every foot lift; no twinning; silhouette from the render camera; the iconic ponytail swoop reads (A:702-708).

## 2. Character: a light melee attack inside a gameplay window
- **Read:** "a quick jab is coming from the right, and it lands now".
- **Drivers:** the gameplay window (startup, active, recovery, cancel) comes from the feature contract; the animator never changes it (AP:473, AP:986).
- **Technique:** keyed clip; upper body layered over locomotion if the game lets the player move while attacking (priority Action over Movement; key only the upper-body joints, AP:751).
- **Phases:** anticipation fits inside startup as information, not extra delay (AP:115-121); the accent pose sits at `active_start`; recovery reads as committed and returns to a pose that blends into idle and run.
- **Spacing:** snap into the strike (fewer frames between keys is faster, A:446-448); no default ease on the impact (AP:1109); ease only the settle.
- **Events:** `windup_start`, `active_start`, `contact_candidate`, `recovery_start`, `cleanup`. Damage is the server's; a trail may start before contact (AP:477).
- **Checks:** with VFX hidden the hit still reads (AP:481); the threat's direction is visible before the player must react (AP:131-137); the clip ends where the next state starts.

## 3. Held item: a heavy two-handed sword swing
Paper profile PF3 (heavy tool swing, AP:316-330) applied to a sword.
- **Read:** "this blade is heavy and committed; once it starts, it follows through".
- **Drivers:** feet organize force and braking; torso and arms together accelerate the blade; the primary hand owns the grip, the secondary hand follows a solved contact (AP:321-322). Heavy is the feel, not an invented mass; heavy does not mean slow playback (AP:323). A held object reads heavier the closer it is carried to the body, lighter when held far out [E] (R:3121-3133); a wider, lower stance adds weight (R:3147-3161).
- **Technique:** keyed on the character rig, the sword on a grip socket (`rig-pipeline`: grip anchors, impact surface). The item's own parts (a chain, a tassel) are keyed or bounded secondary motion; they never pass through the floor or detach the grip (AP:325).
- **Phases:** load, accelerate, impact, decelerate, recover, with cancel rules from design (AP:1110). Lengths: the gameplay window; inside it, a longer load and recovery and a very short acceleration give the heavy feel (the lab hammer study shows a heavier tool lengthening phases, measured context only, not a preset: AP:1113-1114).
- **Spacing:** the tip draws a clean arc (trace it, AP:326); a small change near the shoulder throws a long blade tip far off its arc (AP:674).
- **Events:** `swing_accel` (whoosh, trail start for VFX), `contact_candidate` (blade reaches the target zone), `follow_through_end`, `cleanup`. Trails and impact flashes are VFX, on these ids.
- **Checks:** both grips hold (contact metric); the tip arc is smooth from the game camera; impact reads with effects off; recovery shows the weight.

## 4. Creature action: a heavy beast's pounce
- **Read:** "it is going to leap at me: I can see it coming and dodge".
- **Drivers:** a quadruped body; the hind legs load and push, the front legs reach and catch; the tail counterbalances in the air (an active part, AP:228); ears and jaw carry intent.
- **Technique:** keyed clip on a skinned rig with AnimationController + Animator (no Humanoid needed, AP:771); creature LOD variant if many are on screen (AP:432).
- **Phases:** crouch-load (the telegraph: the readable part of startup), launch, flight, land-catch, recover. Landing: contact fast, the catch follows (A:438-446); hang time at the top and a fast fall if the style is cartoony (A:342-352).
- **Spacing:** a hold at the deepest crouch (energy tightening, A:450-454); parabolic flight path for the body (A:754-758).
- **Events:** `telegraph_start` (sound and UI may cue danger), `launch`, `land_contact` (dust VFX, impact sound), `recover_end`.
- **Checks:** the telegraph silhouette reads at phone size from the player's camera; stance feet stay planted while loading (contact metric); the landing does not scoot.

## 5. Pet: idle with attention and a catch-up
- **Read:** "it is alive, it likes me, it is not a machine".
- **Drivers:** attention (the owner, nearby things), comfort, curiosity; motivated holds instead of a uniform oscillation (AP:1120, AP:389).
- **Technique:** keyed idle loop + a few one-shot attention gestures; head look-at as a bounded procedural layer if the owner moves (AP:508); follow and catch-up driven by the controller with in-place locomotion (AP:813).
- **Phases:** attention / optional gesture / return (AP:1120); correction behaviour after the pet is teleported (AP:426-428).
- **Checks:** loop seam (pose and velocity); many pets on screen do not twin (phase offsets); off-screen throttling does not break the next visible pose.

## 6. Door (no rig): open on interaction
- **Read:** "it unlocked, it swings open, I can pass".
- **Drivers:** a hand or a mechanism on a hinge line along the door edge, never the mesh centre (`rigging-design` mechanisms). Phases unlock / accelerate / travel / stop (AP:1119).
- **Technique:** code-driven on the client (a tween of the door CFrame about the hinge pivot; Roblox's own doors example tweens CFrame between targets, RT1-10) for the cosmetic swing, or a hinge servo whose target the server sets once per state change (TC12); the server owns "open" and collision (a server tween replicates every frame: RT1-05). No rigger step. The animator writes `templates/anim/motion-spec.md`; a builder writes the code. A second tween cancels the first and leaves the door mid-way: the spec says which end state wins (TC02).
- **Curves:** a small latch rattle first (the door gives); out-ease into the travel for a heavy door, a quicker start for a light one; a hard stop with a small settle, or a soft stop on a damped hinge. Name each EasingStyle and direction and why.
- **Events:** `unlock_click`, `swing_start`, `door_stop` (sound).
- **Checks:** pivot correct from two views; a late joiner sees the open state, not a replay; triggering again mid-swing is defined.

## 7. Drawbridge: heavy, slow, chained
- **Read:** "something huge is coming down; wait for it".
- **Drivers:** a winch or counterweight lets out chains; gravity does the work; the bridge pivots at its base hinge.
- **Technique:** code-driven rotation on the hinge for the deck (one axis, rigid); chains as a short keyed clip or a texture scroll if they read only as detail; physics only if players can stand on it while it moves (then the physics owner decides).
- **Curves:** slow start (the counterweight overcomes friction), speeding up as gravity takes over, a heavy landing with a small bounce and dust; no ease-in-out on the whole travel (that reads as a lift motor).
- **Events:** `release` (chain rattle starts), `land_contact` (thud, dust, camera shake if the game uses it), `walkable` (gameplay, server-owned).
- **Checks:** the bridge is not walkable before `walkable`; the motion reads as heavy from the player's position at the far side.

## 8. Chest, lever, elevator, trap (props and mechanisms)
| Object | Read | Technique (why) | Key decisions |
| --- | --- | --- | --- |
| Chest | "something good is inside" | code-driven lid on its hinge, or a short keyed clip when lid, lock and contents all move | a small anticipation rattle; the lid opens fast then settles; the reveal peak sits on an event VFX and sound share; reward outcome is server-owned |
| Lever | "I pulled it, something changed" | keyed hand contact on the character + code-driven lever on its pivot | the hand holds the grip through the pull; the lever has a hard stop; the change it triggers has its own event |
| Elevator / moving platform | "it is safe to ride; it will start and stop gently" | code or physics; occupancy and collision server-owned (AP:450) | gentle start and stop for riders; a clear arrival; never moves while a door is open |
| Trap (swinging axe, spikes) | "danger, now; safe, now" | code-driven pendulum or keyed clip; the active window from the game-designer | the telegraph reads before the active window; danger and safe poses are distinct silhouettes; the pendulum keeps a constant period (a mechanism, not a character) |

## 9. Vehicles and mounts
- **Vehicle (cart, car):** the body's motion comes from the vehicle controller or physics; animation adds what reads: wheel spin matched to ground speed (no sliding wheels), suspension and body roll that follow turns and bumps, a driver clip. Wheel and suspension links come from the rig plan (AP:450).
- **Mount (horse, beast):** the mount's gait carries the rider; the rider's hips follow the saddle, the upper body balances and leads intent. Gait patterns are species-specific hypotheses (AP:244); stance feet stay planted in world space; mount and rider share events (`mount_start`, `stride_contact` for hoof sounds).
- **Checks:** wheel or foot contact speed against ground speed (slide metric); rider hands stay on the reins (contact metric); in-place clips with the controller owning travel.

## 10. Buildings and large structures: build-up, transformation, collapse
- **Read:** "it is being built / it changed / it fell" with a clear end state.
- **Drivers:** a chosen sequence. Fortnite's wall build: pieces arrive in an art-directed order with eased rotation and a separate drag, while collision stays untouched [V] (AP:147-153).
- **Technique:** a code-driven or keyed sequence of rigid pieces for build-up and transformation; debris and collapse are physics or VFX, decided with the destruction / physics owner and the environment-designer; the gameplay state (blocked, walkable, destroyed) is server-owned and never waits on the show.
- **Spacing:** each piece has a readable arrival and settle; drag explains travel, never ornamental wobble (AP:151); stagger arrivals so the eye follows the order.
- **Events:** `build_start`, per-stage `stage_n_complete`, `complete` (VFX flash, sound), `collapse_start`, `rubble_settled`.
- **Checks:** end state matches collision; the sequence reads at the gameplay distance; cost of moving pieces measured when many build at once.

## 11. World decoration and ambient loops (many copies)
- **Read:** "the world is alive", without pulling the eye from gameplay.
- **Flag:** a short looped clip on a few bones on a client Animator (bones deform the mesh, not collision; client tracks do not replicate, which is wanted: TC10, TC11), or a code sway of a rigid flag; a static or flipbook stand-in far away. Global wind does **not** move flags or meshes, only grass, clouds and particles (TC19). Vary phase per copy so a row of flags does not wave in step.
- **Windmill, water wheel:** constant rotation in one client loop for all copies (`PivotTo` or `Motor6D.Transform`, TC07-TC08), or a hinge motor if it must physically push things (TC12). A mechanism at steady speed has no ease inside the loop; speed linked to its cause (wind, water).
- **Plants, signs:** a gentle sway with irregular timing; a hanging sign can be a local physics hinge (reacts to players, may differ per client, TC13) or a code sway (identical for all, never reacts); state which.
- **Scale:** cost per copy × copies on screen decides, and no per-copy cost is documented (SD01): measure at the peak count on the floor phone (`animation-craft` §6). Animated models get no far LOD (TC20); client motion restarts on stream-in at a believable phase (TC23); offer a still or slow variant for reduced motion (TC29).
- **Checks:** copies out of step; loop seam clean; measured cost at the peak count on the target phone (or BLOCKED without a phone).
