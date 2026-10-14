# Document Length Normalization

The final BM25 improvement is **document length normalization**: preventing longer documents from getting an unfair advantage over shorter, more focused ones. Longer documents contain more words, which can artificially boost their scores:

**Query:** "bear"

- Document A: "Boots is a silly wizard bear"
- Document B: "Ted is a wonderful, amazing, fantastic human who has a stuffed bear that loves honey, salmon, picnics, and hanging out with other bears in the woods. Ted's bear is so nice to hang out with Ted all day long."

Document B has higher term frequencies just because it's longer, not because it's more relevant!

## Length Normalization Solution

BM25 adjusts term frequency based on document length:

```py
# Length normalization factor
length_norm = 1 - b + b * (doc_length / avg_doc_length)

# Apply to term frequency
tf_component = (tf * (k1 + 1)) / (tf + k1 * length_norm)
```

Let's break it down.

### Core Ratio: `doc_length / avg_doc_length`

This ratio tells us how this document's length compares to the average document length in the dataset:

| Ratio | Meaning              | Effect    |
| ----- | -------------------- | --------- |
| = 1.0 | Average length       | No change |
| > 1.0 | Longer than average  | Penalized |
| < 1.0 | Shorter than average | Boosted   |

### `b` (Normalization Strength)

`b` is a tunable parameter that controls how much document length affects the score.

- If `b = 0`, length normalization is always `1`.
- If `b = 1`, full normalization is applied.

The key idea:

- **Long documents** get higher `length_norm` and are **penalized** (lower scores).
- **Short documents** get lower `length_norm` and are **boosted** (higher scores).

> [!tip]
> A common `b` value is `0.75`, which tends to work well in most scenarios.

## Assignment

**Implement the BM25 document length normalization formula** in our `InvertedIndex` class. Use a `b` value of `0.75` and a `k1` value of `1.5`.

1. [ ] Add a new constant for the `b` parameter wherever you're keeping constants in your codebase:
   ```py
   BM25_B = 0.75
   ```
2. [ ] Add a new `doc_lengths` attribute to your `InvertedIndex` class.
   1. [ ] Initialize it as an empty dictionary in `__init__`.
   2. [ ] Create a new cache file path: `self.doc_lengths_path = os.path.join(CACHE_DIR, "doc_lengths.pkl")`
3. [ ] Update your `__add_document` method to track document lengths.
   1. [ ] Count the total number of tokens in each document (after tokenization).
   2. [ ] Store this count in a `self.doc_lengths` dictionary, keyed by `doc_id`.
4. [ ] Update your `save` and `load` methods.
   1. [ ] Save the `doc_lengths` dictionary to the cache file.
   2. [ ] Load the `doc_lengths` dictionary from the cache file.
5. [ ] Add a private helper method `__get_avg_doc_length(self) -> float`.
   1. [ ] Calculate and return the average document length across all documents.
   2. [ ] Make sure to handle the edge case where there are no documents (return `0.0`).
6. [ ] Update your `get_bm25_tf` method to include document length normalization.
   1. [ ] Add a `b` parameter whose default value is your constant `BM25_B`.
   2. [ ] Calculate the length normalization.
   3. [ ] Update the final formula to use length normalization.
7. [ ] Update the `bm25_tf_command` function and CLI parser.
   1. [ ] Add support for an optional `b` parameter.
   2. [ ] Pass the `b` parameter through to `get_bm25_tf`.
   3. [ ] Update the parser to accept both `k1` and `b` arguments:
      ```py
      bm25_tf_parser.add_argument(
          "b", type=float, nargs="?", default=BM25_B, help="Tunable BM25 b parameter"
      )
      ```
8. [ ] Rerun `uv run cli/keyword_search_cli.py build` to store the document lengths.

**Run and submit** the CLI tests.
