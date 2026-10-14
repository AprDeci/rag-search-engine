# BM25 Search

In the last chapter we implemented TF-IDF, and in this chapter we've made the key improvements needed for BM25 search:

- More stable IDF calculation
- Term frequency saturation
- Document length normalization

Now we're ready to put it all together to implement BM25.

## BM25 Search Algorithm

The BM25 formula multiplies TF by IDF, like TF-IDF, but it uses the improved versions we've built in the last few lessons:

```py
BM25 = bm25_tf * bm25_idf
```

This gives us a score for one `document` and one `term`. To calculate the full BM25 score for a query, we sum the scores for each query term:

1. Tokenize the query.
2. Calculate the BM25 score for each query token in a given document, and sum them.
3. Do this _for every document_.
4. Sort documents by score (highest first).
5. Return the top `N` documents.

## Assignment

1. [ ] Add a new `bm25(self, doc_id, term)` method to the `InvertedIndex` class in `lib/keyword_search.py`.
   1. [ ] Use your `get_bm25_tf` and `get_bm25_idf` methods to get the score components.
   2. [ ] Return the full BM25 score, i.e. `bm25_tf * bm25_idf`.
2. [ ] Add a new `bm25_search(self, query, limit)` method to the `InvertedIndex` class.
   1. [ ] Tokenize the query.
   2. [ ] Initialize a scores dictionary to map document IDs to their total BM25 scores.
   3. [ ] For each document in the index, calculate the total BM25 score:
      1. [ ] For each query token, add its BM25 score to the document's running total.
      2. [ ] Store the total score in the scores dictionary.
   4. [ ] Sort the documents by score in descending order.
   5. [ ] Return the top `limit` documents along with their scores.
3. [ ] Add a `bm25search` command to your CLI in `keyword_search_cli.py`. It should accept, at minimum, a query as a positional argument. You may also like to add an optional `--limit` argument (defaulting to `5`).
   ```py
   bm25search_parser = subparsers.add_parser(
       "bm25search", help="Search movies using full BM25 scoring"
   )
   bm25search_parser.add_argument("query", type=str, help="Search query")
   ```
4. [ ] The command should use the `InvertedIndex` to load the movie data and perform the BM25 search.
5. [ ] Print the results in this format:

   ```text
   1. (15) The Adventures of Mowgli - Score: 7.79
   2. (11342) Gakuen Alice - Score: 7.42
   3. (30) Day of the Animals - Score: 7.21
   4. (5542) Candy - Score: 7.07
   5. (3395) Life of Pi - Score: 7.05
   ```

   _The number in parentheses is the document ID._

**Run and submit** the CLI tests.

## Tips

If `animated family` scores `7.14` and `6.91`, lowercase the stop words and remove their punctuation, then rebuild the index.
