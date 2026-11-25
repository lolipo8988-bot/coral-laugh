"""Write one funny line to /output/entry.txt.

One Line, One Laugh (make.fun): a single line of at most 200
characters. The joke: a dog trained to fetch slippers turns the
trick into a negotiation — the setup is ordinary pet training,
the turn (he withholds the second slipper to bargain) is the laugh.
Revised once after a first run: filler ("for me", "with me",
"the other one") cut so every word earns its place.
"""

import os

TEXT = "I taught my dog to fetch my slippers; now he brings me one and negotiates for the other."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
