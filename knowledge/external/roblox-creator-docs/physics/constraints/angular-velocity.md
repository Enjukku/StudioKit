---
title: AngularVelocity
description: The AngularVelocity constraint applies torque on an assembly to maintain a constant angular velocity.
tags: [roblox, documentation, external-reference, priority-reference, physics]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/angular-velocity.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/angular-velocity.md). Published page: [https://create.roblox.com/docs/physics/constraints/angular-velocity](https://create.roblox.com/docs/physics/constraints/angular-velocity).

<Alert severity="info">
For an overview on creating, visualizing, and simulating mover constraints, including `Class.AngularVelocity`, see [[external/roblox-creator-docs/physics/mover-constraints|mover constraints]]. Also see [[external/roblox-creator-docs/physics/units|Roblox&nbsp;units]] to understand how Roblox units compare to metric units.
</Alert>

An `Class.AngularVelocity` constraint applies torque on an assembly to maintain a constant angular velocity.

<video controls src="../../assets/physics/constraints/AngularVelocity-Demo.mp4" width="90%" alt="Demo video of AngularVelocity constraint"></video>

<Alert severity="warning">
The `Class.AngularVelocity` constraint applies torque that attempts to maintain a **constant** angular velocity. If you want to control the amount of torque applied, use a [[external/roblox-creator-docs/physics/constraints/torque|Torque]] constraint. Alternatively, if you only need **initial** angular velocity, set the `Class.BasePart.AssemblyAngularVelocity|AssemblyAngularVelocity` method directly on the assembly.
</Alert>

## Relativity

Application of velocity can be controlled through the constraint's `Class.AngularVelocity.RelativeTo|RelativeTo` property. If set to `Enum.ActuatorRelativeTo|World`, the angular velocity vector is used as is. If set to `Enum.ActuatorRelativeTo|Attachment1` and the constraint's `Class.Constraint.Attachment1|Attachment1` property is set to another attachment, the angular velocity will be affected by that of the other attachment as seen by how the upper-left red part's velocity affects the attached blue part's velocity.

<GridContainer numColumns="2">
  <figure>
    <video controls src="../../assets/physics/constraints/AngularVelocity-RelativeTo-World.mp4" alt="Video showing relative behavior set to world space"></video>
    <figcaption>RelativeTo = **World**</figcaption>
  </figure>
  <figure>
    <video controls src="../../assets/physics/constraints/AngularVelocity-RelativeTo-Attachment1.mp4" alt="Video showing relative behavior set to Attachment1"></video>
    <figcaption>RelativeTo = **Attachment1**</figcaption>
  </figure>
</GridContainer>

<Alert severity="info">
Setting `Class.AngularVelocity.RelativeTo|RelativeTo` to `Enum.ActuatorRelativeTo|Attachment1` also exposes the `Class.AngularVelocity.ReactionTorqueEnabled|ReactionTorqueEnabled` property.
</Alert>


## Related Files

- [[external/roblox-creator-docs/physics/constraints/align-orientation]] - AlignOrientation.
- [[external/roblox-creator-docs/physics/constraints/align-position]] - AlignPosition.
- [[external/roblox-creator-docs/physics/constraints/animation]] - AnimationConstraint.
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
