# Tokenization

[Tokenization](https://en.wikipedia.org/wiki/Search_engine_indexing#Tokenization) means splitting text into smaller pieces, called **tokens**. Simple **word-based tokenization** looks like this:

- **Input:** `"The Matrix is a great movie!"`
- **Output:** `["the", "matrix", "is", "a", "great", "movie"]`

Many tokenization methods exist, but we'll use word-based tokenization for keyword search. We already handled case insensitivity and punctuation removal in the previous steps.

> [!info]
> You might hear that ["tokens" in the context of LLMs](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) don't map one-to-one with words, and that's true, so don't let that trip you up here.

## Assignment

We want Webflyx users to be able to search for _partial matches_, not just exact full-query substrings. For example, the query "Great Bear" should match the title "Big Bear" because the `bear` token appears in both.

> [!tip]
> Wrap this logic in a helper function! You'll need to apply the exact same processing throughout the course.

1. [ ] Split the query and title into tokens with [`.split()`](https://docs.python.org/3/library/stdtypes.html#str.split) **without an argument** so it splits on all whitespace, not only literal spaces.
2. [ ] Update your matching logic to allow matches where _at least one_ query token appears in _any_ title token (stemming not required).

**Run and submit** the CLI tests.
