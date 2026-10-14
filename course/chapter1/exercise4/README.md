# Keyword Search

Before we get deep into the advanced techniques of RAG, let's start with more "basic" search. That way, we can understand the benefits of the features we'll build on top of it. _Keyword search_ is exactly what it sounds like: we check whether the user's search terms exist in our dataset and return matching results.

Many modern search systems, including RAG systems, use keyword search as a foundational component. It's fast, simple, and effective for many use cases.

The more technical and precise the terminology is in a given domain, the more powerful keyword search becomes! For example:

**Medical Search – Precision Desired**

- **Query:** "COVID-19"
- **Keyword search:** ✅ Finds documents specifically about COVID-19
- **Semantic-only search:** ❌ Finds less-related content about "respiratory viruses" or "pandemic diseases"

**Movie Search – Generalization Desired**

- **Query:** "Alien movie"
- **Keyword search:** ❗Only finds "Alien"
- **Semantic-only search:** ✅ Finds similar movies like "Invaders from Mars," "E.T.," or "Alien"

## Assignment

Let's make our `search` command _actually work_!

> [!isaac]
> I'm not going to be overly prescriptive about your file and directory structure. I'll describe the expected behavior. If you'd like to follow my structure, check the solutions after each step.

1. [ ] Load the `data/movies.json` file into a Python dictionary using the [`json.load`](https://docs.python.org/3/library/json.html#json.load) function.
2. [ ] Iterate over all the movies in the list stored under the `movies` key and check their `title` field. If the title contains the search query, append the movie to a results list.
3. [ ] Print the results in this format:
   ```text
   Searching for: QUERY
   1. Movie Title 1
   2. Movie Title 2
   3. Movie Title 3
   ...
   ```
4. [ ] Truncate the list to a maximum of 5 results ordered by ascending ID (which the dataset already is).

> [!warning]
> Notice that this search is case-sensitive and matches only exact substrings. Don't worry, we'll improve it soon enough!

**Run and submit** the CLI tests.
