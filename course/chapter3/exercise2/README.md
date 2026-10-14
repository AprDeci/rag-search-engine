# Term Frequency Saturation

Now let's tackle the second BM25 improvement: **term frequency saturation**. This prevents a single term from dominating search results just because it appears _many many_ times.

## The Term Frequency Problem

In basic TF-IDF, a word that appears 100 times gets **10x** more weight than a word that appears 10 times. That can create bad rankings:

**Query:** "bear hunting"

- Document A: "bear bear bear bear" → 4 matches
- Document B: "bear hunting guide for beginners" → 2 matches

With basic TF, Document A gets a much higher score despite probably being less useful!

## The Saturation Solution

BM25 uses **diminishing returns** – after a certain point, additional occurrences matter less. Let's break down the formula:

```py
tf_component = (tf * (k1 + 1)) / (tf + k1)
```

`k1` is a tunable parameter that controls the diminishing return; a common value is `1.5`. Here's how different TF values get saturated:

| Occurrences | Basic TF | BM25 TF (k1 = 1.5) |
| ----------: | -------: | -----------------: |
|           1 |        1 |                1.0 |
|           2 |        2 |                1.4 |
|           5 |        5 |                1.9 |
|          10 |       10 |                2.2 |
|          20 |       20 |                2.3 |

Notice how BM25 grows much slower: the first few occurrences matter the most.

![Basic vs BM25 TF Growth](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/jafuwkh-580x447.png)

## Assignment

**Implement the BM25 term frequency saturation formula** in our `InvertedIndex` class. Use a `k1` value of `1.5` to control the saturation effect.

1. [ ] Define a constant to use as the default value for `k1`. You might find it useful to place constants like this in a dedicated module, so they can be reused across different parts of your codebase.
   ```py
   BM25_K1 = 1.5
   ```
2. [ ] Add a new method `get_bm25_tf(self, doc_id, term, k1=BM25_K1)` to your `InvertedIndex` class:
   1. [ ] Get the raw term frequency using your existing `get_tf` method.
   2. [ ] Apply the BM25 saturation formula: `(tf * (k1 + 1)) / (tf + k1)`
   3. [ ] Return the saturated TF score.
3. [ ] Add a new `bm25_tf_command` function that:
   1. [ ] Takes `doc_id`, `term`, and optional `k1` parameters
   2. [ ] Loads the index from disk
   3. [ ] Tokenizes the term with your single-term helper function
   4. [ ] Calls the `get_bm25_tf` method with the provided parameters
   5. [ ] Returns the BM25 TF score
4. [ ] Add a new `bm25tf` command to the `keyword_search_cli.py` entrypoint script:
   ```py
   bm25_tf_parser = subparsers.add_parser(
       "bm25tf", help="Get BM25 TF score for a given document ID and term"
   )
   bm25_tf_parser.add_argument("doc_id", type=int, help="Document ID")
   bm25_tf_parser.add_argument("term", type=str, help="Term to get BM25 TF score for")
   bm25_tf_parser.add_argument(
       "k1", type=float, nargs="?", default=BM25_K1, help="Tunable BM25 K1 parameter"
   )
   ```
5. [ ] Handle the command in your match statement:
   1. [ ] Call the `bm25_tf_command` function with the provided arguments.
   2. [ ] Print the result, formatted to 2 decimal places:
      ```py
      print(f"BM25 TF score of '{args.term}' in document '{args.doc_id}': {bm25tf:.2f}")
      ```

**Run and submit** the CLI tests.
