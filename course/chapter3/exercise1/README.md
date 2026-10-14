# BM25

While TF-IDF is a good start, there's a keyword ranking algorithm called [Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25) that performs even better. BM25 addresses three problems with basic TF-IDF:

1. **Better IDF calculation:** More stable scoring for rare and common terms
2. **Term frequency saturation:** Prevents terms from dominating by appearing too often
3. **Document length normalization:** Accounts for long and short documents

## The IDF Problem

In basic TF-IDF, IDF is calculated as `log(N / df)`:

- **N** = total number of documents in the collection
- **df** = document frequency (how many documents contain this term)
- **log** = logarithm function (reduces the impact of very large numbers)

The problems with this formula are:

- **Division by zero:** When `df = 0` (we "solved" this by adding `1` to both the numerator and denominator)
- **Unstable rare terms:** Very rare terms get extremely high scores
- **Zero scores:** Terms that appear in every document can bottom out at `0`

## BM25 IDF Solution

BM25 uses a more _stable_ IDF formula:

```py
IDF = log((N - df + 0.5) / (df + 0.5) + 1)
```

Let's break down the reasoning behind each piece, starting with the core ratio:

```py
(N - df + 0.5) / (df + 0.5)
```

This compares the documents that **don't contain** the term against documents that **do contain** it.

- **Numerator `(N - df + 0.5)`:** Documents without the term, plus smoothing
- **Denominator `(df + 0.5)`:** Documents with the term, plus smoothing

### What Is Smoothing?

The _smoothing_ part of this formula is where we add `0.5` to the numerator and denominator, then add `1` to the division result.

- **Why add `0.5`?** To prevent division by `0`. The fancy term for this is [Laplace smoothing](https://en.wikipedia.org/wiki/Additive_smoothing).
- **Why add `1`?** The final `+ 1` ensures IDF is always positive, which handles some edge cases.

## Assignment

In this lesson we'll focus on the first improvement offered by BM25: **better IDF calculation**.

1. [ ] Add a new method, with a signature like `get_bm25_idf(self, term: str) -> float`, to your `InvertedIndex` class.
   1. [ ] Use the BM25 IDF formula: `log((N - df + 0.5) / (df + 0.5) + 1)`, where `N` is the total number of documents and `df` is the document frequency.
   2. [ ] Assume `term` is a single token.
   3. [ ] Return the calculated BM25 IDF score.
2. [ ] Add a function that allows this new method to be called and tested. I named mine `bm25_idf_command`. It should:
   1. [ ] Accept a single argument – the term to get the BM25 IDF score for.
   2. [ ] Load the inverted index from disk.
   3. [ ] Tokenize the term with your single-term helper function.
   4. [ ] Call the `get_bm25_idf` method (or whatever you named it) with the single token.
   5. [ ] Return the BM25 IDF score for the term, as a float.
3. [ ] Back in your entrypoint script, i.e. `keyword_search_cli.py`, add a new `bm25idf` command:
   ```py
   bm25_idf_parser = subparsers.add_parser(
       "bm25idf", help="Get BM25 IDF score for a given term"
   )
   bm25_idf_parser.add_argument("term", type=str, help="Term to get BM25 IDF score for")
   ```
4. [ ] Handle the `bm25idf` command in your match statement:
   1. [ ] Call the BM25 IDF command function.
   2. [ ] Print the result formatted to 2 decimal places (using whatever variable name you assigned):
      ```py
      print(f"BM25 IDF score of '{args.term}': {bm25idf:.2f}")
      ```

**Run and submit** the CLI tests.
