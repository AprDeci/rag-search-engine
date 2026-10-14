# Adding Citations

A summary without sources is just **claims without evidence**. Lack of citations is one of the primary reasons users don't trust AI-generated content.

Let's add citations to our summary so users can verify and explore further. Citations matter for:

- **Trust:** Users can verify claims
- **Exploration:** Jump to full sources
- **Attribution:** Credit original content
- **Legal:** Avoid plagiarism issues

The simplest approach is to have the LLM keep track of all the sources _during_ summarization, in other words, just asking the model to include sources in its output:

> Write a summary that answers the query.
> Cite the sources I've given you using the format [1], [2], etc. when referencing them.

Expected LLM output is now:

```text
"The most intense bear attacks occur in The Revenant [1] where Hugh Glass is
mauled by a grizzly, and Backcountry [3] which depicts a true story of a camping
trip gone wrong."
```

Which we can display alongside the actual search results:

1. _The Revenant_: "Fur trapper Hugh Glass (Leonardo DiCaprio) watches as American soldiers..."
2. _Backcountry_: "Alex (Jeff Roop) and his girlfriend Jenn (Missy Peregrym) arrive at a provincial park to go camping..."

## Assignment

**Add a citation-aware answer command that references its sources.**

1. [ ] Add a new `citations` command to the `cli/augmented_generation_cli.py` script. It should accept a required `query` positional argument and an optional `--limit` argument that defaults to `5`.
2. [ ] The `citations` command should:
   1. [ ] Load the movie dataset, and use it to set up a `HybridSearch` instance.
   2. [ ] Perform an RRF search using the provided query.
   3. [ ] Prompt the LLM to answer the search query and provide a list of citations. Here's the prompt I used:

      ```py
      prompt = f"""Answer the query below and give information based on the provided documents.

      The answer should be tailored to users of Webflyx, a movie streaming service.
      If not enough information is available to provide a good answer, say so, but give the best answer possible while citing the sources available.

      Query: {query}

      Documents:
      {documents}

      Instructions:
      - Provide a comprehensive answer that addresses the query
      - Cite sources in the format [1], [2], etc. when referencing information
      - If sources disagree, mention the different viewpoints
      - If the answer isn't in the provided documents, say "I don't have enough information"
      - Be direct and informative

      Answer:"""
      ```

3. [ ] Print the search results and the answer in this format:

   ```text
   Search Results:
     - Dark Star
     - Terra
     - Eliminators
     - Destricted
     - The Octagon

   LLM Answer:
   <ANSWER WITH CITATIONS>
   ```

Once the new command is working, **submit** the CLI tests.
