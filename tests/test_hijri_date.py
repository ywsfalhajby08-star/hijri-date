import datetime as dt

import pytest

from hijri_date import format_hijri, to_gregorian, to_hijri, today_hijri
from hijri_date.cli import main


def test_to_hijri_string_and_date():
    assert to_hijri("2026-11-02") == (1448, 5, 22)
    assert to_hijri(dt.date(2024, 3, 11)) == (1445, 9, 1)  # 1 Ramadan 1445


def test_to_gregorian():
    assert to_gregorian(1448, 5, 22) == dt.date(2026, 11, 2)
    assert to_gregorian(1445, 9, 1) == dt.date(2024, 3, 11)


def test_round_trip():
    d = dt.date(2000, 1, 1)
    while d < dt.date(2001, 1, 1):
        assert to_gregorian(*to_hijri(d)) == d
        d += dt.timedelta(days=17)


def test_today_hijri():
    assert today_hijri() == to_hijri(dt.date.today())


def test_format_hijri():
    assert format_hijri(1448, 5, 22) == "22 جمادى الأولى 1448 هـ"
    with pytest.raises(ValueError):
        format_hijri(1448, 13, 1)


def test_cli(capsys):
    assert main(["2026-11-02"]) == 0
    assert capsys.readouterr().out.strip() == "22 جمادى الأولى 1448 هـ"


def test_cli_reverse(capsys):
    assert main(["--reverse", "1448-05-22"]) == 0
    assert capsys.readouterr().out.strip() == "2026-11-02"


def test_cli_invalid(capsys):
    assert main(["not-a-date"]) == 1
    assert "error" in capsys.readouterr().err
