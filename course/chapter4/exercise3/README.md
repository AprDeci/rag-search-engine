# Embedding Models

Training a model to convert text into vectors takes a lot of data and computation. The model slurps up a _massive_ amount of text and learns patterns about how words and phrases relate to each other.

For our purposes, there isn't much to gain by training our own model from scratch. We'll use a **pre-trained embedding model** called [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) because it:

- **Runs fast** on any computer
- Has a **small size** (~80 MB, not including standard dependencies)
- Provides **good quality** for most use cases
- Allows **local execution** – no internet required after download

## Loading a Model

This is all it takes to load the model and convert some `text` into vectors:

```py
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

print(f"Model loaded: {model}")
print(f"Max sequence length: {model.max_seq_length}")

model.encode(text)
```

> [!warning]
> The first time you run this, it downloads the model files. Subsequent runs will load from your local cache.

> [!tip]
> If you get an error about your GPU or hardware acceleration, load the model on your CPU instead by passing `device="cpu"`.

## Assignment

**Set up and test a pre-trained embedding model** for our movie search system.

1. [ ] Add the `sentence-transformers` package and its sub-dependencies to the project:
   ```sh
   uv add sentence-transformers
   ```
2. [ ] Create a new library module, e.g. `cli/lib/semantic_search.py`, and start by defining a class called `SemanticSearch`. Give it a constructor that initializes the `all-MiniLM-L6-v2` model and assigns it to an instance variable called `self.model`. (You'll also need to import `SentenceTransformer` as shown above.)
3. _Outside_ of the class definition, create a new function called `verify_model` that creates an instance of the `SemanticSearch` class and prints the model information:
   1. [ ] `Model loaded: {MODEL}`, where `{MODEL}` is the `.model` string representation
   2. [ ] `Max sequence length: {MAX_LENGTH}`, where `{MAX_LENGTH}` is the `.max_seq_length` property of the model
4. [ ] Back in your semantic search CLI script, create a new `verify` command. It should simply call the `verify_model` function to print the model information.

**Run and submit** the CLI tests.
