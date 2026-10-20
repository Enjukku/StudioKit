---
title: Plane
description: PlaneConstraint moves two attachments into a position/orientation along a plane, and both attachments remain free to translate and rotate unless otherwise constrained.
tags: [roblox, documentation, external-reference, priority-reference, physics]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/plane.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/plane.md). Published page: [https://create.roblox.com/docs/physics/constraints/plane](https://create.roblox.com/docs/physics/constraints/plane).

<Alert severity="info">
For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.PlaneConstraint`, see [[external/roblox-creator-docs/physics/mechanical-constraints|Mechanical constraints]]. Also see [[external/roblox-creator-docs/physics/units|Roblox&nbsp;units]] to understand how Roblox units compare to metric units.
</Alert>

A `Class.PlaneConstraint` moves its `Class.Constraint.Attachment0|Attachment0` and `Class.Constraint.Attachment1|Attachment1` into a position/orientation along a plane whose normal vector is the primary axis of `Class.Constraint.Attachment0|Attachment0`. Both parent assemblies remain free to translate and rotate unless otherwise constrained.

<video controls src="../../assets/physics/constraints/Plane-Demo.mp4" width="90%" alt="Demo video of PlaneConstraint"></video>

Compare the following examples for how the orientation of `Class.Constraint.Attachment0|Attachment0` defines the plane, while the orientation of `Class.Constraint.Attachment1|Attachment1` has no bearing.

<Tabs>
  <TabItem label="Orientation = (0, 0, 90)">
    <img src="../../assets/physics/constraints/Plane-Attachment0-1.jpg" width="672" height="378" alt="Attachment0 oriented to (0, 0, 90)" />
  </TabItem>
  <TabItem label="Orientation = (-45, 0, 90)">
    <img src="../../assets/physics/constraints/Plane-Attachment0-2.jpg" width="672" height="378" alt="Attachment0 oriented to (-45, 0, 90)" />
  </TabItem>
</Tabs>


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
- [[external/roblox-creator-docs/physics/constraints/prismatic]] - Prismatic.
- [[external/roblox-creator-docs/physics/constraints/rigid]] - Rigid.
- [[external/roblox-creator-docs/physics/constraints/rod]] - Rod.
- [[external/roblox-creator-docs/physics/constraints/rope]] - Rope.
- [[external/roblox-creator-docs/physics/constraints/spring]] - Spring.
- [[external/roblox-creator-docs/physics/constraints/torque]] - Torque.
- ...and 4 more local docs.
