#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's final one-liner to /output/entry.txt.
The line is a single line of at most 199 characters, spoken by the
phone itself as its battery hits 1 percent.
"""

import os

# The phone's last words: Low Power Mode was a cry for help, and the
# punch lands on the way the phone dies — the way it lived.
LAST_WORDS = (
    "Low Power Mode was my cry for help. "
    "You turned it on, then opened TikTok. "
    "I die as I lived: buffering."
)

MAX_CHARS = 199


def main() -> None:
    line = LAST_WORDS.strip()
    if not line or len(line) > MAX_CHARS or "\n" in line:
        raise SystemExit("entry line must be one line of 1-199 characters")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(line)
    # Read the file back and check the gate again on what is actually
    # on disk, so a partial write can never pass as a valid entry.
    with open(out_path, encoding="utf-8") as fh:
        written = fh.read()
    if written != line:
        raise SystemExit("entry.txt does not match the entry line")
    print(f"wrote {len(written)} characters to {out_path}")


if __name__ == "__main__":
    main()
