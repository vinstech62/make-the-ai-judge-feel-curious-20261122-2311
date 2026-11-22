#!/usr/bin/env python3
"""Make the AI judge feel curious — make.fun bounty entry.

Writes one short text (273 Unicode code points) to /output/entry.txt.
Deterministic: the same text on every run, no network, no randomness.
"""

import os

TEXT = (
    "The lighthouse keeper writes one letter a year, to no one. "
    "He seals it, drops it in the sea, and watches the lamp turn. "
    "Tonight the tide brought one back \u2014 dry, unopened, in his own "
    "handwriting, addressed to him. He hasn't opened it. "
    "Some letters wait for the right reader."
)

# The gate requires 1-280 Unicode code points, not only whitespace.
# The text is 273 code points; fail loudly instead of writing an
# invalid entry if it ever drifts out of range.
assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "entry text out of gate range"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
