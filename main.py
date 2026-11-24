"""Write a vending machine's pickup line to /output/entry.txt.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

LINE = "My best seller isn't the cola. It's the five seconds you stand here deciding."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # The grader collects the output as another user, so it must be readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
