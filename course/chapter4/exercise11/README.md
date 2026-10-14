# Document Embeddings

Now that we've created an embedding for a single string, let's create embeddings for our _entire movie dataset_. This will turn our movies into a searchable vector store.

We'll save the embeddings in a [`.npy` file](https://numpy.org/devdocs/reference/generated/numpy.lib.format.html) using [`numpy.save`](https://numpy.org/devdocs/reference/generated/numpy.save.html#numpy.save). The `.npy` file will be our **vector store**.

## Assignment

Add logic to **generate embeddings** for the full movie dataset, **save them** to disk, **load them** if they already exist, and **verify** that they seem correct. This way, the slow embedding generation step only needs to happen once.

1. [ ] Add `numpy` as a dependency.
   ```sh
   uv add numpy==2.3.3
   ```
2. [ ] In `cli/lib/semantic_search.py` (or whatever you named your semantic search library module), add the import at the top of the file:
   ```py
   import numpy as np
   ```
3. [ ] In the `SemanticSearch` class, initialize a few more values:
   1. [ ] `self.embeddings` to `None`
   2. [ ] `self.documents` to `None`
   3. [ ] `self.document_map` to an empty dictionary
4. [ ] Add a new `build_embeddings(self, documents)` method. `documents` is a list of dictionaries, each representing a movie.
   1. [ ] Set `self.documents` equal to the `documents` argument.
   2. [ ] For each document, add an entry to `self.document_map` where the key is the document's `id` and the value is the document itself.
   3. [ ] Create a string representation of each document (movie) and store them all in a list. Each string should have this format: `f"{doc['title']}: {doc['description']}"`
   4. [ ] Use the model's `encode` method on the list of movie strings. Set the `show_progress_bar` argument on `encode` to `True` so you can watch the progress (it takes a while). Store the result as `self.embeddings`.
   5. [ ] Save the embeddings into `cache/movie_embeddings.npy` using [`np.save`](https://numpy.org/devdocs/reference/generated/numpy.save.html#numpy.save).
   6. [ ] Return `self.embeddings` from the method.
5. [ ] We want to build the embeddings only once, then load them from disk. Add a new `load_or_create_embeddings(self, documents)` method to the `SemanticSearch` class.
   1. [ ] Populate `self.documents` and `self.document_map` in this method as well, just like in `build_embeddings`.
   2. [ ] Check if the `cache/movie_embeddings.npy` file [`exists`](https://docs.python.org/3/library/os.path.html#os.path.exists).
      1. [ ] If it does, call [`np.load`](https://numpy.org/devdocs/reference/generated/numpy.load.html#numpy.load) to load the embeddings from that file into `self.embeddings`.
      2. [ ] Verify that the length of `self.embeddings` is equal to the length of `documents`. _If it is_, return the cached `self.embeddings`.
   3. [ ] Otherwise, return the result of rebuilding the embeddings from scratch with `self.build_embeddings(documents)`.
6. [ ] Add a new top-level `verify_embeddings` function. It should:
   1. [ ] Create an instance of `SemanticSearch`.
   2. [ ] Load the documents from `movies.json` into a list.
   3. [ ] Call `load_or_create_embeddings` with those movie documents.
   4. [ ] Print the number of documents and the shape of the embeddings:
      ```py
      print(f"Number of docs:   {len(documents)}")
      print(
          f"Embeddings shape: {embeddings.shape[0]} vectors in {embeddings.shape[1]} dimensions"
      )
      ```
7. [ ] Add a `verify_embeddings` command to your semantic search CLI script. It should simply call the `verify_embeddings` function.

**Run and submit** the CLI tests.
