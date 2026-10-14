# Chunked Semantic Embeddings

Now that we can chunk documents, let's create embeddings for those chunks. This is the foundation for a more useful search system: it can find relevant _sections_ inside longer documents.

In this lesson, we'll focus on:

1. **Chunking documents** using our semantic chunking approach
2. **Creating embeddings** for each individual chunk
3. **Storing metadata** to map chunks back to their original documents

Creating embeddings for chunks instead of full documents lets us find specific relevant sections within longer texts. That's crucial for RAG systems when documents are too large, too broad, or too noisy to embed as one unit.

> [!tip]
> This is very similar to the embeddings we created for full documents, but it's a little trickier because we need to map chunks back to their original documents.

## Assignment

**Implement a system that creates embeddings for document chunks.**

1. [ ] Create a new `ChunkedSemanticSearch` class that inherits from `SemanticSearch`:
   ```py
   class ChunkedSemanticSearch(SemanticSearch):
       def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> None:
           super().__init__(model_name)
           self.chunk_embeddings = None
           self.chunk_metadata = None
   ```
2. [ ] Write a new `build_chunk_embeddings(self, documents: list[dict]) -> np.ndarray` method on the `ChunkedSemanticSearch` class. It's similar to `build_embeddings` from the `SemanticSearch` class, but it handles chunking.
   1. [ ] Populate `self.documents` and `self.document_map` from the input documents (same as before).
   2. [ ] Create an empty list of strings to hold all the chunks.
   3. [ ] Create an empty list of dictionaries to hold metadata about each chunk.
   4. [ ] For each document:
      1. [ ] If the description text is empty, skip it.
      2. [ ] Reuse the chunking function from your `semantic_chunk` command to split the description text into **chunks of `4` sentences** with **overlap of `1` sentence**. Both should call the same function.
      3. [ ] Add each chunk to the "all chunks" list.
      4. [ ] For each chunk, add a dictionary to the "chunk metadata" list with the following keys:
         - `movie_idx`: The index of the document in `self.documents`
         - `chunk_idx`: The index of the chunk within the document
         - `total_chunks`: The total number of chunks in the document
   5. [ ] Use the model to `.encode()` the entire list of all chunks, and save the results into the `self.chunk_embeddings` attribute.
   6. [ ] Save the chunk metadata into the `self.chunk_metadata` attribute.
   7. [ ] Use [`np.save`](https://numpy.org/devdocs/reference/generated/numpy.save.html#numpy.save) to save the embeddings to a `cache/chunk_embeddings.npy` file.
   8. [ ] Save the metadata as a JSON file in `cache/chunk_metadata.json` in this format:
      ```py
      json.dump({"chunks": chunk_metadata, "total_chunks": len(all_chunks)}, f, indent=2)
      ```
   9. [ ] Return the chunk embeddings list.
3. [ ] Write a new `load_or_create_chunk_embeddings(self, documents: list[dict]) -> np.ndarray` method on the `ChunkedSemanticSearch` class:
   1. [ ] Populate `self.documents` and `self.document_map` from the input documents (same as before).
   2. [ ] If the `cache/chunk_embeddings.npy` and `cache/chunk_metadata.json` files exist:
      1. [ ] Load embeddings into `self.chunk_embeddings`.
      2. [ ] Load metadata JSON and extract chunks into `self.chunk_metadata`.
      3. [ ] Return `self.chunk_embeddings`.
   3. [ ] Otherwise, return the result of rebuilding the chunk embeddings with `build_chunk_embeddings`.
4. [ ] Add a new `embed_chunks` command to your `semantic_search_cli.py` script. It should:
   1. [ ] Load the movie documents.
   2. [ ] Initialize a `ChunkedSemanticSearch` instance.
   3. [ ] Load or build the chunk embeddings.
   4. [ ] Print info about the embeddings in this format:
      ```py
      print(f"Generated {len(embeddings)} chunked embeddings")
      ```

**Run and submit** the CLI tests.

> [!info]
> Building the embeddings for the first time might take quite a while. Go make yourself a nice soy latte.

> [!warning]
> We're storing metadata about each chunk so we can later map chunks back to their original documents.

## Tip

If you want to type the chunk metadata shape explicitly, a `TypedDict` works well here:

```py
from typing import TypedDict


class ChunkMetadata(TypedDict):
    movie_idx: int
    chunk_idx: int
    total_chunks: int
```
