# Semantic Chunking

Word-based chunking with overlap helps preserve context, but it still splits text at _arbitrary word boundaries_. For example:

- "Ted explores themes of friendship"
- "of friendship and growing up"
- "growing up while John must"
- "John must choose between his"

Notice how "Ted explores themes" gets separated from "of friendship and growing up"? The chunks don't follow the author's intended meaning.

**Semantic chunking** respects natural language structure like sentences and paragraphs. Each chunk contains **complete thoughts** as the author organized them. Instead of splitting at random words, we split at natural breaks like sentences or paragraphs.

- "Ted is a 2012 comedy film directed by Seth MacFarlane."
- "The story follows John Bennett and his magical teddy bear."
- "The film explores themes of friendship and growing up."

> [!isaac]
> You can still use overlap with semantic chunking. This preserves both _meaning_ and _context continuity_.

## Assignment

**Implement semantic chunking** that splits text on sentence boundaries to preserve meaning.

1. [ ] Add a new `semantic_chunk` command to your `semantic_search_cli.py` script. It should accept:
   - [ ] A required positional argument for the text to chunk
   - [ ] An optional `--max-chunk-size` argument (defaulting to `4`)
   - [ ] An optional `--overlap` argument (defaulting to `0`)
2. [ ] The command should:
   1. [ ] Split the input into individual sentences with a regular expression. The [`re.split()` function](https://docs.python.org/3/library/re.html#re.split) and the following nasty regex should help: `r"(?<=[.!?])\s+"`
   2. [ ] Produce chunks that contain up to `max_chunk_size` _sentences_.
   3. [ ] Support `overlap` by _number of sentences_.
   4. [ ] Return a list of chunk strings.
3. [ ] Print semantic chunk information in the following format:
   ```text
   Semantically chunking 85 characters
   1. First sentence here. Second sentence here.
   2. Second sentence here. Third sentence here.
   3. Third sentence here. Fourth sentence here.
   ```

**Run and submit** the CLI tests.
