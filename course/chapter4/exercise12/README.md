# Query Embeddings

We need to convert user queries into vectors, just like we did with our documents. That way we can compare the query to the documents. For example, say we have these vectors in our document vector store:

- `[1,2,3]`
- `[4,5,6]`
- `[7,8,9]`

Which one is closest to the query "bear"?

... It's impossible to say without first converting "bear" into the same kind of vector. So, `"bear" –> [2, 3, 4]` (for example).

Now, what's closest to `[2, 3, 4]`? _We can use vector math to find out!_

## Preprocessing for Embeddings

Remember that embedding models handle many preprocessing tasks automatically:

- **Case-insensitive:** "FUNNY" and "funny" get similar embeddings.
- **Punctuation-robust:** "movies!" and "movies" are nearly identical.
- **Whitespace-tolerant:** Extra spaces are handled gracefully.

This means we can use minimal preprocessing for queries – just basic cleaning like stripping whitespace.

## Assignment

**Implement query embedding functionality** that converts user search queries into vectors.

1. [ ] Add a new `embed_query_text(query)` function to your library module. It should:
   1. [ ] Create an instance of the `SemanticSearch` class.
   2. [ ] Call your existing `generate_embedding` method with the provided query (this method already handles whitespace stripping and validation).
   3. [ ] Print information about the query and its embedding:
      ```py
      print(f"Query: {query}")
      print(f"First 3 dimensions: {embedding[:3]}")
      print(f"Shape: {embedding.shape}")
      ```
2. [ ] In your CLI script, add a new `embed_query` command that accepts a positional query string argument. It should call your `embed_query_text` function with the provided query.

**Run and submit** the CLI tests.
