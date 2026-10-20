---
title: AnimationConstraint
description: AnimationConstraint aligns two base parts with an animate-able kinematic or force-based joint.
tags: [roblox, documentation, external-reference, priority-reference, physics, animation]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/animation.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/animation.md). Published page: [https://create.roblox.com/docs/physics/constraints/animation](https://create.roblox.com/docs/physics/constraints/animation).

<Alert severity="info">
For an overview on creating, visualizing, and simulating mover constraints, including `Class.AnimationConstraint`, see [[external/roblox-creator-docs/physics/mover-constraints|mover constraints]]. Also see [[external/roblox-creator-docs/physics/units|Roblox&nbsp;units]] to understand how Roblox units compare to metric units.
</Alert>

An `Class.AnimationConstraint` constrains its `Class.Attachment|Attachments` by an offset [transform](#transform). It can be either [kinematic](#kinematic) for snap‑to behavior or it can follow the target trajectory using [force and torque](#force-and-torque). limited by `Class.AnimationConstraint.MaxForce|MaxForce` and `Class.AnimationConstraint.MaxTorque|MaxTorque`.

<video controls src="../../assets/physics/constraints/AnimationConstraint-Demo.mp4"></video>

## Transform

The constraint's `Class.AnimationConstraint.Transform|Transform` is the internal `Datatype.CFrame` that's manipulated when the constraint is being animated. How this transform is reached depends on the constraint's [kinematic](#kinematic) setting.

<figure>
<video controls src="../../assets/physics/constraints/AnimationConstraint-Transform.mp4" width="90%"></video>
</figure>

## Kinematic

When the constraint's `Class.AnimationConstraint.IsKinematic|IsKinematic` property is `true`, the connected parts snap to the [transform](#transform) instantly and precisely without participating in physics simulation. When `false`, the connected parts follow the trajectory using [force and torque](#force-and-torque).

<figure>
<video controls src="../../assets/physics/constraints/AnimationConstraint-IsKinematic.mp4" width="90%"></video>
</figure>

## Force and torque

If the constraint is **not** set to [kinematic](#kinematic), the connected parts follow a trajectory toward the [transform](#transform) using a maximum force/torque limited by `Class.AnimationConstraint.MaxForce|MaxForce` and `Class.AnimationConstraint.MaxTorque|MaxTorque` respectively.


## Related Files

- [[external/roblox-creator-docs/physics/constraints/align-orientation]] - AlignOrientation.
- [[external/roblox-creator-docs/physics/constraints/align-position]] - AlignPosition.
- [[external/roblox-creator-docs/physics/constraints/angular-velocity]] - AngularVelocity.
- [[external/roblox-creator-docs/physics/constraints/ball-socket]] - BallSocket.
- [[external/roblox-creator-docs/physics/constraints/cylindrical]] - Cylindrical.
- [[external/roblox-creator-docs/physics/constraints/hinge]] - Hinge.
- [[external/roblox-creator-docs/physics/constraints/linear-velocity]] - LinearVelocity.
- [[external/roblox-creator-docs/physics/constraints/line-force]] - LineForce.
- [[external/roblox-creator-docs/physics/constraints/no-collision]] - NoCollision.
- [[external/roblox-creator-docs/physics/constraints/plane]] - Plane.
- [[external/roblox-creator-docs/physics/constraints/prismatic]] - Prismatic.
- [[external/roblox-creator-docs/physics/constraints/rigid]] - Rigid.
- [[external/roblox-creator-docs/physics/constraints/rod]] - Rod.
- [[external/roblox-creator-docs/physics/constraints/rope]] - Rope.
- [[external/roblox-creator-docs/physics/constraints/spring]] - Spring.
- [[external/roblox-creator-docs/physics/constraints/torque]] - Torque.
- ...and 4 more local docs.
