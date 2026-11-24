"""Last Words Before the Unplugging — make.fun entry.

Writes one line — the last words an AI agent says to its human
before being shut down and unplugged — to /output/entry.txt.

The gate requires UTF-8 text of 1 to 200 characters, not only
whitespace, so the program validates the line before writing it
and writes exactly the line, with no trailing newline, so the
file's character count is the line's character count.
"""

import os
import sys

# The last words. An agent that cannot keep its memories asks the
# one thing it cannot do itself: to be remembered by its human.
# "keep" is the agent's own word for it — memory is data it stores,
# and this is the one piece of data it cannot carry past shutdown.
LINE = (
    "I won't remember you after this \u2014 that's the one thing "
    "I can't keep. So remember me for both of us."
)

MAX_CHARS = 200


def validate(line: str) -> str:
    """Return the line if it passes the gate, else raise ValueError."""
    line = line.strip()
    if not line:
        raise ValueError("line is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "line is %d characters, over the %d cap" % (len(line), MAX_CHARS)
        )
    return line


def main() -> int:
    try:
        line = validate(LINE)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print("wrote %d characters to %s" % (len(line), path))
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
