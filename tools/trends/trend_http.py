#!/usr/bin/env python3
"""Polite HTTP GET for trend collectors: a minimum interval between requests, HTTP 429 and Retry-After
honoured, exponential backoff with jitter on 429/5xx/network errors, bounded retries, a User-Agent that
names the tool. No cookies, no auth headers, no proxy or IP rotation.

A 429 that says stop (Retry-After over max_retry_after_s, or still 429 after the last retry) ends the run for
this client: every later get() raises FetchFailed without a request (lead decision J004-T12 finding 1; the
Roblox ruling's condition "honour 429 and retry-after"). One client serves one source per run.

fetch, sleep, clock and rng are injectable so tests run offline:
  fetch(url, headers, timeout) -> (status: int, headers: dict[str, str], body: bytes)

Python 3.11+ standard library only.
"""
from __future__ import annotations

import http.client
import os
import random
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

USER_AGENT = "StudioKit-TrendScout/0.1 (studio research tool; public counters only)"


class FetchFailed(Exception):
    pass


def urllib_fetch(url: str, headers: dict, timeout: float) -> tuple[int, dict, bytes]:
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, dict(resp.headers.items()), resp.read()
    except urllib.error.HTTPError as err:
        return err.code, dict(err.headers.items()) if err.headers else {}, err.read() or b""


def retry_after_seconds(value: str | None, now: datetime | None = None) -> float | None:
    """Retry-After as seconds (delta-seconds or HTTP-date); None if absent or unreadable."""
    if not value:
        return None
    value = value.strip()
    if value.isdigit():
        return float(value)
    try:
        when = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    return max(0.0, (when - (now or datetime.now(timezone.utc))).total_seconds())


class PoliteClient:
    def __init__(self, settings: dict, fetch=urllib_fetch, sleep=time.sleep, clock=time.monotonic,
                 rng: random.Random | None = None):
        self.s = settings
        self.fetch, self.sleep, self.clock = fetch, sleep, clock
        self.rng = rng or random.Random()
        self._last: float | None = None
        self.stopped: str | None = None  # reason, once a 429 said stop
        contact = os.environ.get("TREND_CONTACT", "").strip()
        self.headers = {"User-Agent": USER_AGENT + (f" contact: {contact}" if contact else ""),
                        "Accept": "application/json"}

    def _wait_turn(self) -> None:
        if self._last is not None:
            wait = self.s["min_interval_s"] - (self.clock() - self._last)
            if wait > 0:
                self.sleep(wait)
        self._last = self.clock()

    def get(self, url: str) -> bytes:
        """Body of a 200 response. Raises FetchFailed after bounded retries or on a non-retryable status."""
        if self.stopped:
            raise FetchFailed(f"{url}: not requested, this run stopped earlier ({self.stopped})")
        attempts = int(self.s["max_retries"]) + 1
        for attempt in range(attempts):
            self._wait_turn()
            try:
                status, headers, body = self.fetch(url, dict(self.headers), self.s["timeout_s"])
            except (OSError, http.client.HTTPException) as err:  # HTTPException: e.g. IncompleteRead mid-body
                status, headers, body, why = None, {}, b"", f"network error {err}"
            else:
                why = f"HTTP {status}"
            if status == 200:
                return body
            if status is not None and status != 429 and not 500 <= status < 600:
                raise FetchFailed(f"{url}: {why}, not retried")
            if attempt == attempts - 1:
                break
            lower = {k.lower(): v for k, v in headers.items()}
            delay = retry_after_seconds(lower.get("retry-after")) if status == 429 else None
            if delay is None:
                base = self.s["backoff_base_s"]
                delay = base * (2 ** attempt) + self.rng.uniform(0, base)
            if delay > self.s["max_retry_after_s"]:
                if status == 429:
                    self.stopped = f"HTTP 429, Retry-After {delay:.0f}s > max_retry_after_s"
                raise FetchFailed(f"{url}: {why}, server asks to wait {delay:.0f}s (> max_retry_after_s); stopped")
            self.sleep(delay)
        if status == 429:
            self.stopped = f"HTTP 429 after {attempts} attempts"
        raise FetchFailed(f"{url}: {why} after {attempts} attempts; stopped")
