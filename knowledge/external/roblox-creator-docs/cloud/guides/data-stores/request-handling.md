---
title: Handle Open Cloud data store requests
description: Explains how to handle Open Cloud API requests for data stores.
tags: [roblox, documentation, external-reference, priority-reference, cloud, datastores, ui]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [cloud/guides/data-stores/request-handling.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/cloud/guides/data-stores/request-handling.md). Published page: [https://create.roblox.com/docs/cloud/guides/data-stores/request-handling](https://create.roblox.com/docs/cloud/guides/data-stores/request-handling).

There are a number of considerations around sending requests to and handling responses from the Open Cloud data store APIs.

## HTTP headers

Like all Open Cloud endpoints, data store requests that use API key authentication must include the `x-api-key` header. For more information, see [[external/roblox-creator-docs/cloud/auth/api-keys|Manage API keys]].

- An incorrect or missing API key results in a 401 error.
- A valid API key that lacks the correct permissions results in a 403 error.

If a request includes a body, such as a create or update request, include the `Content-Type: application/json` and `Content-Length` headers. Most clients include these headers automatically.

## Pagination

Data stores often contain many entries, which means your code, particularly when calling [List Data Store Entries](/cloud/reference/DataStoreEntry#Cloud_ListDataStoreEntries__Using_Universes), must deal with a maximum number of results and pages. To learn more, see [[external/roblox-creator-docs/cloud/reference/patterns#pagination|Pagination]].

## Filters

If you use prefixes in the names of your data store entries, you likely want to filter your GET calls, like so:

```python
def list_entries(universe, data_store, filter):
    list_path = f'universes/{universe}/data-stores/{data_store}/entries'
    url = base_url + list_path
    return requests.get(url, params={'filter': f'id.startsWith("global/{filter}")'}, headers={apiHeaderKey: apiKey})
```

Filter syntax is extremely limited. See the reference documentation for available filters for [standard](/cloud/reference/DataStoreEntry#Cloud_ListDataStoreEntries__Using_Universes) and [ordered](/cloud/reference/OrderedDataStoreEntry#Cloud_ListOrderedDataStoreEntries) data stores.

## Allow missing flags

The PATCH (update) methods for standard and ordered data stores have an `allow_missing` parameter. If set to true, this parameter lets you create entries that don't already exist rather than throwing an error. Leave this parameter at its default value of false unless you have a good reason not to; updating an entry that was never created often represents an error in programming logic.

## Scopes

Many requests require you to specify a scope, even if it's the default value of `global`. These scopes are distinct from permission scopes and let you subdivide and organize the entries in a data store.

Rather than creating non-default scopes, however, we strongly recommend using prefixes. To learn more, see [[external/roblox-creator-docs/cloud-services/data-stores/versioning-listing-and-caching#listing-and-prefixes|Listing and prefixes]].

## Content-MD5

<Alert severity="info">
This section only applies to the Open Cloud v1 API.
</Alert>

The Open Cloud v1 API supports an optional base64-encoded MD5 checksum in some requests, which can catch data integrity issues. Many languages have built-in functions to calculate the value of the `content-md5` header. The following example uses Python:

```python
$ echo "750" | python -c "import base64, hashlib; print(str(base64.b64encode(hashlib.md5(bytes(input(), encoding='utf8')).digest()), encoding='utf8'))"
sTf90fedVsft8zZf6nUg8g==
```

If you run into issues generating a valid `content-md5` value, you might need to encode your request body in UTF-8 before computing the checksum.


## Related Files

- [[external/roblox-creator-docs/cloud/guides/data-stores/index]] - Open Cloud data stores.
- [[external/roblox-creator-docs/cloud/guides/data-stores/throttling]] - Rate limits and throttling.
