# Chunked Edge Cases

Chunking seems straightforward until you, you know, _implement it on real data_. Human writing has seemingly **infinite edge cases**. The way to get reliable chunks is to create them and **manually inspect the results**. _A lot_.

Real documents are messy, for example:

- **Tables:** Text gets jumbled when extracted from spreadsheets or PDFs.
- **Multi-page paragraphs:** A paragraph chunk-splitter can still create massive chunks.
- **Headers/footers:** The same boilerplate text appears in every chunk.
- **Images:** Alt text or captions get mixed into unrelated content.

With PDFs, you might run into problems like these:

- **Column layouts:** Text from different columns gets merged incorrectly.
- **Weird spacing:** "The&nbsp;&nbsp;movie&nbsp;&nbsp;&nbsp;&nbsp;Ted&nbsp;&nbsp;&nbsp;&nbsp;is&nbsp;&nbsp;&nbsp;&nbsp;great"
- **Missing line breaks:** Sentences run together without spaces.
- **Font artifacts:** Special characters appear as random symbols.

With rich text formats like Markdown and HTML, you might see:

- **Code blocks:** Programming examples break semantic boundaries.
- **Lists:** Bullet points that are split across chunks lose context.
- **Quotes:** Long quotations get separated from their attribution.
- **References:** Citations appear without the content they reference.

## Example of Chunking Failure

Say we have this movie review:

```text
Movie Review: Ted                    Page 1 of 3

Ted is a 2012 comedy film that follows John Bennett's relationship with his talking teddy bear.

Plot Summary                         Special Effects
The film explores themes of          The CGI work that brought
friendship and responsibility.       Ted to life was groundbreaking.

Rating: 4/5 stars                   © 2023 Movie Reviews Inc.
```

A poor chunking algorithm might produce chunks like these:

- Chunk 1: `"Movie Review: Ted Page 1 of 3 Ted is a"`
- Chunk 2: `"2012 comedy film that follows John Bennett's Plot Summary"`
- Chunk 3: `"The film explores themes of The CGI work that"`

The chunks are _completely broken_ due to PDF layout issues. The best approach to identifying the issues with _your_ data is:

- **Manually review** chunks from different document types
- **Manually review more** chunks from different document types
- **Manually review even more** chunks from different document types
- ... you get the idea

## Assignment

We have a few edge cases that are making our semantic chunking... less than ideal. **Make the following improvements** to the chunking function shared by your `semantic_chunk` command and `build_chunk_embeddings`:

1. [ ] [Strip](https://docs.python.org/3/library/stdtypes.html#str.strip) leading and trailing whitespace from the input text before using the regex to split sentences.
2. [ ] If there's nothing left after stripping, return an empty list.
3. [ ] After splitting sentences, if there's only one sentence _and_ it doesn't [end with](https://docs.python.org/3/library/stdtypes.html#str.endswith) a punctuation mark like `.`, `!`, or `?`, keep the whole text as one sentence.
4. [ ] [Strip](https://docs.python.org/3/library/stdtypes.html#str.strip) leading and trailing whitespace from each sentence before appending it to the chunk list.
5. [ ] Only use chunks that still have content after the stripping.
6. [ ] Test your improvements using the `semantic_chunk` command with edge cases like:
   - `"   Leading and trailing spaces.   "`
   - `"Text without punctuation"`
   - `"   "` (only whitespace)
   - `""` (empty string)

   > [!warning]
   > This list of edge cases is _far_ from exhaustive, but it's a good start!

When you're confident in your improvements, **run and submit** the CLI tests.

> [!danger]
> You'll need to manually delete the embeddings from your cache directory when you make changes, so that they'll be regenerated on the next run.
