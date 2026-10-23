---
type: template
scope: universal
status: active
updated: 2026-10-22
source: J006; animation paper AP:266-282 (motion profile TP01-TP12), AP:584 (fields for the rigger); rig-pipeline S1; J019 P6 (G3-P6): TP01 slots for `animation-design/references/body-and-species.md` §5
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21; revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6)

# Motion profile: <asset-id> · rig sheet revision <n> (or "no rig")

Animator's own file at S1 (`rig-pipeline`), next to the rig sheet: `content/rigs/<asset-id>/motion-profile.md`, or `content/anim/<asset-id>/` when no rig is needed. The rig sheet §B holds the animator keys copied from here. Every number has a unit and a source (reference id, owner decision id, gameplay window id, measured file) or says PROPOSAL / UNKNOWN. Mass, delays and spring values stay UNKNOWN unless supplied.

## Evidence used
| id | File | What it shows |
| --- | --- | --- |
| V1-V6 | renders/ (front, back, left, right, raised ¾, game camera) | |
| C1 | renders/cameras.json | saved camera transforms |
| M1 | inspect.json | measured geometry facts |

## TP01 Identity and purpose
| Key | Value |
| --- | --- |
| Subject | |
| Feel words (2-4), each with its visible change (`animation-design/references/body-and-species.md` §5) | |
| Identity anchors and hook shapes (2-5) that stay visible at key poses, each with the side the camera sees (`body-and-species.md` §5) | |
| Body shape agrees with the motion? (black-fill read vs brief; a disagreement is asked before keying: `body-and-species.md` §1, §5) | yes / no + question id |
| Costly parts, each with its cheap fallback (`body-and-species.md` §5; `rig-pipeline` §8) | |
| Kind | character / creature / pet / held item / prop or mechanism / vehicle or mount / building / ambient |
| Camera and size on the phone screen | |
| Gameplay role and windows (owner, id) | |
| Clips or motions the brief needs | |

## TP02 Parts (semantic inventory; the rig hierarchy is the rigger's)
| Part | What it is | Carried by | Moves (yes / no / with parent) | Driver (active / passive / rigid / mechanical) | Technique (clip / code / physics / texture) + reason | Views |
| --- | --- | --- | --- | --- | --- | --- |

## TP03-TP05 Scale, mass, support
| Key | Value |
| --- | --- |
| Units, rest size, forward / up | |
| Mass and inertia | UNKNOWN unless supplied; perceived weight: <feel> |
| Contacts (ground, grip, perch, hinge) per clip, with state planted / rolling / sliding / released | |

## TP06-TP08 Drivers, secondary, personality
| Part | What drives it | Secondary response and its cause | Personality cue |
| --- | --- | --- | --- |

## TP09-TP10 Range of motion and stress poses (copied to rig sheet §B)
| Part | Axis | Range (unit) | Needed by (clip or pose) | Source |
| --- | --- | --- | --- | --- |

Stress poses (combined): 
Silhouette that must survive: 
Sockets needed (grip, VFX, sound, hitbox) with orientation: 

## TP11 Runtime
| Key | Value |
| --- | --- |
| Driver | Humanoid + Animator / AnimationController + Animator / code-driven / physics / texture |
| Who plays it (server for replication, or client cosmetic) | |
| Root policy | in place (default; native root motion not released) / other with reason |
| Priority intent and layered joints | |
| On-screen count and LOD intent | |

## TP12 Open questions and decisions
| id | Question | Owner | Default if no answer |
| --- | --- | --- | --- |
