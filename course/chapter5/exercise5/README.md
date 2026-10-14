# Chunked Semantic Search

Let's implement search using the embeddings we generated for document chunks. We'll search across all chunks to find the most relevant sections, then aggregate results back to the document level.

In this lesson, we'll focus on:

1. **Searching across chunks** using cosine similarity with query embeddings
2. **Aggregating chunk scores** to determine the most relevant documents
3. **Returning formatted results** that map chunks back to their original movies

> [!info]
> By searching at the chunk level, we can find relevant information even when it's buried deep within a long document, like a book or technical manual.

## Assignment

**Implement search functionality that queries chunk embeddings and aggregates results.**

1. [ ] Write a new `search_chunks(self, query: str, limit: int = 10)` method on the `ChunkedSemanticSearch` class. It should:
   1. [ ] Generate an embedding of the query (using the method from the `SemanticSearch` class).
   2. [ ] Create an empty list to store "chunk score" dictionaries.
   3. [ ] For each chunk embedding:
      1. [ ] Calculate the cosine similarity between the chunk embedding and the query embedding.
      2. [ ] Append a dictionary to the chunk score list with fields:
         - `chunk_idx`: The index of the chunk within the document
         - `movie_idx`: The index of the document in `self.documents` (you'll need to use `self.chunk_metadata` to map back to this)
         - `score`: The cosine similarity score
   4. [ ] Create an empty dictionary that maps movie indexes to their best chunk scores.
   5. [ ] For each chunk score, if the `movie_idx` is _not_ in the movie score dictionary yet, _or_ the new score is higher than the existing one, update the movie score dictionary with the new chunk score.
   6. [ ] Sort the movie scores by score in descending order.
   7. [ ] Filter down to the top `limit` movies.
   8. [ ] Build each result as a dictionary from the movie document (`self.documents[movie_idx]`), truncating the description to 100 characters:
      ```py
      {
          "id": doc["id"],
          "title": doc["title"],
          "document": doc["description"][:100],
          "score": round(score, 3),
      }
      ```
   9. [ ] Return the final list of results.
2. [ ] Add a new `search_chunked` command to your `semantic_search_cli.py` script. It should:
   1. [ ] Accept a _required_ positional argument for the search query.
   2. [ ] Accept an _optional_ `--limit` argument (defaulting to `5`) for the number of results to return.
   3. [ ] Load the movie documents using `load_movies()`.
   4. [ ] Initialize a `ChunkedSemanticSearch` instance.
   5. [ ] Load or create chunk embeddings.
   6. [ ] Get the results using the `search_chunks` method with the given `query` and `limit` arguments.
   7. [ ] Print results in the following format:
      ```py
      print(f"\n{i}. {TITLE} (score: {SCORE:.4f})")
      print(f"   {DOCUMENT}...")
      ```

**Run and submit** the CLI tests.
