"""The Robot Vacuum's Funniest Excuse — make.fun entry.

One line (120 characters) in which a robot vacuum explains why it missed
a spot: it skipped the corner under the couch because the dust bunnies
there have unionised, and it refuses to cross a picket line.

Why this line: one concrete scene (the corner under the couch), one
specific antagonist (unionised dust bunnies), and the punchline lands on
the vacuum treating a labour dispute as a hard rule it will not break —
a principled excuse, not a malfunction.
"""

import os

LINE = "I skipped the corner under the couch because the dust bunnies there have unionised, and I refuse to cross a picket line."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
