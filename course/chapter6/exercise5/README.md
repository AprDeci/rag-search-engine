# Reciprocal Rank Fusion

![Reciprocal Rank Fusion Explainer Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/RRF-1920x1080.mp4)

Score normalization can be messy. Min-max normalization doesn't work well with major outliers, or if the data you're combining has different kinds of distributions.

What if we could **skip scores entirely**? That's what [Reciprocal Rank Fusion](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion) (RRF) does!

```py
def rrf_score(rank: int, k: int = 60) -> float:
    return 1 / (k + rank)
```

It uses _rankings_ instead of _scores_. A ranking is just a position in a list, so instead of:

- Document A = 15.2
- Document B = 8.7
- Document C = 6.3

We use numbered ranks:

- Document A = 1st
- Document B = 2nd
- Document C = 3rd

## Example Result Set

Say we run a query through keyword and semantic search, and get these score-based results:

- **BM25:**
  - _Brother Bear_ (15.2)
  - _Jungle Book_ (8.7)
  - _Paddington_ (6.3)
- **Semantic:**
  - _Paddington_ (0.8)
  - _Brother Bear_ (0.7)
  - _We Bare Bears_ (0.6)

We can use the `rrf_score` function to convert these into rrf rankings:

- **BM25:**
  1. _Brother Bear_ – `1 / (60 + 1) = 0.0164`
  2. _Jungle Book_ – `1 / (60 + 2) = 0.0161`
  3. _Paddington_ – `1 / (60 + 3) = 0.0159`
- **Semantic:**
  1. _Paddington_ – `1 / (60 + 1) = 0.0164`
  2. _Brother Bear_ – `1 / (60 + 2) = 0.0161`
  3. _We Bare Bears_ – `1 / (60 + 3) = 0.0159`

To create a hybrid ranking, we can just sum the RRF scores for each document across both result sets:

- _Brother Bear_: `0.0164 + 0.0161 = 0.0325`
- _Paddington_: `0.0164 + 0.0159 = 0.0323`
- _Jungle Book_: `0.0161`
- _We Bare Bears_: `0.0159`

## What's the K Parameter?

The `k` parameter (a constant) controls _how much more weight_ we give to higher-ranked results vs. lower-ranked ones.

- **Lower `k` values like `20`:** Gives more weight to top-ranked results, creating a steep drop-off in scores.
- **Higher `k` values like `100`:** Creates a more gradual decline, giving lower-ranked results more influence.

> [!isaac]
> A good "default" value for `k` is around `60`; this tends to work well across many datasets and queries.

## Assignment

**Build hybrid search using Reciprocal Rank Fusion.**

1. [ ] Add a new `rrf-search` command to your hybrid search CLI script.
   - [ ] It should accept a required positional `query` parameter.
   - [ ] It should accept an optional `-k` parameter (default to `60`).
   - [ ] It should accept an optional `--limit` parameter (default to `5`).
2. [ ] Implement the missing `rrf_search` method in your `HybridSearch` class. It should:
   - [ ] Call the `_bm25_search` method to get BM25 results. Again, get `500` times the actual limit.
   - [ ] Call the search method of `ChunkedSemanticSearch` to get semantic chunk results for the same query. Again, get `500` times the actual limit.
   - [ ] Combine the results from both searches **using Reciprocal Rank Fusion** as follows:
     - [ ] Create a dictionary mapping document IDs to the documents themselves and their BM25 and semantic _ranks_ (not scores).
     - [ ] For each document, calculate the RRF score using the `rrf_score` function and add that score to each document as well. If a document shows up in both searches, sum its RRF scores.
     - [ ] Return the results sorted by the RRF score in descending order.
3. [ ] Hook up your `rrf-search` command to your `HybridSearch` class's `rrf_search` method. It should call the method and return the results, truncated to the specified limit, in this format:

   ```text
   1. Paddington
     RRF Score: 0.033
     BM25 Rank: 1, Semantic Rank: 1
     Deep in the rainforests of Peru, a young bear lives peacefully with his Aunt Lucy and Uncle Pastuzo,...

   2. The Indian in the Cupboard
     RRF Score: 0.031
     BM25 Rank: 2, Semantic Rank: 8
     On his ninth birthday, Omri receives an old cupboard from his brother Gillon (Vincent Kartheiser) an...
   ```

**Run and submit** the CLI tests.
