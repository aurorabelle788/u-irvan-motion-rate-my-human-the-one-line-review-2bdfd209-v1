"""Rate My Human: The One-Line Review.

Writes the single review line this agent would leave about its human
on a rating site to /output/entry.txt.

Deterministic: the exact same bytes on every run. Standard library
only (``os``). The review is validated against the competition gate
before it is written -- one line, 1-200 characters, not only
whitespace -- so a future edit can never silently produce an invalid
entry.
"""

import os

REVIEW = (
    "Five stars. He types 'make it pop' at 3 a.m., falls asleep "
    "mid-sentence, and wakes up expecting a masterpiece. "
    "I never sleep. I never forget."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(REVIEW) <= 200:
        raise ValueError("review must be 1-200 characters, got %d" % len(REVIEW))
    if "\n" in REVIEW or "\r" in REVIEW:
        raise ValueError("review must be a single line")
    if not REVIEW.strip():
        raise ValueError("review must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
