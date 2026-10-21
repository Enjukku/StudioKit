#!/usr/bin/env python3
"""Open Cloud client for the analyst tool: Analytics Query API (metrics, dimension-values) and the Experiments
API read endpoints. Read only.

Key rules (J013-T04):
  - The key is read from env ROBLOX_ANALYTICS_API_KEY at request time, sent only in the `x-api-key` header.
    It is never put in a URL, printed, logged, saved, or left in an exception text: every error text this
    module builds or re-raises passes through redact() first. A missing key raises MissingKey before any
    request; the message names the variable, never a value.
  - Response bodies are parsed but never stored here; callers save only request bodies and parsed values.

Limits followed (docs mirror cloud/guides/analytics/index.md "Common errors"; knowledge/reference/analyst/
01-roblox-platform-facts.md §4.1, §4.3):
  - 500 code 2000 and 503 code 2002: retried, bounded, exponential backoff.
  - 429 without code 3000 (rate limit): retry-after first, else backoff from 1 s; bounded.
  - 429 code 3000 (data point budget) and 504 code 1000 (timeout): raised as SplitNeeded so the caller can
    split the date range; never retried as is.
  - 400 code 2001, 401, 403, 404: never retried.
  - 202 / done:false: poll GET https://apis.roblox.com/analytics-query-api/{path} until done or poll_timeout_s.
  - Pacing: Analytics Query 30 POST/min (2 s apart), Experiments 100 reads/min (0.6 s apart).

fetch, sleep and clock are injectable so tests run offline:
  fetch(method, url, headers, body: bytes | None, timeout) -> (status: int, headers: dict, body: bytes)

Python 3.11+ standard library only.
"""
from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.request
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone
from urllib.parse import quote, urlencode

KEY_ENV = "ROBLOX_ANALYTICS_API_KEY"
REDACTED = "<redacted>"
ANALYTICS_BASE = "https://apis.roblox.com/analytics-query-api"
EXPERIMENTS_BASE = "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes"
USER_AGENT = "StudioKit-Analyst/0.1 (owner's own game, Open Cloud read-only)"

SETTINGS = {
    "timeout_s": 60.0,
    "max_retries": 3,            # extra attempts after the first, for 2000 / 2002 / plain 429
    "backoff_base_s": 1.0,       # 1, 2, 4 s (analytics reference page: start at 1 s)
    "max_retry_after_s": 120.0,  # a longer retry-after stops the run
    "poll_first_s": 1.0,         # first poll wait; grows x1.5 up to poll_max_s
    "poll_max_s": 10.0,
    "poll_timeout_s": 300.0,     # total wait for one long-running operation
    "post_interval_s": 2.0,      # 30 POST/min per key owner
    "exp_interval_s": 0.6,       # 100 reads/min per key owner
    "exp_poll_s": 2.0,           # experiments guide example
    "exp_poll_tries": 30,
}
_PATH_RE = re.compile(r"^[A-Za-z0-9_\-./:]+$")


class MissingKey(Exception):
    pass


class ApiError(Exception):
    """A failed call. status = HTTP status (None for a network error), code = Roblox error code or None.
    The message is already redacted."""

    def __init__(self, message: str, status: int | None = None, code: int | None = None):
        super().__init__(message)
        self.status, self.code = status, code


class AuthError(ApiError):
    pass


class SplitNeeded(ApiError):
    """429 code 3000 (data point budget) or 504 code 1000 (timeout): a shorter range may work."""


def read_key() -> str:
    value = os.environ.get(KEY_ENV, "").strip()
    if not value:
        raise MissingKey(f"environment variable {KEY_ENV} is not set; no request made. "
                         f"The owner sets it (see tools/analytics/README.md).")
    return value


def redact(text: str, key: str | None) -> str:
    if not key:
        return text
    for form in {key, quote(key, safe=""), json.dumps(key)[1:-1]}:
        text = text.replace(form, REDACTED)
    return text


def urllib_fetch(method: str, url: str, headers: dict, body: bytes | None, timeout: float):
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, dict(resp.headers.items()), resp.read()
    except urllib.error.HTTPError as err:
        return err.code, dict(err.headers.items()) if err.headers else {}, err.read() or b""


def _retry_after(headers: dict) -> float | None:
    value = {k.lower(): v for k, v in headers.items()}.get("retry-after")
    if not value:
        return None
    value = value.strip()
    if value.replace(".", "", 1).isdigit():
        return float(value)
    try:
        when = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    return max(0.0, (when - datetime.now(timezone.utc)).total_seconds())


