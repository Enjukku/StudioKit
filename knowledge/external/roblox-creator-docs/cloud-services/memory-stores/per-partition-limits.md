---
title: Partitions and data distribution
description: Explains the concept of a partition and how memory stores distribute data.
tags: [roblox, documentation, external-reference, priority-reference, cloud, services, memory, optimization]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [cloud-services/memory-stores/per-partition-limits.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/cloud-services/memory-stores/per-partition-limits.md). Published page: [https://create.roblox.com/docs/cloud-services/memory-stores/per-partition-limits](https://create.roblox.com/docs/cloud-services/memory-stores/per-partition-limits).

The MemoryStores API stores data on partitions so it can scale throughput across data structures. Sorted maps and queues each reside on one partition, while hash maps automatically spread items across many partitions. This page explains how that assignment works.

## Partitions

The MemoryStores API stores data on _partitions_, which are just subdivisions of storage. Whenever you write an item to a memory store, that item is stored on exactly one partition. Partitions are fully managed by the MemoryStores API; you do not need to manage them yourself.

## Partition assignment

Partition storage is different according to the data structure an item is being stored on. For sorted maps and queues, each data structure is assigned a single partition.

For example, consider a carnival game with a sorted map called `PlayerScores` and a queue called `PlayerLine` of players waiting to play the game:

<img src="../../assets/data/memory-store/Per-Partition-Limits-1.png" width="100%" />

Unlike sorted maps and queues, hash maps are allotted multiple partitions, and data is automatically distributed across these partitions. If you were to add a hash map called `Prizes`, the partitions might look like this:

<img src="../../assets/data/memory-store/Per-Partition-Limits-3.png" width="100%" />

Note how the hash map exists on all partitions, and each partition has some subset of items.

For the request limits that apply to each partition and to individual hash map keys, see [[external/roblox-creator-docs/cloud-services/memory-stores/index#per-partition-limits|Per-partition limits]]. For guidance on spreading load across keys and data structures, see [[external/roblox-creator-docs/cloud-services/memory-stores/best-practices|best practices]].


## Related Files

- [[external/roblox-creator-docs/cloud-services/memory-stores/best-practices]] - Best practices for memory stores.
- [[external/roblox-creator-docs/cloud-services/memory-stores/hash-map]] - Memory store hash map.
- [[external/roblox-creator-docs/cloud-services/memory-stores/observability]] - Memory store observability.
- [[external/roblox-creator-docs/cloud-services/memory-stores/queue]] - Memory store queue.
- [[external/roblox-creator-docs/cloud-services/memory-stores/sorted-map]] - Memory store sorted map.
- [[external/roblox-creator-docs/cloud-services/memory-stores/index]] - Memory stores.
