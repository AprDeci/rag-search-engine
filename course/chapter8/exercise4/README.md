# Cross-Encoder Re-Ranking

A second approach to re-ranking is to use a [cross-encoder](https://sbert.net/examples/cross_encoder/applications/README.html). Our semantic search embeddings were created with a **bi-encoder**, which embeds queries and documents separately so that we can use cosine similarity to get a relevance score.

A **cross-encoder** does the same thing, but embeds the query and document as a single input to produce a relevance score directly. The output _is_ the score – no need to compute cosine similarity.

Cross-encoders see the full context of how the query and document interact, so they can catch subtle relationships that bi-encoders miss.

## Re-Ranking Speed

One big advantage of cross-encoders is that they are _much_ faster and cheaper than LLMs, as they do not require the same level of computational resources. Instead of using a tool with all the capabilities of an LLM, this type of re-ranker can only do one thing: take in a query and document pair and output a relevance score.

In other words, it's a regression model.

## Fine-Tuning Cross-Encoders

The second major advantage of cross-encoders is that they can be [fine-tuned](https://www.ibm.com/think/topics/fine-tuning) on your specific domain relatively easily. You can train them on your own query-document pairs to learn the exact relevance patterns for your use case, and they are cheaper and faster than LLMs.

We won't be doing any fine-tuning in this course, but it's good to know about!

> [!isaac]  
> A fast way to get up and running with a re-ranker is to use the [Cohere API](https://docs.cohere.com/reference/about) or one of its competitors. Typically these APIs use cross-encoders.

## Assignment

**Implement a cross-encoder re-ranker for RRF search.**

1. [ ] Add a new option to the `--rerank-method` argument. Now it can be `"individual"`, `"batch"`, or `"cross_encoder"`.
2. [ ] Again, gather **5 times as many results** as the `limit` specified _if_ a `--rerank-method` is set.
3. [ ] If the `"cross_encoder"` re-rank method is provided, _after_ doing the initial RRF search:
   - [ ] Create a new list of "pairs" lists, where the first element is the query, and the second element is the document, in this stringified format:

     ```py
     pairs.append([query, f"{doc.get('title', '')} - {doc.get('document', '')}"])
     ```

   - [ ] From the same [`sentence_transformers`](https://www.sbert.net) library as before, import the [`CrossEncoder`](https://sbert.net/docs/package_reference/cross_encoder/cross_encoder.html) class.
   - [ ] Create a new `CrossEncoder` instance (just do this once per query, not for each document) using the `cross-encoder/ms-marco-TinyBERT-L2-v2` model.

     ```py
     cross_encoder = CrossEncoder("cross-encoder/ms-marco-TinyBERT-L2-v2")
     ```

     > [!tip]
     > If you get an error about your GPU or hardware acceleration, load the cross-encoder on your CPU instead by passing `device="cpu"`.

   - [ ] Use the `CrossEncoder` to compute scores for all the pairs:

     ```py
     # `predict` returns a list of numbers, one for each pair
     scores = cross_encoder.predict(pairs)
     ```

4. [ ] Sort the results by the new score in descending order.
5. [ ] Print the results after truncating to the `limit`, preserving the RRF score and the new cross-encoder score in this format:

   ```text
   Re-ranking top 25 results using cross_encoder method...
   Reciprocal Rank Fusion Results for 'family movie about bears in the woods' (k=60):

   1. Care Bears Movie II: A New Generation
      Cross Encoder Score: 3.314
      RRF Score: 0.028
      BM25 Rank: 1, Semantic Rank: 26
      Aboard their boat, a yellow bear and a purple horse look after the baby animals known as the Care Be...

   2. A Bear for Punishment
      Cross Encoder Score: -1.001
      RRF Score: 0.020
      BM25 Rank: 41, Semantic Rank: 35
      The film begins with the bear family sleeping peacefully at home, when suddenly, the alarms of dozen...

   3. The Country Bears
      Cross Encoder Score: -1.276
      RRF Score: 0.023
      BM25 Rank: 25, Semantic Rank: 32
      Beary Barrington is a young bear who has been raised by a human family and struggles with his identi...
   ```

**Submit** the CLI tests.
