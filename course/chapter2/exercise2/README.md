# Use the Index

Now that we've built the index and saved it to disk, we can _use_ it for fast document lookup.

As long as the movie data doesn't change, we don't need to rebuild the index before every search.

## Assignment

1. [ ] Delete the hardcoded "merida" search test from your build command.
2. [ ] Add a `load()` method to your `InvertedIndex` class. It should load the index and docmap from disk using the [`pickle`](https://docs.python.org/3/library/pickle.html) module's [`load` function](https://docs.python.org/3/library/pickle.html#pickle.load).
   - [ ] Use `cache/index.pkl` for the index
   - [ ] Use `cache/docmap.pkl` for the docmap
   - [ ] It should raise an error if the files don't exist.
3. [ ] Update your search command to load the index from disk. If it doesn't exist, print an error message and exit.
4. [ ] Remove the logic that loops through every query and every movie.
5. [ ] Instead, iterate over each token in the query and **use the inverted index** to get matching documents.
   - [ ] Stop searching once you have 5 results.
   - [ ] Print the resulting document titles and IDs.

**Run and submit** the CLI tests.
