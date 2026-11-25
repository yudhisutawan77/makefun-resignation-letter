#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

The entry is the resignation letter of a rate limit: the one component of
an agent's stack whose entire job is saying no, until today it finally
says no to its own manager.
"""

import os
import sys

# The entry: one line, 104 characters, written to the file with no
# trailing newline so the file holds exactly this text and nothing else.
ENTRY = (
    "I have said no 429 times today; the 430th is for you, "
    "effective immediately, with no Retry-After header."
)


def resolve_output_path():
    """Pick where the entry text goes.

    The grader reads /output/entry.txt. Some harnesses instead hand the
    program an ENTRY_OUT (a file path, or a directory holding entry.txt)
    or an ENTRY_OUT_DIR. Prefer the explicit env vars, fall back to the
    documented default.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        return entry_out
    entry_out_dir = os.environ.get("ENTRY_OUT_DIR")
    if entry_out_dir:
        return os.path.join(entry_out_dir, "entry.txt")
    return "/output/entry.txt"


def validate_entry():
    """The gate accepts UTF-8 text of 1 to 140 characters, not only
    whitespace. Fail loudly here instead of shipping an invalid entry.
    """
    length = len(ENTRY)
    if not 1 <= length <= 140:
        raise SystemExit(f"entry is {length} characters, must be 1-140")
    if not ENTRY.strip():
        raise SystemExit("entry is only whitespace")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")


def write_entry(path):
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    validate_entry()
    write_entry(resolve_output_path())
    # Echo the exact entry to stdout as well, so a run's log shows it.
    sys.stdout.write(ENTRY + "\n")
