# Punctuation

We're going to keep it _really_ simple for now by removing punctuation before matching text.

**Examples:**

- `Boots the bear!` → `Boots the bear`
- `The wonderful bear, Boots` → `The wonderful bear Boots`

There are cases where this doesn't work well, such as hyphenated words, but we don't need to worry about them yet.

## Assignment

**Remove all punctuation** from both the query and the title before attempting to match them.

Here are some of the standard library functions I used:

- [`.translate()`](https://docs.python.org/3/library/stdtypes.html#str.translate)
- [`str.maketrans()`](https://docs.python.org/3/library/stdtypes.html#str.maketrans)
- [`string.punctuation`](https://docs.python.org/3/library/string.html#string.punctuation)

**Run and submit** the CLI tests.
