---
title: BallSocket
description: BallSocketConstraint forces its two attachments into the same position and allows them to freely rotate about all three axes, with optional limits to restrict both tilt and twist.
tags: [roblox, documentation, external-reference, priority-reference, physics]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/ball-socket.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/ball-socket.md). Published page: [https://create.roblox.com/docs/physics/constraints/ball-socket](https://create.roblox.com/docs/physics/constraints/ball-socket).

<Alert severity="info">
For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.BallSocketConstraint`, see [[external/roblox-creator-docs/physics/mechanical-constraints|Mechanical constraints]]. Also see [[external/roblox-creator-docs/physics/units|Roblox&nbsp;units]] to understand how Roblox units compare to metric units.
</Alert>

A `Class.BallSocketConstraint` forces its two attachments into the same position and allows them to freely rotate about all three axes. However, you can enable limits to restrict both tilt and twist.

<video controls src="../../assets/physics/constraints/BallSocket-Demo.mp4"></video>

## Limits

You can set limits to restrict both **tilt** and **twist** of a ball socket, similar to how a human's head can tilt and turn within a limited axial range. Enabling the `Class.BallSocketConstraint.LimitsEnabled|LimitsEnabled` property exposes the `Class.BallSocketConstraint.UpperAngle|UpperAngle` value to restrict **tilt** within a cone; it also exposes the `Class.BallSocketConstraint.TwistLimitsEnabled|TwistLimitsEnabled` property which, when enabled, lets you restrict **twist** rotation through the `Class.BallSocketConstraint.TwistLowerAngle|TwistLowerAngle` and `Class.BallSocketConstraint.TwistUpperAngle|TwistUpperAngle` limits.

<figure>
<video controls src="../../assets/physics/constraints/BallSocket-Limits-Tilt.mp4" width="90%"></video>
<figcaption>Constraint with `Class.BallSocketConstraint.LimitsEnabled|LimitsEnabled` set to `true` and `Class.BallSocketConstraint.UpperAngle|UpperAngle` set to `15`</figcaption>
</figure>

<figure>
<video controls src="../../assets/physics/constraints/BallSocket-Limits-Twist.mp4" width="90%"></video>
<figcaption>Constraint with `Class.BallSocketConstraint.LimitsEnabled|LimitsEnabled` and `Class.BallSocketConstraint.TwistLimitsEnabled|TwistLimitsEnabled` set to `true`, `Class.BallSocketConstraint.TwistLowerAngle|TwistLowerAngle` set to `-60`, and `Class.BallSocketConstraint.TwistUpperAngle|TwistUpperAngle` set to `0`</figcaption>
</figure>

<Alert severity="info">
Enabling `Class.BallSocketConstraint.LimitsEnabled|LimitsEnabled` also exposes the `Class.BallSocketConstraint.Restitution|Restitution` value which defines the elasticity of the attachments at their tilt and/or twist limits.
</Alert>

<Alert severity="warning">
When `Class.BallSocketConstraint.LimitsEnabled|LimitsEnabled` is enabled, orientation of a ball socket's attachments affects how it rotates. To ensure rotation occurs around the desired axis, each attachment's `Class.Attachment.Axis|Axis`, visualized by the yellow arrow, should point in the same direction.
</Alert>


## Related Files

- [[external/roblox-creator-docs/physics/constraints/align-orientation]] - AlignOrientation.
- [[external/roblox-creator-docs/physics/constraints/align-position]] - AlignPosition.
- [[external/roblox-creator-docs/physics/constraints/angular-velocity]] - AngularVelocity.
- [[external/roblox-creator-docs/physics/constraints/animation]] - AnimationConstraint.
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
