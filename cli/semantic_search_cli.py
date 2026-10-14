import argparse
import json
from lib.semantic_search import SemanticSearch, embed_query_text, embed_text, verify_embeddings, verify_model


def main() -> None:

    parser = argparse.ArgumentParser(description="Semantic Search CLI")

    verify_parser = parser.add_subparsers(dest="command", help="Available commands")
    verify_parser.add_parser("verify", help="Verify the model")

    embed_text_parser = verify_parser.add_parser("embed_text", help="Embed text")
    embed_text_parser.add_argument("text", type=str, help="Text to embed")

    verify_embeddings_parser = verify_parser.add_parser("verify_embeddings", help="Verify embeddings")

    embed_query_text_parser = verify_parser.add_parser("embed_query", help="Embed query text")
    embed_query_text_parser.add_argument("query", type=str, help="Query text to embed")

    search_parser = verify_parser.add_parser("search", help="Search for documents")
    search_parser.add_argument("query", type=str, help="Query text to search")
    search_parser.add_argument("--limit", type=int, default=5, help="Number of results to return")



    args = parser.parse_args()


    match args.command:
        case "verify":
            verify_model()
        case "embed_text":
            embed_text(args.text)
        case "verify_embeddings":
            verify_embeddings()
        case "embed_query":
            embed_query_text(args.query)
        case "search":
            with open("data/movies.json", encoding="utf-8") as f:
                documents = json.load(f)["movies"]
            semantic_search = SemanticSearch()
            semantic_search.load_or_create_embeddings(documents)
            results = semantic_search.search(args.query, args.limit)
            for i, r in enumerate(results, 1):
                print(f"{i}. {r['title']} (score: {r['score']:.4f})")
                print(f"  {r['description'][:100]}...\n")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()