> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `rigging-design`. Source: animation paper AP:180-541 (notes `knowledge/reference/animation/01-*.md` §5, §12 rigger digest RG01-RG17). Read by the rigger at S1/S2 and S6; the animator's own book (J006) holds the craft.

# What motion asks of a rig

The animator states needs; the rigger decides how (rig-pipeline §1). Use this to read §B, to spot missing needs before K1, and to know what the animator will test at S6.

## 1. What the animator's §B gives you (and what it must not invent)
| Field | Meaning for the rig | Source |
| --- | --- | --- |
| Part inventory | every visible part, also "does not move"; a bone name is not proof of anatomy; a decorative fin, a steering fin and a rigid plate can look alike | AP:184-186 |
| Driver | active (intent, gaze, balance, steering), passive (follows, settles), rigid (rides the parent), mechanical | AP:204-220 |
| ROM | per axis, unit, the pose or clip that needs it, source; an extreme attack pose counts even if locomotion never reaches it | AP:280; RP:117 |
| Contacts | ground, perch, grip, hinge, attachment; planted / rolling / sliding / released; a deliberate skid is allowed | AP:209, 275 |
| Mass | UNKNOWN unless supplied; never from bone length, bounding box or weighted vertex count | AP:188 |
| Delays and springs | no universal per-bone delay or spring constant exists; any value is an authored choice marked OPINION | AP:230, 510 |

## 2. Body part → rig consequence (AP:204-220; rig reading is the extractor's inference, checked by the lead)
| Part | Driven by | Rig consequence |
| --- | --- | --- |
| Root / whole body | travel, braking, support, impulses | root control ≠ centre of mass; in-place clips by default (root motion not released, RR39-RR41) |
| Pelvis, trunk, shoulders | actuation, balance, load transfer | no fixed "hips lead" order built into controls |
| Neck, head | gaze, orientation, stabilization, reaction | head orients independently of the trunk |
| Arms, hands, held prop | reach, grip, leverage, release | prop sockets and grip anchors; both hands + object solved as one system |
| Legs, feet | stance, swing, touchdown, recovery | contact pivots for planted, rolling, sliding |
| Passive tail / strap | base motion, flexibility, gravity, collision | chain with enough segments to follow through |
| Active tail | counterbalance, support, steering, signal | drivable as a primary part; body responds [V B05] |
| Bird wing + tail | takeoff, cruise, brake, land, fold, glide | wing, body, tail controllable together; fold and glide reachable [V B06, B10] |
| Bat wing | extension, membrane, flap, manoeuvre | independent left / right retraction [V B07, B08] |
| Insect wing | stroke amplitude, pitch, frequency | stroke pitch and amplitude joints; sampling plan [V B09] |
| Ears | orientation, sensing, passive tissue | left / right independent of the head [V B16] |
| Antennae | search, contact, deflection | active and passive modes [V B17] |
| Hair, cloth, soft tissue | attachment, stiffness, wind, collision, art direction | per-material choice: keyed, procedural or hybrid; no single delay |
| Fins | propulsion, steering, braking | separate control surfaces; ray curvature varies [V B18] |
| Long body | traction or fluid + travelling wave | many segments; curvature and travel controlled separately [V B14, B15] |
| Hinge, piston, gear | actuator, linkage, hard stop | hard stops and linkage in the rig |

## 3. Clip lists that become test needs (AP:404-454)
| Asset | Clips that stress the rig |
| --- | --- |
| Playable character | idle + variations, start / stop / turn / strafe / back, jump take-off / fall / land, equip / aim / use / reload, attack families, hit / stagger / knockback / death, emotes, any seated / climb / swim / carry state; transitions between them |
| Creature, pet | rest, alert, attention shifts, gait changes, start / stop / turn, flight / glide / fold / perch / swim / burrow / slither only if relevant, follow / catch-up / settle / sleep, correction after teleport; LOD versions that keep identity and major contacts |
| Weapon, tool | hold, equip, ready, aim, use, recoil, recovery, stow, cancel, reload / charge, grip constraints and attachment transfer, first- vs third-person |
| Prop, moving object | rest, start, loop, endpoint, return, interrupted move; pivots, occupancy, wheel and suspension dependencies; collision state separate from cosmetic motion |

## 4. Held tool profile (AP:316-330)
Tool root, head, handle, primary and secondary grip anchors, impact surface. The primary hand sets the attachment policy; the secondary hand follows a solved contact. Grips must not detach in follow-through; the tool must not pass through the floor. Impact: does it stop, rebound or continue?

## 5. What the animator checks at S6 (expect it)
Turntable with labelled rig overlay, unlit silhouette render, unobscured mesh view, saved cameras, joint-limit renders, planted-contact markers with the support region, silhouette at phone size in the gameplay view (AP:192, 582). A pose beyond the rig's stated reach is a rejection: state the reach in §C (AP:280).

## 6. Secondary motion that needs bones
For each passive part decide keyed / procedural / hybrid. A procedural layer needs: target, local frame, rest state, damping and stiffness form, timestep dependence, collision scope, rotation limits, teleport and interruption reset, off-screen behaviour, determinism, authority (AP:510). Never bake a lag into a clip and add a runtime spring on top (AP:512). Cloth that hides the action, costs too much or fails import is reduced or replaced (AP:512).
