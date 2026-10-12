import argparse
import json
import os
import pickle
import string

from nltk.stem import PorterStemmer

with open("data/stopwords.txt", encoding="utf-8") as f:
    stop_words = set(f.read().splitlines())

stemmer = PorterStemmer()


def tokenize_text(text: str) -> list[str]:
    """小写 -> 去标点 -> 分词 -> 去停用词 -> 词干化。"""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return [stemmer.stem(t) for t in text.split() if t not in stop_words]


def process_query(query: str) -> list[str]:
    return tokenize_text(query)


def load_movies() -> list[dict]:
    with open("data/movies.json", encoding="utf-8") as f:
        return json.load(f)["movies"]


class InvertedIndex:
    def __init__(self) -> None:
        self.index: dict[str, set[int]] = {}
        self.docmap: dict[int, dict] = {}

    def __add_document(self, doc_id: int, text: str) -> None:
        for token in tokenize_text(text):
            self.index.setdefault(token, set[int]()).add(doc_id)

    def get_documents(self, term: str) -> list[int]:
        return sorted(self.index.get(term, set[int]()))

    def build(self) -> None:
        for movie in load_movies():
            self.docmap[movie["id"]] = movie
            self.__add_document(movie["id"], f"{movie['title']} {movie['description']}")

    def save(self) -> None:
        os.makedirs("cache", exist_ok=True)
        with open("cache/index.pkl", "wb") as f:
            pickle.dump(self.index, f)
        with open("cache/docmap.pkl", "wb") as f:
            pickle.dump(self.docmap, f)
    
    def load(self) -> None:
        with open("cache/index.pkl", "rb") as f:
            self.index = pickle.load(f)
        with open("cache/docmap.pkl", "rb") as f:
            self.docmap = pickle.load(f)



def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    subparsers.add_parser("build", help="Build and save the inverted index")

    args = parser.parse_args()

    match args.command:
        case "search":
            # print the search query here
            print(f"Searching for: {args.query}")  
            with open("data/movies.json", encoding="utf-8") as f: 
                movies = json.load(f)["movies"]
            results = []
            for movie in movies:
                title = movie["title"].lower().split()
                title_token = [stemmer.stem(token) for token in title]
                if any(token in title_token for token in process_query(args.query)):
                    results.append(movie)
            results = results[:5]  # limit to 5 results
            result_str = ""
            for index, movie in enumerate(results, 1):
                result_str += f"{index}. {movie['title']}\n"
            print(result_str)

        case "build":
            inverse_index = InvertedIndex()
            inverse_index.build()
            inverse_index.save()
            

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
