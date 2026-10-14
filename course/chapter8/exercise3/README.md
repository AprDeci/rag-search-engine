# LLM Batch Re-Ranking

Using LLMs for re-ranking individual search results is fairly straightforward. Now let's scale it up to do **batch re-ranking**, that is, processing multiple queries more efficiently.

When you have many documents to process, calling the LLM individually for each one can be slow and expensive. We're re-processing the system prompt and query with each call, and adding latency for each individual request.

Even if we ignore speed and cost, the _quality_ of the results can suffer when we re-rank documents individually because it's scoring each independently on an arbitrary scale. By giving it all the documents, we can ask it to simply _rank_ them, which means they'll always be compared against each other in the same context.

## Assignment

**Implement _batch_ re-ranking for RRF search.**

1. [ ] Add a new option to the `--rerank-method` argument. It can now be `"individual"` or `"batch"`.
2. [ ] Again, gather **5 times as many results** as the `limit` specified _if_ a `--rerank-method` is set.
3. [ ] If the `"batch"` re-rank method is provided, _after_ doing the initial RRF search, run the results through a _single LLM prompt_ (this will be much easier on your API limits, and faster). It should include all the documents and the query, and ask for the movie IDs back as a JSON list _in order of relevance_. Here's my prompt:

   ````py
   f"""Rank the movies listed below by relevance to the following search query.

   Query: "{query}"

   Movies:
   {doc_list_str}

   Return the movie IDs in order of relevance, best match first.

   Your response must be a raw JSON array of integers.
   Do not wrap the JSON in Markdown. Do not use a ```json code block.
   Do not include any explanatory text.

   For example:
   [75, 12, 34, 2, 1]

   Ranking:"""
   ````

4. [ ] Parse the JSON using [`json.loads()`](https://docs.python.org/3/library/json.html#json.loads) to get the ranked movie IDs.
5. [ ] Sort the results by the new rank in ascending order.
6. [ ] Print the results after truncating to the `limit`, preserving the RRF score and the new LLM rank in this format:

   ```text
   Re-ranking top 3 results using batch method...
   Reciprocal Rank Fusion Results for 'family movie about bears in the woods' (k=60):

   1. The Berenstain Bears' Christmas Tree
      Re-rank Rank: 1
      RRF Score: 0.027
      BM25 Rank: 37, Semantic Rank: 1
      It is Christmas Eve in Bear Country and the Bear Family is decorating for Christmas. Now the only th...

   2. Goldilocks and the Three Bears
      Re-rank Rank: 2
      RRF Score: 0.023
      BM25 Rank: 2, Semantic Rank: 91
      In Southey's tale, three anthropomorphic bears – "a Little, Small, Wee Bear, a Middle-sized Bear, an...

   3. The Country Bears
      Re-rank Rank: 3
      RRF Score: 0.023
      BM25 Rank: 25, Semantic Rank: 32
      Beary Barrington is a young bear who has been raised by a human family and struggles with his identi...
   ```

Once you have the new query pipeline working, **submit** the CLI tests.
