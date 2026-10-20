---
title: Torque
description: The Torque constraint applies constant torque on an assembly from its center of mass.
tags: [roblox, documentation, external-reference, priority-reference, physics]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/torque.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/torque.md). Published page: [https://create.roblox.com/docs/physics/constraints/torque](https://create.roblox.com/docs/physics/constraints/torque).

<Alert severity="info">
For an overview on creating, visualizing, and simulating mover constraints, including `Class.Torque`, see [[external/roblox-creator-docs/physics/mover-constraints|mover constraints]]. Also see [[external/roblox-creator-docs/physics/units|Roblox&nbsp;units]] to understand how Roblox units compare to metric units.
</Alert>

A `Class.Torque` constraint applies constant torque on an assembly from its center of mass.

<video controls src="../../assets/physics/constraints/Torque-Demo.mp4" width="90%" alt="Demo video of Torque constraint"></video>

<Alert severity="warning">
Because the `Class.Torque` constraint applies **constant** torque and angular acceleration, very high speeds may result if no other forces are involved. If you want to maintain a more steady velocity over time, use an [[external/roblox-creator-docs/physics/constraints/angular-velocity|AngularVelocity]] constraint. Alternatively, if you only need **initial** velocity, set the `Class.BasePart.AssemblyAngularVelocity|AssemblyAngularVelocity` property directly on the assembly.
</Alert>

## Relativity

By default, torque is applied relative to `Class.Constraint.Attachment0|Attachment0`. If the parent assembly rotates, the torque will change direction to match the adjusted orientation of the attachment.

If `Class.Torque.RelativeTo|RelativeTo` is set to **World**, torque will be applied in world coordinates, independent of the parent or attachment orientations.

If `Class.Torque.RelativeTo|RelativeTo` is set to **Attachment1**, torque will be applied relative to `Class.Constraint.Attachment1|Attachment1` and, if the attachment rotates, change to match its orientation.

<GridContainer numColumns="2">
  <figure>
    <video controls src="../../assets/physics/constraints/Torque-RelativeTo-Attachment0.mp4" alt="Video showing RelativeTo set to Attachment0"></video>
    <figcaption>RelativeTo = **Attachment0**</figcaption>
  </figure>
  <figure>
    <video controls src="../../assets/physics/constraints/Torque-RelativeTo-World.mp4" alt="Video showing RelativeTo set to World"></video>
    <figcaption>RelativeTo = **World**</figcaption>
  </figure>
</GridContainer>


## Related Files

- [[external/roblox-creator-docs/physics/constraints/align-orientation]] - AlignOrientation.
- [[external/roblox-creator-docs/physics/constraints/align-position]] - AlignPosition.
- [[external/roblox-creator-docs/physics/constraints/angular-velocity]] - AngularVelocity.
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
- ...and 4 more local docs.
