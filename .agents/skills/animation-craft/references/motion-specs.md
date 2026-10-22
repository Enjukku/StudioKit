> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-craft`. Facts: `knowledge/reference/animation/fact-check-techniques.md` (RT<q>-<n> rows, TC facts, SD silent items; mirror revision 7400643, read 2026-10-21). Template: `templates/anim/motion-spec.md`. The animator writes the spec; a builder (feature-builder or quick-builder) writes the code; values live in data. Revised by J018 maker animator · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§2 items 10-12).

# Code-driven and physics motion: what the spec must say

## 1. Choose the mover
| Mover | Good for | Facts that decide it |
| --- | --- | --- |
| **TweenService** (client) | one start, one end, one curve: doors, chests, lids, levers, signs, bobbing pickups, fog or texture offsets | tweens number, boolean, CFrame, Color3, UDim/UDim2, Vector2/3, Rect, EnumItem (RT1-01); 11 styles (Linear, Sine, Back, Quad, Quart, Quint, Bounce, Elastic, Exponential, Circular, Cubic) × In/Out/InOut (RT1-02); `TweenInfo.new(time, style, direction, repeatCount, reverses, delayTime)`, `-1` repeats forever, defaults 1 s, Quad, Out (RT1-02, RT1-03); a server tween replicates every frame (RT1-05) |
| **CFrame / PivotTo loop** (client) | continuous or input-driven rigid motion: constant rotation, follow, bob with a custom curve | anchor one root, weld the rest, move with `PivotTo` (TC05); one loop per system, never per object (TC08); a shared curve via `TweenService:GetValue(alpha, style, direction)` or a follower via `SmoothDamp` (RT1-09, TC04); `BulkMoveTo` only for a measured bottleneck (TC06); no tween of a whole Model: `PivotTo` from a loop or a tweened helper value (TC28) |
| **Motor6D.Transform** (PreSimulation) | rigid hierarchies moved every frame by code (turret aim, gear trains) | the documented efficient path; an Animator on the same rig overwrites it (TC07) |
| **Keyed clip on a Motor6D rig** (AnimationController + Animator) | several linked parts with authored timing: drawbridge with chains, windmill with gears, a machine cycle | needs `rig-pipeline` (TC09); client Animator for decoration (TC10) |
| **Constraints** (server-owned or local decoration) | motion that reacts to players or gravity: swinging signs, trapdoors, ropes; servo doors and lifts; motor wheels | Hinge: ActuatorType None / Motor / Servo; Servo `TargetAngle` in **degrees**, `AngularSpeed` in **rad/s**; limits `LowerAngle` / `UpperAngle` (RT3-01). Prismatic: Servo `TargetPosition` (studs), `Speed` (studs/s), properties on `SlidingBallConstraint` (RT3-02). Cylindrical = slide + rotate (RT3-03). Spring and torsion spring for closers and suspension (RT3-04). Sleep when idle; actuated joints use a stricter threshold (RT3-10, RT3-11); any constraint change wakes the assembly, so write servo targets on state change only (RT3-12, TC14). Owner simulates; free mechanisms may differ per client (RT3-15, SD07) |
| **Texture offset / flipbook** | surface motion: water, belts, lava, fire, glow | `Texture` `OffsetStudsU/V` tween or step (RT1-11, TC16); flipbooks ≤ 8×8 at ≤ 30 fps, may be off on low-memory phones (TC17) |

## 2. What every spec states (the builder must not guess)
1. **Read and feel** in one line each.
2. **Pivot or rail** with position, axis and space (a door's hinge line, not its centre). Rotation preview from two views in the evidence.
3. **Travel** with units (state degrees vs radians per property: the hinge mixes them, RT3-01).
4. **Phases** with lengths and curves; each curve has a reason ("Quart Out: heavy door, fast start, long settle" is a choice; name it PROPOSAL until the owner sees it).
5. **End state and interruption:** a second tween cancels the first and `Cancel()` leaves the part mid-way (RT1-04, RT1-08): say which end state wins when retriggered, and what `Completed` (fires on finish or cancel, not on pause, RT1-07) should do.
6. **Who runs it:** client for cosmetic motion; server owns the gameplay state (open, locked, occupied, damaging) and collision. A trap's damage never reads the client's visual state (TC30).
7. **Streaming and late join:** client motion on server-made instances is lost on stream-out; restart on stream-in from the current state (TC23). A late joiner sees the current state, never a replay.
8. **Events** on the timing list (same ids as VFX and sound).
9. **Checks:** pivot right; phase times from the Output log; copies out of step; off-screen rule.
10. **Feel of the curve:** the prop's personality in 3-5 words (a door that is "heavy, old, grinding" vs "light, cheap, rattly") and the curve that shows it: a small anticipation where something gives first (a latch rattle), eased starts and stops (constant speed only for a mechanism running steadily), one clear arrival, a small overshoot and settle (Back or Elastic easing) where energy should show, never ease-in-out on the whole travel of something heavy. The end state reads in a still.
11. **Reduced motion and pulses:** what the motion does when the player reduces motion (stop, slow, or snap to the end state; the state change itself stays visible). A looping bob or pulse on a pickup or hazard is at most 3 cycles per second and follows its meaning: slow and steady for safe, faster for urgent.
12. **Truth:** a trap's danger pose lasts exactly as long as the danger, and its visible reach matches the gameplay area read from data.

## 3. Examples (short; full reasoning in `animation-design/references/worked-examples.md`)
| Object | Mover | Spec core |
| --- | --- | --- |
| Heavy wooden door | client tween of the door CFrame about the hinge pivot (official doors example tweens CFrame between targets, Quart InOut, one script for all doors: RT1-10) | latch rattle 0 → small angle; travel to the open angle with an out-ease; hard stop with a small settle; server owns `open` and collision; retrigger mid-swing reverses from the current angle |
| Elevator | prismatic servo, server-owned (official elevator toggles `TargetPosition` with a servo: RT3-02) | gentle start and stop; never moves while its door is open; occupancy server-owned |
| Windmill | client `PivotTo` or `Motor6D.Transform` loop at constant angular speed; or a hinge motor if it must physically push things | constant speed: no ease inside the loop; speed linked to the wind design value; one loop for all windmills |
| Swinging tavern sign | local hinge (reacts to the player, may differ per client) or a client code sway (identical, never reacts) | state which and why; low swing that settles |
| Conveyor or river | texture offset scroll | speed in studs/s matches the gameplay belt speed if items ride it |

## 4. Silent in the docs (measure before relying on it)
SD01 per-copy cost of each mover · SD04 a LocalScript tween on a server-made part with a second client watching · SD07 constraint determinism across clients · SD10 cost of many idle vs cycling servo doors · SD12 server servo vs server tween traffic. Each has a Studio measurement in `fact-check-techniques.md`.
