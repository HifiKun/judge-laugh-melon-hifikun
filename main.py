"""One-line joke for make.fun's "Make the AI Judge Laugh" bounty.

The whole entry is a single funny line about office life, at most 200
characters, written to /output/entry.txt. The setup is the boss's favourite
line — "we're a family here" — and the turn treats it literally: if we are
family, where is the family discount on rent? The first draft rambled
("keeps saying", "asked him", "my rent"); the revision cuts every word that
does not earn its place, so the joke lands in one breath with the turn at
the end.
"""

from pathlib import Path

JOKE = (
    "My boss says we're a family here, "
    "so I asked when the family discount on rent kicks in."
)


def main() -> None:
    # The gate only accepts 1-200 characters of real text, and the judge
    # reads a single cold line, so collapse any stray whitespace first.
    text = " ".join(JOKE.split())
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
