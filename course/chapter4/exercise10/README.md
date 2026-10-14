# Generating Text Embeddings

Let's convert some text into embeddings.

## Preprocessing

Unlike keyword search, embedding models handle many preprocessing tasks automatically:

- **Case-insensitive:** "PADDINGTON" and "paddington" get similar embeddings.
- **Punctuation-robust:** "Ted!" and "Ted" are nearly identical.
- **Context-aware:** "bear" in "teddy bear" vs. "grizzly bear" gets different vectors.

## Assignment

**Add a function to the semantic search module that generates an embedding for a single text input**, and verify that it works.

1. [ ] In `cli/lib/semantic_search.py` (or whatever you named your semantic search library module), add a `generate_embedding(self, text)` method to the `SemanticSearch` class:
   1. [ ] If the input `text` is empty or contains only whitespace, raise a `ValueError` with a helpful message.
   2. [ ] Use the model's [`encode` method](https://sbert.net/docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode) to generate an `embedding` for the input text. The `encode` method expects a _list_ of inputs, so wrap the text in a list. It returns a corresponding list of outputs, but we only care about the first element.
   3. [ ] Return the `embedding`, using index `0` of the result from `encode`.
2. [ ] Add a new top-level function to the same module: `embed_text(text)`
   1. [ ] Create an instance of the `SemanticSearch` class.
   2. [ ] Get the embedding for the input text.
   3. [ ] Print the following:
      ```py
      print(f"Text: {text}")
      print(f"First 3 dimensions: {embedding[:3]}")
      print(f"Dimensions: {embedding.shape[0]}")
      ```
3. [ ] In your CLI script, add a new `embed_text` command that accepts a single string argument. It should run your `embed_text` function with the provided text.

**Run and submit** the CLI tests.

> [!info]
> Each embedding model is trained with a specific [tokenizer](https://huggingface.co/learn/llm-course/chapter2/4). You must tokenize text the same way the model was trained, so models come packaged with their tokenizers. In other words, **the library does it for you**!
