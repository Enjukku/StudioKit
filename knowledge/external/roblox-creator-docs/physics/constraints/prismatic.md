---
title: Prismatic
description: PrismaticConstraint allows two attachments to slide along one axis but not rotate, with optional assigned power for mechanisms like sliding doors and elevator platforms.
tags: [roblox, documentation, external-reference, priority-reference, physics]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/prismatic.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/prismatic.md). Published page: [https://create.roblox.com/docs/physics/constraints/prismatic](https://create.roblox.com/docs/physics/constraints/prismatic).

<Alert severity="info">
For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.PrismaticConstraint`, see [[external/roblox-creator-docs/physics/mechanical-constraints|Mechanical constraints]]. Also see [[external/roblox-creator-docs/physics/units|Roblox&nbsp;units]] to understand how Roblox units compare to metric units.
</Alert>

A `Class.PrismaticConstraint` creates a rigid joint between two attachments, allowing them to slide along one axis but not rotate. The constraint can also be [powered](#linear-power) for mechanisms like sliding doors and elevator platforms.

<video controls src="../../assets/physics/constraints/Prismatic-Demo.mp4" width="90%" alt="Demo video of PrismaticConstraint"></video>

<Alert severity="info">
Orientation of a prismatic's attachments affects how it will move. To ensure movement occurs along the desired axis, each attachment's `Class.Attachment.Axis|Axis`, visualized by the yellow arrow, should point in the same direction.
</Alert>

## Linear power

If a prismatic's `Class.PrismaticConstraint|ActuatorType` is set to `Enum.ActuatorType|Motor`, it attempts to translate the attachments with the goal of reaching `Class.PrismaticConstraint|Velocity`. You can further control this translation through both `Class.PrismaticConstraint|MotorMaxAcceleration` and `Class.PrismaticConstraint|MotorMaxForce`.

If a prismatic's `Class.PrismaticConstraint|ActuatorType` is set to `Enum.ActuatorType|Servo`, it attempts to translate the attachments to a set separation specified by `Class.PrismaticConstraint|TargetPosition`. This translation is controlled by `Class.PrismaticConstraint|Speed`, `Class.PrismaticConstraint|LinearResponsiveness`, and `Class.PrismaticConstraint|ServoMaxForce`.

<GridContainer numColumns="2">
  <figure>
    <video controls src="../../assets/physics/constraints/Prismatic-ActuatorType-Motor.mp4" alt="Video showing linear power configured for motor behavior"></video>
    <figcaption>ActuatorType = **Motor**</figcaption>
  </figure>
  <figure>
    <video controls src="../../assets/physics/constraints/Prismatic-ActuatorType-Servo.mp4" alt="Video showing linear power configured for servo behavior"></video>
    <figcaption>ActuatorType = **Servo**</figcaption>
  </figure>
</GridContainer>

## Limits

You can set limits to restrict the sliding range a prismatic. Enabling the `Class.PrismaticConstraint|LimitsEnabled` property exposes the `Class.PrismaticConstraint|LowerLimit` and `Class.PrismaticConstraint|UpperLimit` values, as well as `Class.PrismaticConstraint|Restitution` which defines the elasticity of the attachments when they reach either limit.


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
- [[external/roblox-creator-docs/physics/constraints/rigid]] - Rigid.
- [[external/roblox-creator-docs/physics/constraints/rod]] - Rod.
- [[external/roblox-creator-docs/physics/constraints/rope]] - Rope.
- [[external/roblox-creator-docs/physics/constraints/spring]] - Spring.
- [[external/roblox-creator-docs/physics/constraints/torque]] - Torque.
- ...and 4 more local docs.
