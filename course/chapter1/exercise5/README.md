# Text Processing

**Exact** matching, frankly, isn't particularly useful. It's rare that a user searching for "The Alien" wants us to exclude results like:

- "the alien" (different case)
- "Alien" (missing "The")
- "Aliens" (plural form)

Keyword search doesn't need to be exact; in fact, it _shouldn't_ be. To improve keyword search, we need to do some **text processing**. For example, we want `bear`, `Bear`, and `bear.` to be treated as the _same keyword_. We'll do that in a few steps.

## Text Processing Pipeline

![Text Processing](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/COmHbDR-659x647.png)

- **Case insensitivity:** Convert all text to lowercase
  - `"The Matrix"` becomes `"the matrix"`
  - `"HE IS HERE"` becomes `"he is here"`
- **Remove punctuation:** We don't care about periods, commas, etc.
  - `"Hello, world!"` becomes `"hello world"`
  - `"sci-fi"` becomes `"scifi"`
- **Tokenization:** Break text into individual words
  - `"the matrix"` becomes `["the", "matrix"]`
  - `"hello world"` becomes `["hello", "world"]`
- **Stop words:** Remove common [stop words](https://en.wikipedia.org/wiki/Stop_word) that don't add much meaning
  - `["the", "matrix"]` becomes `["matrix"]`
  - `["a", "puppy"]` becomes `["puppy"]`
- **Stemming:** Keep only the [stem](https://en.wikipedia.org/wiki/Word_stem) of words
  - `["running", "jumping"]` becomes `["run", "jump"]`
  - `["watching", "windmills"]` becomes `["watch", "windmill"]`

## Assignment

Webflyx users can't be bothered to use the _shift_ key!

**Update your matching logic** to call [`.lower()`](https://docs.python.org/3/library/stdtypes.html#str.lower) on both the search query and the movie titles before comparing them.

**Run and submit** the CLI tests.
