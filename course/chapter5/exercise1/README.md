# Chunking

We've embedded entire movie descriptions as single units. But what happens when the documents we want to search are much longer? This is where **chunking** becomes essential for effective semantic search.

Short descriptions work just fine:

> Ted: John Bennett's childhood wish brings his teddy bear to life.

Things get complicated when we have long documents, like a full review:

> Ted is a 2012 comedy film that follows John Bennett, played by Mark Wahlberg,
> whose childhood wish magically brings his teddy bear Ted to life. The film
> explores themes of friendship, growing up, and responsibility as John struggles
> to balance his relationship with Ted and his girlfriend Lori.
>
> The movie opens with young John making a wish on a shooting star, and through
> some unexplained magic, Ted comes to life. Fast forward 27 years, and John
> is now an adult who still lives with his talking teddy bear. The film's humor
> comes largely from the contrast between Ted's cute appearance and his crude,
> adult behavior.
>
> Seth MacFarlane, creator of Family Guy, both voices Ted and directs the film.
> The movie was a commercial success, grossing over $549 million worldwide
> against a $50 million budget. A sequel, Ted 2, was released in 2015.
> The film's special effects, particularly the CGI used to bring Ted to life,
> were praised by critics...

If we keep this entire document in a single "chunk," we run into several problems:

- **Semantic dilution:** The embedding tries to capture every topic at once
- **Token limits:** Models have a limit to what they can fit in one embedding effectively
- **Poor precision:** Specific concepts get "averaged out"
- **Irrelevant matches:** Parts of the document may match queries poorly

**Chunking** solves these problems by splitting long documents into smaller pieces. For example, maybe we could break up the review document paragraph by paragraph.

Then a question about "Ted movie money" might only match the _last_ paragraph, where the review actually talks about box office performance.

## Fixed-Size Chunking

The simplest chunking approach splits text into fixed-size pieces based on character count, word count, or token count. The advantages of this naïve approach are:

1. **Predictable size:** All chunks are roughly the same length
2. **Simple implementation:** Easy to understand and implement
3. **Fast runtime performance:** Fast chunking with minimal computation
4. **Token control:** Can ensure chunks fit model limits

## Assignment

**Implement fixed-size chunking** to split long text into smaller pieces for embedding.

1. [ ] Add a `chunk` command to the `semantic_search_cli.py` CLI script:
   1. [ ] It should accept a required positional argument for the text to chunk.
   2. [ ] It should also accept an optional `--chunk-size` argument (defaulting to `200`).
2. [ ] The command should:
   1. [ ] [Split](https://docs.python.org/3/library/stdtypes.html#str.split) the text into words, on whitespace.
   2. [ ] Create chunks by grouping `n` words together into a single string, where `n` is the "chunk size" parameter.
3. [ ] Print the results in the following format, showing the total number of characters and the content of each chunk:
   ```text
   Chunking 70 characters
   1. This is a test text
   2. with more than ten words
   3. to see how chunking works
   ```

**Run and submit** the CLI tests.
