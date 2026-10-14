# Query Rewriting

Users often describe what they want in **messy, informal ways**. Let's transform their intent into better search queries. For example, users might type:

- "that bear movie where leo gets attacked"
- "movie about bear in london with marmalade"
- "scary movie with bear from few years ago"

But what search engines need to perform well are **specific, concise queries**. For example:

- "The Revenant Leonardo DiCaprio bear attack"
- "Paddington London marmalade"
- "bear horror movie 2015-2020"

LLMs have _approximate knowledge of many things_... so the better models are pretty good at transforming vague user input into more specific, searchable terms.

## Assignment

**Build a query rewriter that handles vague user input.**

1. [ ] Add a new string choice to the `--enhance` argument, so it can be either `"spell"` or `"rewrite"`.
2. [ ] If `"rewrite"` is provided, the RRF search command should send the query to the LLM and ask it to _rewrite_ the query to be more optimal for search. Here's the prompt I constructed, but feel free to tweak it:

   ```py
   f"""Rewrite the user-provided movie search query below to be more specific and searchable.

   Consider:
   - Common movie knowledge (famous actors, popular films)
   - Genre conventions (horror = scary, animation = cartoon)
   - Keep the rewritten query concise (under 10 words)
   - It should be a Google-style search query, specific enough to yield relevant results
   - Don't use boolean logic

   Examples:
   - "that bear movie where leo gets attacked" -> "The Revenant Leonardo DiCaprio bear attack"
   - "movie about bear in london with marmalade" -> "Paddington London marmalade"
   - "scary movie with bear from few years ago" -> "bear horror movie 2015-2020"

   If you cannot improve the query, output the original unchanged.
   Output only the rewritten query text, nothing else.

   User query: "{query}"
   """
   ```

3. [ ] Again, if the query was enhanced, print it in this format for the user to see the changes:

   ```py
   f"Enhanced query ({METHOD}): '{QUERY}' -> '{ENHANCED_QUERY}'\n"
   ```

4. [ ] Run the enhanced query using RRF search, and print the results as normal.

**Run and submit** the CLI tests.
