---
title: TorsionSpring
description: TorsionSpringConstraint applies torque based on a relative angle and relative angular velocity, in an attempt to bring two axes from two parts together.
tags: [roblox, documentation, external-reference, priority-reference, physics]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/torsion-spring.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/torsion-spring.md). Published page: [https://create.roblox.com/docs/physics/constraints/torsion-spring](https://create.roblox.com/docs/physics/constraints/torsion-spring).

<Alert severity="info">
For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.TorsionSpringConstraint`, see [[external/roblox-creator-docs/physics/mechanical-constraints|Mechanical constraints]]. Also see [[external/roblox-creator-docs/physics/units|Roblox&nbsp;units]] to understand how Roblox units compare to metric units.
</Alert>

A `Class.TorsionSpringConstraint` applies torque based on a relative angle and relative angular velocity. It attempts to bring two axes from two parts together and is useful for [[external/roblox-creator-docs/physics/constraints/hinge|hinged]] swinging doors with a spring-back effect.

<video controls src="../../assets/physics/constraints/TorsionSpring-Demo.mp4" width="90%" alt="Demo video of TorsionSpringConstraint"></video>

<Alert severity="info">
Correct orientation of a torsion spring's attachments is important. The constraint will attempt to bring the `Class.Attachment.SecondaryAxis|SecondaryAxis` of each attachment, visualized by the orange arrows, into alignment. When building mechanisms like swinging doors, ensure that the secondary axes are **perpendicular** to the intended axis of rotation.
</Alert>

## Damping

The `Class.TorsionSpringConstraint.Damping|Damping` value controls how fast the spring's oscillation dies down. A value of 0 allows the spring to oscillate endlessly, while higher values bring the spring to a rest more quickly.

<GridContainer numColumns="2">
  <figure>
    <video controls src="../../assets/physics/constraints/TorsionSpring-Damping-0.mp4" alt="Video showing Damping set to 0"></video>
    <figcaption>Damping = **0**</figcaption>
  </figure>
  <figure>
    <video controls src="../../assets/physics/constraints/TorsionSpring-Damping-50.mp4" alt="Video showing Damping set to 50"></video>
    <figcaption>Damping = **50**</figcaption>
  </figure>
</GridContainer>

## Stiffness

`Class.TorsionSpringConstraint.Stiffness|Stiffness` sets the torsional strength of the spring. Higher values create a spring that responds with more force.

## Limits

Enabling the `Class.TorsionSpringConstraint.LimitsEnabled|LimitsEnabled` property exposes the `Class.TorsionSpringConstraint.MaxAngle|MaxAngle` value to restrict the spring's range within a cone; it also exposes the `Class.TorsionSpringConstraint.Restitution|Restitution` value which defines the elasticity of the attachments when they reach their limit.


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
