#!/usr/bin/env python3
"""Fail clearly when repository validation uses an unsupported Python."""

import argparse
import re
import sys
from typing import Tuple


MINIMUM_VERSION = (3, 10)


def parse_version(value: str) -> Tuple[int, ...]:
    match = re.match(r"^(\d+)\.(\d+)(?:\.(\d+))?", value)
    if not match:
        raise ValueError(f"invalid Python version: {value}")
    return tuple(int(part) for part in match.groups(default="0"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--runtime-version",
        help="version to validate instead of the running interpreter",
    )
    args = parser.parse_args()

    if args.runtime_version:
        try:
            version = parse_version(args.runtime_version)
        except ValueError as error:
            parser.error(str(error))
    else:
        version = tuple(sys.version_info[:3])

    if version[:2] < MINIMUM_VERSION:
        found = ".".join(str(part) for part in version[:3])
        print(
            f"Python 3.10 or newer is required; found {found}. "
            "Install a supported Python and rerun make check.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
