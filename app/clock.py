"""Clocks. The application reads time only through a clock object so that
tests can control it instead of waiting for posts or tokens to expire."""
from datetime import datetime, timedelta, timezone
from typing import Protocol


class Clock(Protocol):
    def now(self) -> datetime: ...


class SystemClock:
    """Real UTC time, used in production."""

    def now(self) -> datetime:
        return datetime.now(timezone.utc)


class ManualClock:
    """A clock that only moves when told to. Used by the test suite."""

    def __init__(self, start: datetime):
        if start.tzinfo is None:
            raise ValueError("ManualClock requires a timezone-aware datetime")
        self._now = start.astimezone(timezone.utc)

    def now(self) -> datetime:
        return self._now

    def set(self, value: datetime) -> None:
        if value.tzinfo is None:
            raise ValueError("ManualClock requires a timezone-aware datetime")
        self._now = value.astimezone(timezone.utc)

    def advance(self, **kwargs) -> datetime:
        self._now = self._now + timedelta(**kwargs)
        return self._now
