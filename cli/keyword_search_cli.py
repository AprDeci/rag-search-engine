from typing import Any


import argparse
import json


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
                if args.query in movie["title"]:
                    results.append(movie)
            results = results[:5]
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