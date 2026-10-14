# LLMs for Re-Ranking

The massive training data a good LLM goes through will typically understand some **nuance** that traditional scoring misses:

- "family-friendly" → knows "Paddington" is more relevant than "The Revenant"
- "like Paddington" → understands tone and style
- "not too scary" → can judge content appropriateness

LLMs are slow and expensive to run on large data sets, but their built-in knowledge, reasoning, and short-term memory make them great for working with a small set of full documents.

## Assignment

**Implement LLM-based re-ranking for RRF search.**

1. [ ] Add a new optional string argument `--rerank-method` to the `rrf-search` command. For now it can either be `"individual"` or not supplied at all. We'll add more options later.
2. [ ] Perform RRF search as normal, but gather **5 times as many results** as the `limit` specified _if_ the `--rerank-method` is set to `"individual"`.
3. [ ] If the `"individual"` re-rank method is provided, _after_ doing the initial RRF search, run the results through a series of LLM prompts (one per document) asking the LLM to provide a new score for each document. I used this system prompt:

   ```py
   f"""Rate how well this movie matches the search query.

   Query: "{query}"
   Movie: {doc.get("title", "")} - {doc.get("document", "")}

   Consider:
   - Direct relevance to query
   - User intent (what they're looking for)
   - Content appropriateness

   Rate 0-10 (10 = perfect match).
   Output ONLY the number in your response, no other text or explanation.

   Score:"""
   ```

4. [ ] To avoid hitting a rate limit, I recommend [`sleep`](https://docs.python.org/3/library/time.html#time.sleep)ing for 3 seconds (or longer if you're running into issues) between each LLM API call.
5. [ ] Sort the results by the new score in descending order.
6. [ ] Print the results after truncating to the `limit`, preserving the RRF score and the new LLM score in this format:

   ```text
   Re-ranking top 3 results using individual method...
   Reciprocal Rank Fusion Results for 'family movie about bears in the woods' (k=60):

   1. The Berenstain Bears' Christmas Tree
      Re-rank Score: 10.000/10
      RRF Score: 0.027
      BM25 Rank: 37, Semantic Rank: 1
      It is Christmas Eve in Bear Country and the Bear Family is decorating for Christmas. Now the only th...

   2. Goldilocks and the Three Bears
      Re-rank Score: 9.000/10
      RRF Score: 0.023
      BM25 Rank: 2, Semantic Rank: 91
      In Southey's tale, three anthropomorphic bears – "a Little, Small, Wee Bear, a Middle-sized Bear, an...

   3. The Country Bears
      Re-rank Score: 9.000/10
      RRF Score: 0.023
      BM25 Rank: 25, Semantic Rank: 32
      Beary Barrington is a young bear who has been raised by a human family and struggles with his identi...
   ```

> [!tip]  
> Free models can be inconsistent: if a model refuses, returns malformed output, or errors, just retry. Because `openrouter/free` routes to a different model on each request, a retry often succeeds. You can also pin a specific `:free` model from the [models page](https://openrouter.ai/models?max_price=0). You'll never lose armor/sharpshooter from a model failure.

**Submit** the CLI tests.
