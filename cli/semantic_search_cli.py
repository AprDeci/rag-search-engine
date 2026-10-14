import argparse
from lib.semantic_search import embed_query_text, embed_text, verify_embeddings, verify_model

def main() -> None:

    parser = argparse.ArgumentParser(description="Semantic Search CLI")

    verify_parser = parser.add_subparsers(dest="command", help="Available commands")
    verify_parser.add_parser("verify", help="Verify the model")

    embed_text_parser = verify_parser.add_parser("embed_text", help="Embed text")
    embed_text_parser.add_argument("text", type=str, help="Text to embed")

    verify_embeddings_parser = verify_parser.add_parser("verify_embeddings", help="Verify embeddings")

    embed_query_text_parser = verify_parser.add_parser("embed_query", help="Embed query text")
    embed_query_text_parser.add_argument("query", type=str, help="Query text to embed")



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
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()