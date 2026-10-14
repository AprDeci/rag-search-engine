# Semantic Search

![Semantic Search](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/semantic-search-1920x1080.mp4)

Keyword and metadata search are useful, but they have some serious limits. Have you ever searched "baggins" on Netflix and gotten "The Hobbit"? Keyword search _can't do that_ unless the word "baggins" appears in the title, description, cast, or other searchable metadata.

[Semantic search](https://en.wikipedia.org/wiki/Semantic_search) can find results where words have similar _meaning_, not just similar _spelling_. It can find relevant documents even when they don't contain your exact search terms.

**Bear Movie Search Example:**

Query: "exciting adventure"

- **Keyword Search**
  - Searches for: "exciting" AND "adventure"
  - Misses: Movies described as a "thrilling journey"
- **Semantic Search**
  - Understands: You want action-packed films
  - Finds: Movies with "gripping," "suspenseful," "journey"

## When Semantic Search Is Better

- **Synonym matching:** "Happy movies" → finds "joyful" or "uplifting" films
- **Conceptual queries:** "Movies about friendship" → finds films exploring character bonds
- **Natural language:** "What bear movies are good for kids?" → understands family-friendly content

## When Keyword Search Is Better

- **Exact terms:** Medical codes or phrases like "COVID-19"
- **Proper nouns:** Specific titles like "The Matrix"
- **Technical jargon:** Programming terms like "dependency injection"

## Assignment

Let's build semantic search. We'll use a _new_ CLI script for semantic search operations.

In the `cli` directory, create a new file called `semantic_search_cli.py` and paste in the following code:

```py
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Semantic Search CLI")
    args = parser.parse_args()

    match args.command:
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
```

**Run and submit** the CLI tests.
