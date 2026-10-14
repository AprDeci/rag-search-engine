# Score Normalization

What if we could choose to use BM25 **and** semantic search by combining them? That'd be really powerful.

The problem is that we can't directly compare BM25 and semantic scores because they're on **different scales**:

- BM25: `0–100+`
- Cosine: `0–1`

To fix this we need to [**normalize**](<https://en.wikipedia.org/wiki/Normalization_(statistics)>) the scores.

## Min-Max Normalization

The simplest approach is to scale all scores to the range `0–1` using **min-max normalization**. This rescales the scores based on the minimum and maximum values in the set, with the minimum score becoming `0` and the maximum score becoming `1`.

1. Start with the list of scores.
2. Find the minimum and maximum scores.
3. For each score, calculate its normalized value: `(score - min_score) / (max_score - min_score)`

For example, say we have these scores:

```py
[15.2, 8.7, 6.3, 2.1]
```

- `min_score = 2.1`
- `max_score = 15.2`

The formula is then applied as follows:

```py
(15.2 - 2.1) / (15.2 - 2.1) = 1.00
(8.7  - 2.1) / (15.2 - 2.1) = 0.50
(6.3  - 2.1) / (15.2 - 2.1) = 0.32
(2.1  - 2.1) / (15.2 - 2.1) = 0.00
```

And this is the resulting normalized list:

```py
[1.00, 0.50, 0.32, 0.00]
```

If we normalize our BM25 and semantic scores to the same `0–1` range using min-max normalization, we can then combine them effectively!

## Assignment

**Add a `normalize` CLI command to your hybrid search script.** It should accept a list of scores and print the normalized values.

1. [ ] If no scores are given, don't print anything.
2. [ ] If the minimum and maximum scores are the same, print a list of `1.0` values.
3. [ ] Otherwise, print the new normalized scores using the min-max normalization described above.

Print in the following format using `print(f"* {score:.4f}")` to round to 4 decimal places:

```sh
uv run cli/hybrid_search_cli.py normalize 0.5 2.3 1.2 0.5 0.1
# * 0.1818
# * 1.0000
# * 0.5000
# * 0.1818
# * 0.0000
```

> [!tip]
> You can use the [`nargs="*"`](https://docs.python.org/3/library/argparse.html#nargs) keyword argument for `add_argument` to gather zero or more command line arguments into a list.

**Run and submit** the CLI tests.
