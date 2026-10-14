# Term Frequency

Now that we can find documents that contain our search terms, let's measure how _often_ each term appears.

[Term frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf#:~:text=Term%20frequency%5Bedit%5D) (TF) measures how often a word occurs in a document. For example:

> Boots teaches **students** programming while enjoying his _salmon_ for lunch. The **students** gather round as they learn debugging techniques, and all **students** leave with new coding skills.

**Term frequencies:**

- `students` appears 3 times
- `salmon` appears 1 time

This is a signal that `students` is probably more important than `salmon` in this document.

> [!isaac]
> Early internet search engines (pre-Google) used term frequency heavily. Sites could game the rankings by repeating keywords over and over: [keyword stuffing](https://en.wikipedia.org/wiki/Keyword_stuffing). Modern search engines use more advanced signals.

## Assignment

1. [ ] Add a new `term_frequencies` attribute to your `InvertedIndex` class. It should be a dictionary mapping document IDs to [`Counter` objects](https://docs.python.org/3/library/collections.html#collections.Counter). A `Counter` is a dictionary optimized for counting.
2. [ ] Update your `load` and `save` methods to also load and save this new attribute into a new `cache/term_frequencies.pkl` file.
3. [ ] Update your `__add_document` method to update the term frequencies for each token in the document. For each token, increment its count in the `Counter` for that document ID.
4. [ ] Add a new `get_tf(self, doc_id, term)` method. It should return how many times the token appears in the document with the given ID. If the term _doesn't_ appear in that document, return `0`. _Assume `term` is a single token._
5. [ ] Add a new helper function that tokenizes a single term.
   1. [ ] Use your existing tokenizer to tokenize the term.
   2. [ ] If the tokenizer doesn't return exactly one token, raise an exception.
   3. [ ] Return the single token.
6. [ ] Add a new `tf` command to the `keyword_search_cli.py` entrypoint script.
   1. [ ] It should take a document ID and a term as arguments.
   2. [ ] It should tokenize the term (using the new helper function) before looking up the term frequency.
   3. [ ] It should print the term frequency for that term in the document with the given ID.
   4. [ ] If the term doesn't exist in that document, it should just print `0`.
7. [ ] Rerun `uv run cli/keyword_search_cli.py build` to store the term frequencies.

**Run and submit** the CLI tests.
