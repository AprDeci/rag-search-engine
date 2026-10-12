from typing import Any
import string


import argparse
import json

with open("data/stopwords.txt", encoding="utf-8") as f:
    stop_words = set(f.read().splitlines())

def stem(token: str) -> str:
    for suffix in _SUFFIXES:
        if len(token) > len(suffix) + 2 and token.endswith(suffix):
            return token[: -len(suffix)]
    return token

def process_query(query: str) -> list[str]:
    query = query.strip().lower()
    table = str.maketrans("", "", string.punctuation)
    query = query.translate(table)
    query_tokens = query.split()
    query_tokens = [token for token in query_tokens if token not in stop_words]
    return query_tokens

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            # print the search query here
            print(f"Searching for: {args.query}")  
            with open("data/movies.json", encoding="utf-8") as f: 
                movies = json.load(f)["movies"]
            results = []
            for movie in movies:
                if any(token in movie["title"].lower() for token in process_query(args.query)):
                    results.append(movie)
            results = results[:5]  # limit to 5 results
            result_str = f"""
            Searching for: {args.query}
            """
            result_str = f"""
            Searching for: {args.query}
            """
            result_str = ""
            for index, movie in enumerate(results, 1):
                result_str += f"{index}. {movie['title']}\n"
            print(result_str)

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()