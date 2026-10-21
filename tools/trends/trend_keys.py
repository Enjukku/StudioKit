#!/usr/bin/env python3
"""API keys for trend collectors: read only from environment variables, added to the request URL only at
fetch time, and redacted from every error text.

KeyedFetch wraps a fetch(url, headers, timeout). PoliteClient only ever sees the URL without the key, so its
FetchFailed messages and the collector's log lines cannot hold the key. Any exception from the wrapped fetch
is re-raised as OSError with the key removed (PoliteClient treats it as a network error). The last
response headers are kept so a collector can read Cache-Control and Date.

Python 3.11+ standard library only.
"""
from __future__ import annotations

import os
from urllib.parse import quote

REDACTED = "<redacted>"


class MissingKey(Exception):
    pass


def key_from_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise MissingKey(f"environment variable {name} is not set; no request made")
    return value


def redact(text: str, key: str) -> str:
    return text.replace(key, REDACTED).replace(quote(key, safe=""), REDACTED)


class KeyedFetch:
    def __init__(self, fetch, param: str, key: str):
        self.fetch, self.param, self.key = fetch, param, key
        self.last_headers: dict = {}

    def __call__(self, url: str, headers: dict, timeout: float):
        sep = "&" if "?" in url else "?"
        try:
            status, resp_headers, body = self.fetch(f"{url}{sep}{self.param}={quote(self.key, safe='')}",
                                                    headers, timeout)
        except Exception as err:  # noqa: BLE001 - any error text may echo the keyed URL
            raise OSError(redact(f"{type(err).__name__}: {err}", self.key)) from None
        self.last_headers = resp_headers
        return status, resp_headers, body
