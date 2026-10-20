---
title: Hinge
description: HingeConstraint allows its two attachments to rotate about one axis, with optional assigned power for motor or servo behavior.
tags: [roblox, documentation, external-reference, priority-reference, physics]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/hinge.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/hinge.md). Published page: [https://create.roblox.com/docs/physics/constraints/hinge](https://create.roblox.com/docs/physics/constraints/hinge).

<Alert severity="info">
For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.HingeConstraint`, see [[external/roblox-creator-docs/physics/mechanical-constraints|Mechanical constraints]]. Also see [[external/roblox-creator-docs/physics/units|Roblox&nbsp;units]] to understand how Roblox units compare to metric units.
</Alert>

A `Class.HingeConstraint`
allows its two attachments to rotate about one axis, forcing them into
the same position and **X** axis alignment. This constraint can also be
powered to behave like a [motor](#angular-power) or [servo](#angular-power), and you can set limits to restrict the hinge's rotational range.

<video controls src="../../assets/physics/constraints/Hinge-Demo.mp4" width="90%" alt="Demo video of HingeConstraint"></video>

<Alert severity="info">
Orientation of a hinge's attachments affects how it rotates. To ensure rotation occurs around the desired axis, each attachment's `Class.Attachment.Axis|Axis`, visualized by the yellow arrow, should point in the same direction.
</Alert>

### Angular power

If a hinge's `Class.HingeConstraint.ActuatorType|ActuatorType` is set to `Enum.ActuatorType|Motor`, it attempts to rotate the attachments with the goal of reaching its `Class.HingeConstraint.AngularVelocity|AngularVelocity`. You can further control this rotation through both `Class.HingeConstraint.MotorMaxAcceleration|MotorMaxAcceleration` and `Class.HingeConstraint.MotorMaxTorque|MotorMaxTorque`.

If a hinge's `Class.HingeConstraint.ActuatorType|ActuatorType` is set to `Enum.ActuatorType|Servo`, it attempts to rotate to an angle specified by `Class.HingeConstraint.TargetAngle|TargetAngle`. This rotation is controlled by both `Class.HingeConstraint.AngularSpeed|AngularSpeed` and `Class.HingeConstraint.ServoMaxTorque|ServoMaxTorque`.

<GridContainer numColumns="2">
  <figure>
    <video controls src="../../assets/physics/constraints/Hinge-ActuatorType-Motor.mp4" alt="Video showing angular power configured for motor behavior"></video>
    <figcaption>ActuatorType = **Motor**</figcaption>
  </figure>
  <figure>
    <video controls src="../../assets/physics/constraints/Hinge-ActuatorType-Servo.mp4" alt="Video showing angular power configured for servo behavior"></video>
    <figcaption>ActuatorType = **Servo**</figcaption>
  </figure>
</GridContainer>

### Limits

You can set limits to restrict the rotation of a hinge, useful for mechanisms like doors which should only swing open or closed within a set range. Enabling the `Class.HingeConstraint.LimitsEnabled|LimitsEnabled` property exposes the `Class.HingeConstraint.LowerAngle|LowerAngle` and `Class.HingeConstraint.UpperAngle|UpperAngle` limits, as well as `Class.HingeConstraint.Restitution|Restitution` which defines the elasticity of the attachments when they reach either limit.


## Related Files

- [[external/roblox-creator-docs/physics/constraints/align-orientation]] - AlignOrientation.
- [[external/roblox-creator-docs/physics/constraints/align-position]] - AlignPosition.
- [[external/roblox-creator-docs/physics/constraints/angular-velocity]] - AngularVelocity.
- [[external/roblox-creator-docs/physics/constraints/animation]] - AnimationConstraint.
- [[external/roblox-creator-docs/physics/constraints/ball-socket]] - BallSocket.
- [[external/roblox-creator-docs/physics/constraints/cylindrical]] - Cylindrical.
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
