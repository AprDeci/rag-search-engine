# Query Expansion

Sometimes users are **too specific**. They search for "grizzly" and miss other movies about other kinds of bears.

Query expansion adds **related terms** to the query to catch even more relevant results.

> [!isaac]  
> In my consulting work, I find that many companies overlook query expansion. They seem to think they're forced to use the user's query as-is, but there are no rules here! Expansion can be a powerful tool.

## Types of Expansion

1. Synonyms
   - "funny" → "comedy humorous amusing"
2. Broaden
   - "grizzly" → "grizzly bear animal"
3. Related
   - "family" → "family kids children animated"

> [!tip]  
> Manual (programmatic) expansion is also RAG! If you have lists of genres and subgenres in your database, you can do expansion without an LLM. Sometimes an LLM is the answer, but sometimes a simple list is all you need!

## Assignment

**Build a query expander that adds meaningful terms to the query.**

1. [ ] Add a new choice to the `--enhance` argument. Now it can be `"spell"`, `"rewrite"`, or `"expand"`.
2. [ ] If `"expand"` is provided, the RRF search command should send the query to the LLM and ask it to _expand_ the query to be more optimal for search. Here's the prompt I used, but feel free to tweak it:

   ```py
   f"""Expand the user-provided movie search query below with related terms.

   Add synonyms and related concepts that might appear in movie descriptions.
   Keep expansions relevant and focused.
   Output only the additional terms; they will be appended to the original query.

   Examples:
   - "scary bear movie" -> "scary horror grizzly bear movie terrifying film"
   - "action movie with bear" -> "action thriller bear chase fight adventure"
   - "comedy with bear" -> "comedy funny bear humor lighthearted"

   User query: "{query}"
   """
   ```

3. [ ] Again, if the query was enhanced, print it in the following format for the user to see the changes:

   ```py
   f"Enhanced query ({METHOD}): '{QUERY}' -> '{ENHANCED_QUERY}'\n"
   ```

4. [ ] Run the enhanced query using RRF search, and print the results as normal.

**Run and submit** the CLI tests.
