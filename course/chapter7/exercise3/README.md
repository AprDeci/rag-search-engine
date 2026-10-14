# Spell Correction

Typos can _kill_ search results. "Padington" ranks extremely low in keyword search, even though the user clearly wanted "Paddington."

**Let's fix the user's spelling for them with AI before we run the search.**

## LLMs Are Good at Spelling

"Old-school" spell-checkers are often based on dictionaries and simple if/then rules. They can catch common typos, but they have a big limitation: they lack _context awareness_. For example, the word "read" is a typo in this sentence:

> That's a bright read carpet.

But it's correct in this one:

> I love to read books.

Luckily, a decent LLM will catch these kinds of errors.

> [!isaac]  
> While "prompt engineering" is a bit of a meme, there really are some useful tips for writing better prompts. Read through Anthropic's [prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) to understand what kinds of detail can be helpful in a prompt.

## Assignment

**Add spelling correction to improve queries before running hybrid search.**

1. [ ] Add query enhancement support to your `rrf-search` CLI command in `hybrid_search_cli.py`. The command should take an optional string `--enhance` argument. For now, it can either be `"spell"` or not supplied at all (we'll add other options later). You can define specific choices like this:

   ```py
   rrf_parser.add_argument(
       "--enhance",
       type=str,
       choices=["spell"],
       help="Query enhancement method",
   )
   ```

2. [ ] If `"spell"` isn't supplied, run RRF search as normal. If the option _is_ set, provide the query to the LLM, and ask it to return the query with corrected spelling. Here's the prompt I used, consisting of instructions to the model with the query injected at the end. Feel free to adjust this to your liking:

   ```py
   f"""Fix any spelling errors in the user-provided movie search query below.
   Correct only clear, high-confidence typos. Do not rewrite, add, remove, or reorder words.
   Preserve punctuation and capitalization unless a change is required for a typo fix.
   If there are no spelling errors, or if you're unsure, output the original query unchanged.
   Output only the final query text, nothing else.
   User query: "{query}"
   """
   ```

3. [ ] If the query was enhanced, print it in the following format for the user to see the changes:

   ```py
   f"Enhanced query ({METHOD}): '{QUERY}' -> '{ENHANCED_QUERY}'\n"
   ```

   Where:
   - `METHOD` is the enhancement method (e.g. `"spell"`)
   - `QUERY` is the original query
   - `ENHANCED_QUERY` is the enhanced query returned by the LLM

4. [ ] Run the enhanced query using RRF search, and print the results as normal.

**Run and submit** the CLI tests.
