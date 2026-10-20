---
title: Rate limits and throttling
description: Covers rate limits for the Open Cloud v2 Data Stores API.
tags: [roblox, documentation, external-reference, priority-reference, cloud, datastores, ui]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [cloud/guides/data-stores/throttling.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/cloud/guides/data-stores/throttling.md). Published page: [https://create.roblox.com/docs/cloud/guides/data-stores/throttling](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

<Alert severity="info">
The below limits apply only to [Open Cloud v1](/cloud/reference/features/storage#Datastores_ListDatastoresAsync) endpoints. For [Open Cloud v2](/cloud/reference/features/storage#Cloud_ListDataStores) rate limits, see [[external/roblox-creator-docs/cloud-services/data-stores/error-codes-and-limits#access-limits|Data store error codes and limits]].
</Alert>

The [Data Stores API](/cloud/reference/features/storage) enforces two types of throttling: **requests per minute** and **throughput**. Each game allows a certain number of requests per minute and a certain amount of data per minute. These limits are enforced for the universe (experience / game) regardless of the number of API keys used.

Unlike the Engine API, these limits do **not** scale based on user count. Exceeding either one causes the endpoint to return `429 Too Many Requests`.

## Legacy standard data stores throttling limits

These limits apply to the legacy `/datastores/v1/` endpoints.

<table>
  <thead>
    <tr>
      <th>Request type</th>
      <th>Method</th>
      <th>Throttle limits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Write</td>
      <td>
        <ul>
          <li>Create Data Store Entry</li>
          <li>Delete Data Store Entry</li>
          <li>Update Data Store Entry</li>
          <li>Increment Data Store Entry</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>10 MB/minute/universe write throughput</li>
          <li>300 requests/minute/universe</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Read</td>
      <td>
        <ul>
          <li>List Data Stores</li>
          <li>List Data Store Entries</li>
          <li>Get Data Store Entry</li>
          <li>List Data Store Entry Revisions</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>20 MB/minute/universe read throughput</li>
          <li>300 requests/minute/universe</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Delete</td>
      <td>
        <ul>
          <li>Delete Data Store</li>
          <li>Undelete Data Store</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>300 requests/minute/universe</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Legacy ordered data stores throttling limits

These limits apply to the legacy `/ordered-data-stores/v1/` endpoints.

<table>
  <thead>
    <tr>
      <th>Request type</th>
      <th>Method</th>
      <th>Throttle limits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Write</td>
      <td>
        <ul>
          <li>Create Ordered Data Store Entry</li>
          <li>Delete Ordered Data Store Entry</li>
          <li>Update Ordered Data Store Entry</li>
          <li>Increment Ordered Data Store Entry</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>300 requests/minute/universe</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Read</td>
      <td>
        <ul>
          <li>List Ordered Data Store Entries</li>
          <li>Get Ordered Data Store Entry</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>300 requests/minute/universe</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>


## Related Files

- [[external/roblox-creator-docs/cloud/guides/data-stores/request-handling]] - Handle Open Cloud data store requests.
- [[external/roblox-creator-docs/cloud/guides/data-stores/index]] - Open Cloud data stores.
