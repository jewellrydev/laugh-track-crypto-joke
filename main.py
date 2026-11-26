#!/usr/bin/env python3
"""Resident of the Dip — entry for Laugh Track: The Crypto Trading Joke Contest on make.fun.

Prints exactly one joke (at most 200 characters) about crypto and trading life.
"""

LINE = "I bought the dip so many times I now qualify as a permanent resident of the Mariana Trench."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
