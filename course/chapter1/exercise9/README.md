# Stemming

Now that we have a list of tokens, we need to reduce related word forms to a shared _base form_. This helps match different variations of the same word.

## Examples of Word Variations

- running, runs → **run**
- jumping, jumps, jumped → **jump**
- watching, watches, watched → **watch**

![Stemming](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/GkOXqHw-821x727.png)

These variations are normalized to their **stem**, a simplified form used for matching. The process is called [stemming](https://en.wikipedia.org/wiki/Stemming).

## Why Stem Words?

Our goal is to match words from the user's input to words in our dataset. If we don't stem words, we can miss valid results. Here's an example:

User query: **"running"**

- **A River Runs Through It:** Not returned – no exact match for "running"
- **Run Baby Run:** Not returned – no exact match for "running"

**Ugh!** Both contain the concept, but in different forms that don't quite match the query.

## Assignment

Implementing stemming from scratch is a lot of work, so we'll use the [`nltk.stem`](https://www.nltk.org/api/nltk.stem.html) library to handle it for us.

1. [ ] Install the `nltk` library:
   ```sh
   uv add nltk==3.9.1
   ```
2. [ ] Import the [`PorterStemmer`](https://www.nltk.org/api/nltk.stem.porter.html#nltk.stem.porter.PorterStemmer) class from `nltk.stem`:
   ```py
   from nltk.stem import PorterStemmer
   ```
3. [ ] Create an instance of `PorterStemmer`:
   ```py
   stemmer = PorterStemmer()
   ```
4. [ ] After removing stop words from the tokens, reduce each token to its stem before matching. Use [`stemmer.stem(token)`](https://www.nltk.org/api/nltk.stem.porter.html#nltk.stem.porter.PorterStemmer.stem) to get the stemmed form of each token.

**Run and submit** the CLI tests.
