---
title: Rope
description: RopeConstraint prevents two attachments from separating further than a defined length, with optional behavior as an extending or contracting winch.
tags: [roblox, documentation, external-reference, priority-reference, physics]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/rope.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/rope.md). Published page: [https://create.roblox.com/docs/physics/constraints/rope](https://create.roblox.com/docs/physics/constraints/rope).

<Alert severity="info">
For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.RopeConstraint`, see [[external/roblox-creator-docs/physics/mechanical-constraints|Mechanical constraints]]. Also see [[external/roblox-creator-docs/physics/units|Roblox&nbsp;units]] to understand how Roblox units compare to metric units.
</Alert>

A `Class.RopeConstraint` prevents two attachments from separating further than a defined `Class.RopeConstraint.Length|Length`. The attachments can move closer together than this length and both can freely rotate. `Class.RopeConstraint.Restitution|Restitution` defines the elasticity of the attachments when they reach the separation limit specified by `Class.RopeConstraint.Length|Length`.

This constraint can also be powered to behave as a [motorized winch](#winch).

<video controls src="../../assets/physics/constraints/Rope-Demo.mp4" width="90%" alt="Demo video of RopeConstraint"></video>

## Winch

If a rope's `Class.RopeConstraint.WinchEnabled|WinchEnabled` property is enabled, it attempts to translate the attachments to a set separation specified by `Class.RopeConstraint.WinchTarget|WinchTarget`, effectively the target length of the rope in studs. This translation is controlled by `Class.RopeConstraint.WinchSpeed|WinchSpeed`, `Class.RopeConstraint.WinchResponsiveness|WinchResponsiveness`, and `Class.RopeConstraint.WinchForce|WinchForce`.

<Alert severity="info">
`Class.RopeConstraint.WinchSpeed|WinchSpeed` must be a **positive** value, used to either contract or extend the rope length to `Class.RopeConstraint.WinchTarget|WinchTarget`. Setting a negative speed will revert to&nbsp;0, not reverse the winch servo direction.
</Alert>


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
- [[external/roblox-creator-docs/physics/constraints/spring]] - Spring.
- [[external/roblox-creator-docs/physics/constraints/torque]] - Torque.
- ...and 4 more local docs.
