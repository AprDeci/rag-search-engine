# Chunk Overlap

Fixed-size chunking is simple, sure, but it runs the risk of breaking up important context. For example, this document:

> In the climactic scene, the bear attack was terrifying. The stunning and innovative special effects led to record-breaking sales.

could be chunked like this:

- `In the climactic scene, the bear attack was`
- `terrifying. The stunning and innovative special effects led` (What was terrifying? What did special effects lead to?)
- `to record-breaking sales.` (What had record-breaking sales?)

**Chunk overlap** solves this by creating chunks that share words to preserve context across boundaries. For example, we could chunk like this instead:

- `In the climactic scene, the bear attack was`
- `bear attack was terrifying. The stunning and innovative special effects` (The bear attack was terrifying.)
- `special effects led to record-breaking sales` (The special effects led to record-breaking sales.)

So how do you know how aggressive your overlap _should_ be? There's no one-size-fits-all answer, so make it configurable and test it on your data!

> [!isaac]
> Okay, I know I said to test it on your data (and you should!), but a good rule of thumb for many use cases is about _20% overlap_.

## Assignment

**Add an `--overlap` parameter to the `chunk` command in `semantic_search_cli.py`.**

1. [ ] When `overlap` is greater than zero, each previous chunk should share the last `overlap` words with the following chunk.
2. [ ] Print the chunks in the same format as before.
3. [ ] Take a look at the CLI test cases to make sure your overlap works as we expect!

**Run and submit** the CLI tests.

## Tips

- I wrote a `while` loop with a custom condition rather than a `for` loop to handle the overlap.
- I also used [list slicing](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) and the [`.join()` method](https://docs.python.org/3.3/library/stdtypes.html#str.join) to create the chunks.
