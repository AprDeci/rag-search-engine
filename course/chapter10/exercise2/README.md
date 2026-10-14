# LLM Summarization

So what exactly does augmented generation... generate? Oftentimes it's **summaries of the results**. (You've probably seen this with Google's "AI overview" at the top of search results!)

What makes a _good_ summary depends on your users' needs. For example, a movie summary for a parent looking for family content should ideally emphasize themes and age-appropriateness, while a summary of the same movie for a film critic should focus on artistic merit and technical achievements.

_Who your target user is_ will influence what a _good_ summary looks like.

## Multi-Document Summarization

A single document tells one version of a story. **Multiple documents can give more points of view.**

When users search, they get many results:

- Some documents have parts of the needed information.
- Some documents have _wrong_ or _conflicting_ information.
- Documents have different (sometimes biased) perspectives on the information.

LLMs usually do a good job of **synthesizing** all this into one coherent answer. For example:

**Query:** "bear movies for kids"

**Search Results:**

1. _Paddington_ – Polite bear, marmalade, family-friendly
2. _Brother Bear_ – Animated Disney, transformation story
3. _The Jungle Book_ – Baloo the bear, musical numbers
4. _We Bare Bears_ – TV series, modern setting

**Summary:**

> "For family-friendly bear movies, _Paddington_ offers a polite British bear perfect for young children, while Disney's _Brother Bear_ provides beautiful animation with meaningful life lessons. _The Jungle Book_ features the lovable Baloo with catchy songs, and _We Bare Bears_ brings bears into a modern cartoon series format. All are rated G or PG with positive messages."

## Assignment

**Build a multi-document summarization pipeline that synthesizes search results.**

1. [ ] Add a new `summarize` command to the `cli/augmented_generation_cli.py` script. It should accept a required `query` positional argument and an optional `--limit` argument that defaults to `5`.
2. [ ] The `summarize` command should:
   1. [ ] Load the movie dataset, and use it to set up a `HybridSearch` instance.
   2. [ ] Perform an RRF search using the provided query.
   3. [ ] Prompt the LLM to summarize the search results. Here's the prompt I used:

      ```py
      f"""Provide information useful to the query below by synthesizing data from multiple search results in detail.

      The goal is to provide comprehensive information so that users know what their options are.
      Your response should be information-dense and concise, with several key pieces of information about the genre, plot, etc. of each movie.

      This should be tailored to Webflyx users. Webflyx is a movie streaming service.

      Query: {query}

      Search results:
      {results}

      Provide a comprehensive 3–4 sentence answer that combines information from multiple sources:"""
      ```

3. [ ] Print the search results and the summary in this format:

   ```text
   Search Results:
     - We're Back! A Dinosaur's Story
     - The Lost World
     - The Lost World: Jurassic Park
     - Dino Crisis 2
     - Land of the Lost

   LLM Summary:
   <SUMMARY GOES HERE>
   ```

If things look right, **submit** the CLI tests.
