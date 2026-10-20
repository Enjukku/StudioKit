---
title: Universal
description: UniversalConstraint ensures two axes on two assemblies remain perpendicular, useful for applications such as vehicle power transmission to rear drive shafts, robotics, and more.
tags: [roblox, documentation, external-reference, priority-reference, physics]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/universal.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/universal.md). Published page: [https://create.roblox.com/docs/physics/constraints/universal](https://create.roblox.com/docs/physics/constraints/universal).

<Alert severity="info">
For an overview on creating, visualizing, and simulating mechanical constraints, including `Class.UniversalConstraint`, see [[external/roblox-creator-docs/physics/mechanical-constraints|Mechanical constraints]]. Also see [[external/roblox-creator-docs/physics/units|Roblox&nbsp;units]] to understand how Roblox units compare to metric units.
</Alert>

A `Class.UniversalConstraint` ensures two axes on two assemblies remain perpendicular. Example applications include vehicle power transmission to the rear drive shafts, robotics, and more.

<video controls src="../../assets/physics/constraints/Universal-Demo.mp4" width="90%" alt="Demo video of UniversalConstraint"></video>

## Orientations

Orientation of a universal's two attachments affects how it will move. To ensure it behaves correctly, the `Class.Attachment.SecondaryAxis|SecondaryAxis` of the attachments, visualized by the orange arrows, should be **perpendicular** to each other. Note that a green L-shaped indicator appears when the axes are properly oriented.

<Tabs>
  <TabItem label="Axes Perpendicular">
    <img src="../../assets/physics/constraints/Universal-Attachments-Correct.jpg" width="672" height="378" alt="Secondary axes perpendicular for correct behavior" />
  </TabItem>
  <TabItem label="Axes Misoriented">
    <img src="../../assets/physics/constraints/Universal-Attachments-Incorrect.jpg" width="672" height="378" alt="Secondary axes misoriented" />
  </TabItem>
</Tabs>

## Limits

Enabling the `Class.UniversalConstraint.LimitsEnabled|LimitsEnabled` property exposes the `Class.UniversalConstraint.MaxAngle|MaxAngle` limit to restrict tilt within a cone, as well as `Class.UniversalConstraint.Restitution|Restitution` which defines the elasticity of the attachments when they reach the limit.


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
