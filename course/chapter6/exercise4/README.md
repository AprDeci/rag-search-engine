# Weighted Combination

Normalized scores ready? Let's **combine them**. We'll use the following formula to create a new _weighted hybrid score_ based on the BM25 (keyword) and semantic scores:

```py
def hybrid_score(bm25_score: float, semantic_score: float, alpha: float = 0.5) -> float:
    return alpha * bm25_score + (1 - alpha) * semantic_score
```

`alpha` (or "α") is just a constant that we can use to dynamically control the weighting between the two scores:

```text
α = 1.0: [████████████████████] 100% Keyword
α = 0.7: [██████████████------] 70% Keyword, 30% Semantic
α = 0.5: [██████████----------] 50/50 Split
α = 0.2: [████----------------] 20% Keyword, 80% Semantic
α = 0.0: [--------------------] 100% Semantic
```

As the developer, we want to choose an alpha that seems to work well for the query type. For example:

| Query Type  | Example         | Chosen Alpha | Reason                      |
| ----------- | --------------- | ------------ | --------------------------- |
| Exact match | "The Revenant"  | 0.8          | Title search needs keywords |
| Conceptual  | "family movies" | 0.2          | Meaning matters more        |
| Mixed       | "2015 comedies" | 0.5          | Both year AND concept       |

> [!isaac]
> This is why it's so important to tune your search system's constants based on the types of data and queries you're working with in _your_ application! It's not a one-size-fits-all solution, but building _configurability_ into your system allows you to adjust it as needed.

## Assignment

**Build hybrid search with a configurable `alpha`.**

1. [ ] Add a "weighted-search" command to your hybrid search script.
   - [ ] It should accept a required `query` parameter.
   - [ ] It should accept an optional `--alpha` parameter (default to `0.5`)
   - [ ] It should accept an optional `--limit` parameter (default to `5`)
2. [ ] Implement the missing `weighted_search` method in your `HybridSearch` class. It should:
   - [ ] Call the `_bm25_search` method to get BM25 results. Get _500 times_ the _actual_ limit to ensure we have enough results to work with.
   - [ ] Call the `ChunkedSemanticSearch`'s search method to get semantic results for the same query. Again, get _500 times_ the _actual_ limit.
   - [ ] Combine the results from both searches as follows:
     - [ ] Normalize all the keyword and semantic scores using the `normalize` method you implemented earlier.
     - [ ] Create a dictionary mapping document IDs to the documents themselves and their keyword and semantic scores (I just used a new dictionary to store this information)
     - [ ] Add a third score (the hybrid score) to each document – calculate this using the `hybrid_score` function described above.
     - [ ] Return the results sorted by the hybrid score in descending order.
3. [ ] Hook up your "weighted-search" command to your `HybridSearch` class's `weighted_search` method. It should call the method and return the results truncated to the specified limit in this format:
   ```text
   1. Paddington
     Hybrid Score: 1.000
     BM25: 1.000, Semantic: 1.000
     Deep in the rainforests of Peru, a young bear lives peacefully with his Aunt Lucy and Uncle Pastuzo,...
   2. The Indian in the Cupboard
     Hybrid Score: 0.943
     BM25: 0.966, Semantic: 0.850
     On his ninth birthday, Omri receives an old cupboard from his brother Gillon (Vincent Kartheiser) an...
   ```

**Run and submit** the CLI tests.
