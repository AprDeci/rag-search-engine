# TF-IDF

![TF-IDF](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/tf-idf-1920x1080.mp4)

[TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) combines term frequency and inverse document frequency into one relevance score.

1. **TF (term frequency):** How often a term appears in a document
2. **IDF (inverse document frequency):** How rare a term is across all documents

The formula is simple:

```text
TF-IDF = TF * IDF
```

- **Frequent** words get high TF scores.
- **Rare** words get high IDF scores.
- The **best matches** have both high TF _and_ high IDF.

## Example

Suppose we search a movie dataset for `cyborg bear` and score the following documents.

**Document 1:** "The Terminator – A cyborg from the future"

- `cyborg`: TF = 1, IDF = 3.9 → TF-IDF = 1 × 3.9 = 3.9
- `bear`: TF = 0, IDF = 0.05 → TF-IDF = 0 × 0.05 = 0
- Total score: 3.9

**Document 2:** "Ted – A talking bear who loves honey and bear friends"

- `cyborg`: TF = 0, IDF = 3.9 → TF-IDF = 0 × 3.9 = 0
- `bear`: TF = 2, IDF = 0.05 → TF-IDF = 2 × 0.05 = 0.1
- Total score: 0.1

**Document 3:** "Cyborg Bear – A robotic bear saves the city"

- `cyborg`: TF = 1, IDF = 3.9 → TF-IDF = 1 × 3.9 = 3.9
- `bear`: TF = 2, IDF = 0.05 → TF-IDF = 2 × 0.05 = 0.1
- Total score: 4.0

**Final Rankings:**

1. Document 3 ("Cyborg Bear") - 4.0 - has both terms.
2. Document 1 ("The Terminator") - 3.9 - has the rare `cyborg` term.
3. Document 2 ("Ted") - 0.1 - has only the common `bear` term.

The movie that's actually about a cyborg bear ranks highest, and `cyborg` matters more than `bear` in a dataset where `bear` is common.

## Assignment

1. [ ] Add a `tfidf` command to your `keyword_search_cli.py` entrypoint script:
   1. [ ] Take a document ID and term as arguments.
   2. [ ] Load the index and docmap from disk using the `.load()` method you implemented previously.
   3. [ ] Calculate the TF-IDF score for the given document and term.
   4. [ ] Print the TF-IDF value.
2. [ ] Format the floating-point value to 2 decimal places when printing:
   ```py
   print(f"TF-IDF score of '{args.term}' in document '{args.doc_id}': {tf_idf:.2f}")
   ```

**Run and submit** the CLI tests.
