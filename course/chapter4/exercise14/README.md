# Implementing Semantic Search

Now we'll combine everything we've learned to build a complete semantic search engine. It will find movies based on _meaning_ rather than exact keyword matches. Our semantic search system has five main steps:

1. **Embed documents** (done once) – Convert movies to vectors.
2. **Store documents** (done once) – Store embedded documents in a vector store.
3. **Embed query** (per search) – Convert the user query to a vector.
4. **Calculate similarities** – Compare the query vector to all movie vectors.
5. **Rank and return** – Sort by similarity and return the top results.

## Cosine Similarity

For semantic search, we use cosine similarity to compare vectors. It measures the angle between two vectors and gives us a score from `-1.0` to `1.0`:

- **`1.0`:** Vectors point in the same direction (identical meaning)
- **`0.0`:** Vectors are perpendicular (unrelated)
- **`-1.0`:** Vectors point in opposite directions (opposite meaning)

## Assignment

**Build a complete semantic search system** that finds movies by meaning. You'll combine all the pieces you've built in previous lessons.

1. [ ] Add a `cosine_similarity(vec1, vec2)` function to your semantic search library module, _outside_ the class. You implemented this algorithm from scratch earlier in the chapter, but in practice you'll usually use an optimized version written in a fast language like C. The [NumPy library](https://numpy.org/) gives us convenient Python APIs for these fast vector operations. Copy-paste the following code into your module:

   ```py
   import numpy as np


   def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
       dot_product = np.dot(vec1, vec2)
       norm1 = np.linalg.norm(vec1)
       norm2 = np.linalg.norm(vec2)

       if norm1 == 0 or norm2 == 0:
           return 0.0

       return dot_product / (norm1 * norm2)
   ```

2. [ ] Add a `search(self, query, limit)` method to the `SemanticSearch` class.
   1. [ ] Check if embeddings are loaded. If not, raise a `ValueError` with this message:
      ```text
      "No embeddings loaded. Call `load_or_create_embeddings` first."
      ```
   2. [ ] Generate an embedding for the query using `self.generate_embedding(query)`.
   3. [ ] Calculate cosine similarity between the query embedding and each document embedding.
   4. [ ] Create a list of `(similarity_score, document)` tuples.
   5. [ ] Sort the list by similarity score in descending order.
   6. [ ] Return the top results (up to `limit`) as a list of dictionaries, each containing:
      - `score`: The cosine similarity score
      - `title`: The movie title
      - `description`: The movie description
3. [ ] In your semantic search CLI script, add a new `search` command. It should:
   1. [ ] Accept a required positional string argument, the query.
   2. [ ] Accept an optional `--limit` argument (default `5`).
   3. [ ] Create a `SemanticSearch` instance.
   4. [ ] Load movies and load/create embeddings.
   5. [ ] Call the `search` method with the query and limit.
   6. [ ] Print the results in this format:

      ```text
      1. Spaceflight IC-1: An Adventure in Space (score: 0.4406)
        The opening narrative is given by a man in a high ranking military uniform. He tells us the film is ...

      2. Adventureland (score: 0.4150)
        In 1987, James Brennan (Jesse Eisenberg) has two plans. The first plan is to have a summer vacation ...

      3. Odyssey 5 (score: 0.4038)
        The story follows six people on a routine flight of the space shuttle Odyssey, on August 7, 2007: fo...
      ```

**Run and submit** the CLI tests.
