---
title: Rod
description: RodConstraint keeps two attachments separated by a defined length, with optional limits on rotational tilt.
tags: [roblox, documentation, external-reference, priority-reference, physics]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/rod.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/rod.md). Published page: [https://create.roblox.com/docs/physics/constraints/rod](https://create.roblox.com/docs/physics/constraints/rod).

<Alert severity="info">
For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.RodConstraint`, see [[external/roblox-creator-docs/physics/mechanical-constraints|Mechanical constraints]]. Also see [[external/roblox-creator-docs/physics/units|Roblox&nbsp;units]] to understand how Roblox units compare to metric units.
</Alert>

A `Class.RodConstraint` keeps two attachments separated by its defined `Class.RodConstraint.Length|Length`. By default, both attachments can rotate freely, although you can enable limits to restrict rotational tilt.

<video controls src="../../assets/physics/constraints/Rod-Demo.mp4" width="90%" alt="Demo video of RodConstraint"></video>

## Limits

You can limit rotation of the attachments within a cone, independently of each other, by enabling the `Class.RodConstraint.LimitsEnabled|LimitsEnabled` property and setting `Class.RodConstraint.LimitAngle0|LimitAngle0` and `Class.RodConstraint.LimitAngle1|LimitAngle1` respectively.


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
- [[external/roblox-creator-docs/physics/constraints/rope]] - Rope.
- [[external/roblox-creator-docs/physics/constraints/spring]] - Spring.
- [[external/roblox-creator-docs/physics/constraints/torque]] - Torque.
- ...and 4 more local docs.
