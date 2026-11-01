"""hijri-date: convert dates between the Hijri (Umm al-Qura) and Gregorian calendars."""

from __future__ import annotations

import datetime as _dt

from hijridate import Gregorian, Hijri

__all__ = ["to_hijri", "to_gregorian", "today_hijri", "format_hijri", "ARABIC_MONTHS"]
__version__ = "0.1.0"

ARABIC_MONTHS = (
    "محرم",
    "صفر",
    "ربيع الأول",
    "ربيع الآخر",
    "جمادى الأولى",
    "جمادى الآخرة",
    "رجب",
    "شعبان",
    "رمضان",
    "شوال",
    "ذو القعدة",
    "ذو الحجة",
)


def _as_date(value: _dt.date | str) -> _dt.date:
    if isinstance(value, _dt.datetime):
        return value.date()
    if isinstance(value, _dt.date):
        return value
    return _dt.date.fromisoformat(value)


def to_hijri(value: _dt.date | str) -> tuple[int, int, int]:
    """Convert a Gregorian date (``date`` or ``"YYYY-MM-DD"``) to a Hijri ``(year, month, day)``."""
    d = _as_date(value)
    h = Gregorian(d.year, d.month, d.day).to_hijri()
    return (h.year, h.month, h.day)


def to_gregorian(year: int, month: int, day: int) -> _dt.date:
    """Convert a Hijri date to a Gregorian ``datetime.date``."""
    return Hijri(year, month, day).to_gregorian()


def today_hijri() -> tuple[int, int, int]:
    """Return today's date in the Hijri calendar as ``(year, month, day)``."""
    return to_hijri(_dt.date.today())


def format_hijri(year: int, month: int, day: int) -> str:
    """Format a Hijri date with the Arabic month name, e.g. ``22 جمادى الأولى 1448 هـ``."""
    if not 1 <= month <= 12:
        raise ValueError(f"invalid Hijri month: {month}")
    return f"{day} {ARABIC_MONTHS[month - 1]} {year} هـ"
