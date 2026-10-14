# Inverted Index

An [inverted index](https://en.wikipedia.org/wiki/Inverted_index) is what makes keyword search fast. It's like a [SQL database index](https://en.wikipedia.org/wiki/Database_index), but for text. Instead of scanning every document on every search, we build a lookup table ahead of time.

> [!info]
> A "forward index" maps location → value. An "**inverted** index" maps value → location.

Here's an example mapping words to the document IDs where they appear:

- `matrix` → `[1, 5, 10]`
- `hacker` → `[1, 8]`
- `reality` → `[1, 3, 7]`

> [!isaac]
> _Using_ an inverted index is fast: each token lookup is `O(1)` on average. _Building_ the index is slower because we still have to read and tokenize every document once.

## Assignment

**Implement an `InvertedIndex` class** and use it for keyword search.

1. [ ] Create a new `InvertedIndex` class. It should have:
   1. [ ] An `index` attribute: a dictionary mapping tokens to _sets_ of document IDs.
   2. [ ] A `docmap` attribute: a dictionary mapping document IDs to their full document objects.
   3. [ ] An `__add_document(self, doc_id, text)` method. Use your existing `tokenize_text` helper on the input text, then add each token and document ID to the index.
   4. [ ] A `get_documents(self, term)` method. It should get the document IDs for a single preprocessed token and return them as a [sorted](https://docs.python.org/3/library/functions.html#sorted) list in ascending order.
   5. [ ] A `build` method. It should call `load_movies()`, then add each movie to both the index and the docmap. Use each movie's existing `id` as its document ID. When adding movie data to the index with `__add_document()`, concatenate the title and description:
      ```py
      f"{m['title']} {m['description']}"
      ```
   6. [ ] A `save` method. It should save the `index` and `docmap` attributes to disk using the [`pickle`](https://docs.python.org/3/library/pickle.html) module's [`dump` function](https://docs.python.org/3/library/pickle.html#pickle.dump).
      1. [ ] Use the file path/name `cache/index.pkl` for the index.
      2. [ ] Use the file path/name `cache/docmap.pkl` for the docmap.
      3. [ ] Create the `cache` directory if it doesn't exist before writing files into it!
2. [ ] Add a `build_command` function and wire it to a new `build` command in the `keyword_search_cli.py` entrypoint script.
   1. [ ] Build the inverted index and save it to disk.
   2. [ ] Print a message containing the first document ID for the token `'merida'`, which should be document `4651` (`"Brave"`):

      ```py
      print(f"First document for token 'merida' = {docs[0]}")
      ```

      > [!warning]
      > We'll hardcode this as a very simple test to ensure that the index is built correctly.

**Run and submit** the CLI tests.
