> Author: J018 maker character-rigger · claude-opus-5-5 · high · 2026-10-22. Part of `rigging-design`: built also from the owner's Riot transcripts (J018). Worked rig plans in our pipeline (Blender by Python + MCP, Roblox Studio through the Studio MCP). Numbers below are examples of the form, not budgets: real values come from the rig sheet, the game profile or the owner.

# Worked rig plans

Each example follows `SKILL.md` §3 and names the self-review lines it leans on (§8 P-lines; `rigging-craft/references/tests.md` §6 G- and R-lines).

## 1. Boss knight with a cape and a greatsword (custom NPC, AnimationController)
- **Read (step 1):** a slow, heavy boss; stomps; overhead slam is the tell the player must dodge; game camera 14 studs behind and above the player, so the knight is seen from the front at a distance, often half-screen.
- **Needs (step 2):** the slam's wind-up lifts both arms over the helmet: clavicle raise and hip sink are needed; a spin attack: head world-orient needed; hands: grip only, no finger shapes; hook shapes: the helmet plume and the cape tip.
- **Screen (step 4):** the gorget's high collar sits across the neck cut → the modeler lowers it at the back so the head can pitch; the cape hangs over the arms in the reference → split behind the shoulders, mounted on the back plate; the cape is a costly part: reason "boss presence", fallback a rigid two-plate cape; kept as a 3-bone chain driven as one mass plus offsets.
- **Routes (step 5):** head R-cut under the gorget; shoulders R-cut under the pauldrons (cover exists); elbows R-skin inside the vambraces; cape R-skin chain; greatsword its own MeshPart on a Motor6D with `Grip_R` and `Grip_L` sockets and a `BladeTip` socket for the trail.
- **Pushes (step 8):** the slam's impact squash is VFX dust and a camera nudge owned by VFX; the rig gives a `BladeTip` socket and the ground-contact frame.
- **Posed plan (step 10):** slam wind-up, slam contact, spin at 180°: overlaps (hands vs helmet, sword vs cape) 0 new pairs; cap exposure 0 from the game camera and the back; black-fill: sword above the helmet as its own shape, the cape tip visible at the wind-up. 3 poses + 1 close view of the wind-up. (P-04, P-07, P-11)

## 2. Fox pet seen small (custom pet, AnimationController, many on screen)
- **Read:** a friendly follower; hops; seen at about 12 studs behind the owner, small on a phone.
- **Spend articulation where it reads (D-14):** head turn and tilt, two ears (left and right independent), a 4-bone tail driven as one mass plus offsets (the hook shape: its swoop must show from behind), a body bob on the root; no spine chain, no paw toes.
- **Routes:** head R-cut in the fur ruff; ears R-cut in their creases; legs R-skin at shoulder and hip (no cover); tail R-skin chain.
- **Posed plan:** hop apex, landing, tail curled over the back: black-fill from behind at the game camera shows the tail swoop separate from the body and both ears; tail-to-body overlap pairs 0. The fox is small in the phone frame, so its component count is taken on the crop of its box, with the area check (`rigging-craft/references/tests.md` §2); an ear tip under the listing limit means a closer count render. Crowd cost is a game budget measured on the phone at release (release item RB6), never assumed.

## 3. Blocky toy-style custom player (Humanoid, not an avatar body)
- **Read:** a toy look with visible joint breaks is approved in the art bible; the player sees their own back most.
- **Needs:** throws and jumps need shoulder energy, but the game uses the standard 15-joint body for shared clips: no clavicles, so the plan gives UpperTorso and the upper arm the extra range the wind-up needs, and states it at K2. Hands: no fingers; a fist and an open-hand swap mesh per hand, swapped by the builder on named events.
- **Routes:** every joint R-cut with ball-and-socket covers; the overlap depth comes from the widest §B extreme, checked as cap exposure from the back camera.
- **One convention (D-21):** the same joint, socket and control names as the game's other characters, so the shared clip library plays.

## 4. Mimic chest (prop creature, Motor6D rig)
- **Kinematic diagram first:** base fixed; lid on the hinge line (never the mesh centre); a 5-bone tongue chain; teeth rigid on the lid and base.
- **Moving parts with room:** the lid opens 110° without the hinge cap showing; the tongue's travel is cleared of the teeth (overlap pairs 0 through the full cycle).
- **A tell before it bites:** §B asks for a building tell before the snap: a small lid-rattle range on the hinge, keyed by the animator; the rig only gives the range.
- **Push:** the landing squash is a swap mesh of the base (same pivot and sockets, volume kept), shown for 2 frames by a named event; no clip scale (P-09, R-09).

## 5. Sword skin variant (held item on the shared character rig)
- **Fixed from the base:** the grip, guard and `BladeTip` sockets, the rest pose and the bone names, so every shared clip plays (R-11).
- **New:** a fin that slides open in the inspect clip: its own part with a pivot and a rail, travel cleared of the hand; a control so the animator can open it toward the camera.
- **Check:** socket positions equal the base within the rig sheet tolerance; the base equip, swing and inspect clips play on the variant with no hand or body clipping (overlap pairs 0 at the swing extremes).
