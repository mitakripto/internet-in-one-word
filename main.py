"""The Internet in One Word entry.

Writes one word -- the single word that describes the whole
internet -- to /output/entry.txt.

The word is fixed and deterministic: the same bytes on every run.
Procrastopia: the shining place everyone opens a browser to visit,
where the thing you meant to do waits patiently while you fall
down one more wonderful hole instead.
"""

import os

WORD = "Procrastopia"


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters,
    # a single word, not only white space.
    assert 1 <= len(WORD) <= 30, len(WORD)
    # Exactly one word: no whitespace anywhere, no punctuation, letters only.
    assert WORD.split() == [WORD] and WORD.isalpha(), WORD
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
