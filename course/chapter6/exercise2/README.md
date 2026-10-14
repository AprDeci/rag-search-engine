# Hybrid Search

So if keyword search is better in some cases and semantic search is better in others... _which should we use_?

The answer is **both**! It's called **Hybrid Search** – we run both search methods and then combine their results intelligently.

## Query Categories

We expect different search methods to perform better on different types of queries. Here are some of the common ones:

1. **Known-Item Searches:** The user knows the exact title or name they want. _Keyword search is usually best_.
   - "The Revenant"
   - "Paddington 2"
   - "Leonardo DiCaprio movies"
2. **Topical Searches:** The user describes a concept or theme they are interested in. _Semantic search is usually best_.
   - "survival in wilderness"
   - "family friendly comedies"
   - "psychological thrillers"
3. **Exploratory Searches:** The user is browsing broadly without a specific item in mind. _Either method can be best, depending on specificity_.
   - "good movies to watch"
   - "recent releases"
   - "award winners"

## Consider

Before we hop into the assignment, I want you to run both keyword and semantic search using the following commands and _think about_ which method gave you better results and why. Then try to come up with your own queries that you think would be better suited for each method and see if you are correct.

```sh
uv run cli/semantic_search_cli.py search_chunked "gods among mortals"
uv run cli/keyword_search_cli.py bm25search "gods among mortals"

uv run cli/semantic_search_cli.py search_chunked "Bear DiCaprio"
uv run cli/keyword_search_cli.py bm25search "Bear DiCaprio"
```

## Assignment

**Let's start stubbing out the code for hybrid search.**

1. [ ] Create a new entrypoint script, `cli/hybrid_search_cli.py`, with the usual starting boilerplate:

   ```py
   import argparse


   def main() -> None:
       parser = argparse.ArgumentParser(description="Hybrid Search CLI")
       parser.add_subparsers(dest="command", help="Available commands")

       args = parser.parse_args()

       match args.command:
           case _:
               parser.print_help()


   if __name__ == "__main__":
       main()
   ```

2. [ ] Create a new file for your hybrid search logic. It should _import_ some of our earlier keyword and semantic search logic. Here's a starting point that should get you going:

   ```py
   import os

   from .keyword_search import InvertedIndex
   from .semantic_search import ChunkedSemanticSearch


   class HybridSearch:
       def __init__(self, documents: list[dict]) -> None:
           self.documents = documents
           self.semantic_search = ChunkedSemanticSearch()
           self.semantic_search.load_or_create_chunk_embeddings(documents)

           self.idx = InvertedIndex()
           if not os.path.exists(self.idx.index_path):
               self.idx.build()
               self.idx.save()

       def _bm25_search(self, query: str, limit: int) -> list[dict]:
           self.idx.load()
           return self.idx.bm25_search(query, limit)

       def weighted_search(self, query: str, alpha: float, limit: int = 5) -> list[dict]:
           raise NotImplementedError("Weighted hybrid search is not implemented yet.")

       def rrf_search(self, query: str, k: int, limit: int = 10) -> list[dict]:
           raise NotImplementedError("RRF hybrid search is not implemented yet.")
   ```

> [!warning]
> You can structure your code however you like, and yours likely doesn't look exactly like mine. Take some time to [refactor](https://en.wikipedia.org/wiki/Code_refactoring) your code so that it's organized in a way that makes sense to you.

**Run and submit** the CLI tests once you are satisfied with the basic structure.
