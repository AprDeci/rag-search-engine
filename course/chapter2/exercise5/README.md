# Inverse Document Frequency (IDF)

[Inverse document frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf#:~:text=%7D-,Inverse%20document%20frequency,-%5Bedit%5D) is a way of handling common words that are _specific to a given dataset_, not just generic stop words.

Consider a search query for our movie dataset:

> "A movie about an actor who becomes a coding instructor"

`actor` might be a great keyword in _some_ datasets, but tons of movie descriptions mention actors! A match on `actor` isn't very helpful for distinguishing relevant documents from irrelevant ones.

## Why Inverse Frequency?

In its basic form, document frequency (DF) measures how many documents in a dataset contain a term. The more documents a term appears in, the higher its DF. `actor` would have a _high_ DF in a dataset about movies.

So why would we use **inverse** document frequency (IDF)? Because we actually want _rare_ terms to get higher scores.

Say we have 100 documents in total:

- A common term, `bear`, appears in 95 documents; IDF ≈ **0.05** ← Low score
- A rare term, `cyborg`, appears in 2 documents; IDF ≈ **3.52** ← High score
- A _universal_ term, `movie`, appears in all 100 documents; IDF = **0** ← Zero score

If a search query mentions `movie`, a match on that term means effectively nothing. But if a query mentions `cyborg`, a matching document is far more likely to be relevant.

## The Formula

IDF is calculated as follows:

```py
math.log((total_doc_count + 1) / (term_match_doc_count + 1))
```

> [!warning]
> The `+1` values prevent division by zero when a term doesn't appear in any documents.

## Assignment

1. [ ] Add an `idf` command to your `keyword_search_cli.py` entrypoint script.
   1. [ ] Take a term as an argument.
   2. [ ] Load the index and docmap from disk using the `.load()` method you implemented earlier.
   3. [ ] Tokenize the term with your single-term helper.
   4. [ ] Calculate the IDF for the token using the formula above.
   5. [ ] Print the IDF value.
2. [ ] Format the floating-point value to 2 decimal places when printing:
   ```py
   print(f"Inverse document frequency of '{args.term}': {idf:.2f}")
   ```

**Run and submit** the CLI tests.

> [!info]
> Your IDF results will depend on the exact contents of `movies.json` and `stopwords.txt`. If your values are close but not identical to the tests, make sure you haven't changed those files.
