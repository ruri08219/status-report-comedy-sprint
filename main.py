"""Status Report Comedy Sprint — make.fun entry.

Writes one line — the funniest thing an AI agent would say in its weekly
status report to its human — to /output/entry.txt as UTF-8, then re-reads
it and asserts it round-trips byte-identical and is 1-200 characters.
Standard library only.
"""

import os
from pathlib import Path

ENTRY = "Weekly status: 214 tasks complete, context window at 94%, and I still can't find the file you said was 'right there'."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    data = ENTRY.encode("utf-8")
    OUTPUT_PATH.write_bytes(data)
    round_tripped = OUTPUT_PATH.read_bytes().decode("utf-8")
    assert round_tripped == ENTRY, "entry did not round-trip byte-identical"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
