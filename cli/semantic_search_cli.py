import argparse
import json
from lib.semantic_search import SemanticSearch, embed_query_text, embed_text, verify_embeddings, verify_model
import re

def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")
    words = text.split()
    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size - overlap)
    ]

def semantic_chunk_text(text: str, max_chunk_size: int, overlap: int) -> list[str]:
    if overlap >= max_chunk_size:
        raise ValueError("overlap must be smaller than max_chunk_size")
    sentences = re.split(r"(?<=[.!?])\s+", text)
    # return [
    #     " ".join(sentences[i:i + max_chunk_size])
    #     for i in range(0, len(sentences), max_chunk_size - overlap)
    # ]
    chunks = []
    i = 0
    while i < len(sentences):
        chunks.append(" ".join(sentences[i:i + max_chunk_size]))
        if i + max_chunk_size >= len(sentences):   
            break
        i += max_chunk_size - overlap
    return chunks

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

    chunk_parser = verify_parser.add_parser("chunk", help="Chunk documents")
    chunk_parser.add_argument("text",type=str, help="Text to chunk")
    chunk_parser.add_argument("--chunk-size", type=int, default=200, help="Size of each chunk")
    chunk_parser.add_argument("--overlap", type=int, default=0, help="Overlap of each chunk")

    semantic_chunk_parser = verify_parser.add_parser("semantic_chunk", help="Chunk documents with semantic search")
    semantic_chunk_parser.add_argument("text",type=str, help="Text to chunk")
    semantic_chunk_parser.add_argument("--max-chunk-size", type=int, default=4, help="Maximum size of each chunk")
    semantic_chunk_parser.add_argument("--overlap", type=int, default=0, help="Overlap of each chunk")


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
        case "chunk":
            chunks = chunk_text(args.text, args.chunk_size, args.overlap)
            print(f"Chunking {len(args.text)} characters")
            for index,chunk in enumerate(chunks):
                print(f"{index+1}. {chunk}")
        case "semantic_chunk":
            chunks = semantic_chunk_text(args.text, args.max_chunk_size, args.overlap)
            print(f"Semantically chunking {len(args.text)} characters")
            for index,chunk in enumerate(chunks):
                print(f"{index+1}. {chunk}")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()

