---
title: Rigid
description: RigidConstraint connects two attachments with zero offset.
tags: [roblox, documentation, external-reference, priority-reference, physics]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [physics/constraints/rigid.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/physics/constraints/rigid.md). Published page: [https://create.roblox.com/docs/physics/constraints/rigid](https://create.roblox.com/docs/physics/constraints/rigid).

A `Class.RigidConstraint` connects two `Class.Attachment|Attachments` or `Class.Bone|Bones` and ensures they stay in the same relative position/orientation to each other. This flexibility gives it additional functionality beyond `Class.WeldConstraint`, such as attaching accessories to `Class.Attachment|Attachments` on a character rig.

<Alert severity="info">
To attach two `Class.BasePart|BaseParts` together, versus two `Class.Attachment|Attachments` or `Class.Bone|Bones`, see [[external/roblox-creator-docs/physics/constraints/weld|WeldConstraint]].
</Alert>

When creating a `Class.RigidConstraint` using Studio's [[external/roblox-creator-docs/physics/mechanical-constraints#create-constraints|Constraint]] button, the tool behaves differently depending on whether you click on existing `Class.BasePart|BaseParts`, `Class.Attachment|Attachments`, or `Class.Bone|Bones` after the tool is activated:

- Clicking on an existing `Class.BasePart` creates a new `Class.Attachment` upon it as the intended `Class.RigidConstraint.Attachment0` or `Class.RigidConstraint.Attachment1`.
- Clicking on an existing `Class.Attachment` or `Class.Bone` uses that instance as the intended `Class.RigidConstraint.Attachment0` or `Class.RigidConstraint.Attachment1`.

Following the second valid click, a new `Class.RigidConstraint` is created to connect the two new attachments. If either the first or second click is **not** made on a `Class.BasePart`, `Class.Attachment`, or `Class.Bone`, the workflow is canceled and no constraint is created.


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
- [[external/roblox-creator-docs/physics/constraints/rod]] - Rod.
- [[external/roblox-creator-docs/physics/constraints/rope]] - Rope.
- [[external/roblox-creator-docs/physics/constraints/spring]] - Spring.
- [[external/roblox-creator-docs/physics/constraints/torque]] - Torque.
- ...and 4 more local docs.