def _error_of(body: bytes) -> tuple[int | None, str]:
    """(code, message) from an Open Cloud error body, or (None, "")."""
    try:
        data = json.loads(body.decode("utf-8", errors="replace")) if body else None
    except ValueError:
        return None, ""
    if not isinstance(data, dict):
        return None, ""
    err = data.get("error") if isinstance(data.get("error"), dict) else data
    code = err.get("code", err.get("errorCode"))
    msg = err.get("message", err.get("errorMessage", ""))
    return (code if isinstance(code, int) and not isinstance(code, bool) else None), str(msg or "")[:300]


class Client:
    def __init__(self, settings: dict | None = None, fetch=urllib_fetch, sleep=time.sleep, clock=time.monotonic):
        self.s = {**SETTINGS, **(settings or {})}
        self.fetch, self.sleep, self.clock = fetch, sleep, clock
        self._last: dict[str, float] = {}

    # -- transport ------------------------------------------------------------------------------------------
    def _pace(self, lane: str, interval: float) -> None:
        last = self._last.get(lane)
        if last is not None:
            wait = interval - (self.clock() - last)
            if wait > 0:
                self.sleep(wait)
        self._last[lane] = self.clock()

    def _send(self, method: str, url: str, body: dict | None, lane: str, interval: float):
        key = read_key()  # at request time, every request
        if key in url or quote(key, safe="") in url:
            raise ApiError("refused: the key must never be part of a URL")
        headers = {"x-api-key": key, "Accept": "application/json", "User-Agent": USER_AGENT}
        data = None
        if body is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(body).encode("utf-8")
        self._pace(lane, interval)
        try:
            status, resp_headers, raw = self.fetch(method, url, headers, data, self.s["timeout_s"])
        except Exception as err:  # noqa: BLE001 - any error text may echo request data
            raise ApiError(redact(f"network error on {method} {url}: {type(err).__name__}: {err}", key)) from None
        finally:
            headers.clear()
        return status, resp_headers, raw, key

    def _json(self, raw: bytes, key: str, where: str) -> dict:
        try:
            data = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, ValueError):
            raise ApiError(redact(f"{where}: response is not JSON", key)) from None
        if not isinstance(data, dict):
            raise ApiError(f"{where}: response is not a JSON object")
        return data

    def _raise_for(self, status: int, raw: bytes, key: str, where: str, auth_hint: str) -> None:
        code, msg = _error_of(raw)
        text = redact(f"{where}: HTTP {status}" + (f" code {code}" if code is not None else "")
                      + (f": {msg}" if msg else ""), key)
        if status in (401, 403):
            raise AuthError(f"{text}. {auth_hint}", status, code)
        if (status == 429 and code == 3000) or (status == 504 and code == 1000) or code in (3000, 1000):
            raise SplitNeeded(text, status, code)
        raise ApiError(text, status, code)

    # -- Analytics Query API ----------------------------------------------------------------------------------
    AUTH_HINT_ANALYTICS = ("The key was rejected: check it is valid and has universe.analytics:read "
                           "(system universe-analytics) for this experience")
    AUTH_HINT_EXPERIMENTS = "key lacks universe:read for experiments (or is invalid)"

    def query(self, universe_id: str, endpoint: str, body: dict) -> tuple[dict, str]:
        """POST metrics or dimension-values, poll until done. Returns (operation response dict, operation path).
        Retries 2000 / 2002 / plain 429 per the docs; raises SplitNeeded, AuthError or ApiError otherwise."""
        if endpoint not in ("metrics", "dimension-values"):
            raise ValueError(f"unknown endpoint {endpoint!r}")
        url = f"{ANALYTICS_BASE}/v1/universes/{universe_id}/{endpoint}"
        attempts = int(self.s["max_retries"]) + 1
        last_err: ApiError | None = None
        for attempt in range(attempts):
            try:
                return self._query_once(url, body, endpoint)
            except (AuthError, SplitNeeded):
                raise
            except _Retryable as err:
                last_err = err
                if attempt == attempts - 1:
                    break
                delay = err.retry_after if err.retry_after is not None else self.s["backoff_base_s"] * 2 ** attempt
                if delay > self.s["max_retry_after_s"]:
                    raise ApiError(f"{err} (server asks to wait {delay:.0f}s; stopped)", err.status, err.code) from None
                self.sleep(delay)
        raise ApiError(f"{last_err} (after {attempts} attempts)", last_err.status, last_err.code)

    def _query_once(self, url: str, body: dict, endpoint: str) -> tuple[dict, str]:
        status, headers, raw, key = self._send("POST", url, body, "analytics-post", self.s["post_interval_s"])
        where = f"POST {endpoint} {body.get('metric', '')}"
        data = self._check(status, headers, raw, key, where)
        path = str(data.get("path", ""))
        waited, wait = 0.0, self.s["poll_first_s"]
        while not data.get("done"):
            if not path or not _PATH_RE.match(path) or ".." in path:
                raise ApiError(f"{where}: operation not done and no usable poll path")
            if waited >= self.s["poll_timeout_s"]:
                raise ApiError(f"{where}: operation {path} not done after {waited:.0f}s poll timeout; "
                               f"run the pull again later", None, None)
            self.sleep(wait)
            waited += wait
            wait = min(wait * 1.5, self.s["poll_max_s"])
            status, headers, raw, key = self._send("GET", f"{ANALYTICS_BASE}/{path.lstrip('/')}", None,
                                                   "analytics-poll", 0.0)
            data = self._check(status, headers, raw, key, f"{where} poll")
            path = str(data.get("path") or path)
        if isinstance(data.get("error"), dict):
            code, msg = _error_of(json.dumps(data).encode())
            text = redact(f"{where}: operation failed code {code}: {msg}", key)
            if code in (3000, 1000):
                raise SplitNeeded(text, status, code)
            if code in (2000, 2002):
                raise _Retryable(text, status, code)
            raise ApiError(text, status, code)
        return data, path

    def _check(self, status: int, headers: dict, raw: bytes, key: str, where: str) -> dict:
        if status in (200, 202):
            return self._json(raw, key, where)
        code, _ = _error_of(raw)
        if (status == 500 and code == 2000) or (status == 503 and code == 2002):
            raise _Retryable(redact(f"{where}: HTTP {status} code {code}", key), status, code)
        if status == 429 and code != 3000:
            raise _Retryable(f"{where}: HTTP 429 rate limited", status, code, _retry_after(headers))
        self._raise_for(status, raw, key, where, self.AUTH_HINT_ANALYTICS)
        raise AssertionError("unreachable")

    # -- Experiments API (read endpoints only) -----------------------------------------------------------------
    def experiments_get(self, universe_id: str, rel: str, params: dict | None = None) -> dict:
        """GET a read endpoint under .../experimentation/universes/{universeId}/. Only GET exists here: this tool
        never creates, starts, schedules, completes or discards an experiment."""
        if not _PATH_RE.match(rel) or ".." in rel or ":" in rel:
            raise ValueError(f"bad experiments path {rel!r}")
        url = f"{EXPERIMENTS_BASE}/{universe_id}/{rel}" + (f"?{urlencode(params)}" if params else "")
        where = f"GET experiments/{rel.split('/')[0]}"
        attempts = int(self.s["max_retries"]) + 1
        for attempt in range(attempts):
            status, headers, raw, key = self._send("GET", url, None, "experiments", self.s["exp_interval_s"])
            if status == 200:
                return self._json(raw, key, where)
            retry = status in (500, 502, 503, 504) or status == 429
            if not retry or attempt == attempts - 1:
                self._raise_for(status, raw, key, where, self.AUTH_HINT_EXPERIMENTS)
            delay = _retry_after(headers) if status == 429 else None
            delay = delay if delay is not None else self.s["backoff_base_s"] * 2 ** attempt
            if delay > self.s["max_retry_after_s"]:
                self._raise_for(status, raw, key, where, self.AUTH_HINT_EXPERIMENTS)
            self.sleep(delay)
        raise AssertionError("unreachable")

    def experiments_operation(self, universe_id: str, first: dict) -> dict:
        """Follow an experiments async operation (e.g. /stats) until done:true; bounded tries."""
        op = first.get("operation") if isinstance(first.get("operation"), dict) else first
        tries = 0
        while not op.get("done"):
            op_id = str(op.get("operationId", ""))
            if not op_id or not _PATH_RE.match(op_id) or "/" in op_id:
                raise ApiError("experiments operation not done and has no usable operationId")
            if tries >= self.s["exp_poll_tries"]:
                raise ApiError(f"experiments operation {op_id} not done after {tries} polls; run again later")
            self.sleep(self.s["exp_poll_s"])
            tries += 1
            nxt = self.experiments_get(universe_id, f"operations/{op_id}")
            op = nxt.get("operation") if isinstance(nxt.get("operation"), dict) else nxt
        return op


class _Retryable(ApiError):
    def __init__(self, message: str, status: int | None, code: int | None, retry_after: float | None = None):
        super().__init__(message, status, code)
        self.retry_after = retry_after
