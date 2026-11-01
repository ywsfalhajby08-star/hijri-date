"""Command-line interface: ``hijri-date [YYYY-MM-DD]``."""

from __future__ import annotations

import argparse
import sys

from . import __version__, format_hijri, to_gregorian, to_hijri, today_hijri


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="hijri-date",
        description="Convert a Gregorian date to Hijri (or Hijri to Gregorian with --reverse).",
    )
    parser.add_argument("date", nargs="?", help="date as YYYY-MM-DD (default: today)")
    parser.add_argument(
        "-r", "--reverse", action="store_true",
        help="treat DATE as a Hijri date and print the Gregorian date",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(argv)

    try:
        if args.reverse:
            if not args.date:
                parser.error("--reverse requires a date")
            y, m, d = (int(p) for p in args.date.split("-"))
            print(to_gregorian(y, m, d).isoformat())
        else:
            print(format_hijri(*(to_hijri(args.date) if args.date else today_hijri())))
    except (ValueError, OverflowError) as exc:
        print(f"hijri-date: error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
