import argparse
import json
import math
import os
import pickle
import string
from collections import Counter

from nltk.stem import PorterStemmer

from count import BM25_B, BM25_K1

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


def tokenize_term(term: str) -> str:
    """把单个 term 也过一遍分词器，保证和建表时的写法一致。"""
    tokens = tokenize_text(term)
    if len(tokens) != 1:
        raise ValueError(f"term {term!r} 分词后不是恰好一个 token: {tokens}")
    return tokens[0]


def load_movies() -> list[dict]:
    with open("data/movies.json", encoding="utf-8") as f:
        return json.load(f)["movies"]


class InvertedIndex:
    def __init__(self) -> None:
        self.index: dict[str, set[int]] = {}
        self.docmap: dict[int, dict] = {}
        self.term_frequencies:dict[int,Counter] = {}
        self.doc_lengths:dict = {}


    def __add_document(self, doc_id: int, text: str) -> None:
        tokens = tokenize_text(text)
        for token in tokens:
            self.index.setdefault(token, set[int]()).add(doc_id)
        self.term_frequencies[doc_id] = Counter(tokens)
        self.doc_lengths[doc_id] = len(tokens)

    def get_documents(self, term: str) -> list[int]:
        return sorted(self.index.get(term, set[int]()))

    def get_tf(self, doc_id: int, term: str) -> int:
        return self.term_frequencies.get(doc_id, Counter()).get(term, 0)
    
    def get_idf(self, term: str) -> float:
        total_doc_count = len(self.docmap)
        term_match_doc_count = len(self.get_documents(term))
        return math.log((total_doc_count + 1) / (term_match_doc_count + 1))

    def get_bm25_idf(self, term: str) -> float:
        total_doc_count = len(self.docmap)
        term_match_doc_count = len(self.get_documents(term))
        return math.log((total_doc_count - term_match_doc_count + 0.5) / (term_match_doc_count + 0.5)+1)

    def get_bm25_tf(self, doc_id, term, k1=BM25_K1, b=BM25_B) -> float:
        tf = self.get_tf(doc_id, term)
        doc_length = self.doc_lengths.get(doc_id, 0)
        avg_doc_length = self.__get_avg_doc_length()
        length_norm=1 - b + b * (doc_length / avg_doc_length)
        return (tf * (k1 + 1)) / (tf + k1 * length_norm)

    def bm25(self, doc_id, term)->float:
        tf = self.get_bm25_tf(doc_id, term)
        idf = self.get_bm25_idf(term)
        return tf * idf
    
    def bm25_search(self, query, limit):
        # 1) 查询分词
        tokens = process_query(query)

        # 2) doc_id -> 累计 BM25 总分
        scores: dict[int, float] = {}

        # 3) 对每个查询词，把它的 BM25 分加到"含该词的文档"头上
        for token in tokens:
            for doc_id in self.get_documents(token):
                scores[doc_id] = scores.get(doc_id, 0) + self.bm25(doc_id, token)

        # 4) 按分数从高到低排序
        ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)

        # 5) 返回前 limit 个 (doc_id, score)
        return ranked[:limit]

    def __get_avg_doc_length(self) -> float:
        if not self.doc_lengths:
            return 0.0
        return sum(self.doc_lengths.values()) / len(self.doc_lengths)

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
        with open("cache/term_frequencies.pkl", "wb") as f:
            pickle.dump(self.term_frequencies, f)
        with open("cache/doc_lengths.pkl", "wb") as f:
            pickle.dump(self.doc_lengths, f)
    
    def load(self) -> None:
        with open("cache/index.pkl", "rb") as f:
            self.index = pickle.load(f)
        with open("cache/docmap.pkl", "rb") as f:
            self.docmap = pickle.load(f)
        with open("cache/term_frequencies.pkl", "rb") as f:
            self.term_frequencies = pickle.load(f)
        with open("cache/doc_lengths.pkl", "rb") as f:
            self.doc_lengths = pickle.load(f)



def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    subparsers.add_parser("build", help="Build and save the inverted index")

    tf_parser = subparsers.add_parser("tf", help="Get term frequency")
    tf_parser.add_argument("doc_id", type=int, help="Document ID")
    tf_parser.add_argument("term", type=str, help="Term")

    idf_parser = subparsers.add_parser("idf", help="Get inverse document frequency")
    idf_parser.add_argument("term", type=str, help="Term")

    tfidf_parser = subparsers.add_parser("tfidf", help="Get term frequency-inverse document frequency")
    tfidf_parser.add_argument("doc_id", type=int, help="Document ID")
    tfidf_parser.add_argument("term", type=str, help="Term")

    bm25_idf_parser = subparsers.add_parser(
        "bm25idf", help="Get BM25 IDF score for a given term"
    )
    bm25_idf_parser.add_argument("term", type=str, help="Term to get BM25 IDF score for")

    bm25_tf_parser = subparsers.add_parser(
    "bm25tf", help="Get BM25 TF score for a given document ID and term"
)
    bm25_tf_parser.add_argument("doc_id", type=int, help="Document ID")
    bm25_tf_parser.add_argument("term", type=str, help="Term to get BM25 TF score for")
    bm25_tf_parser.add_argument(
        "k1", type=float, nargs="?", default=BM25_K1, help="Tunable BM25 K1 parameter"
    )
    bm25_tf_parser.add_argument(
        "b", type=float, nargs="?", default=BM25_B, help="Tunable BM25 b parameter"
    )

    bm25search_parser = subparsers.add_parser(
    "bm25search", help="Search movies using full BM25 scoring"
)
    bm25search_parser.add_argument("query", type=str, help="Search query")
    bm25search_parser.add_argument(
        "limit", type=int, nargs="?", default=5, help="Number of results to return"
    )


    args = parser.parse_args()

    match args.command:
        case "search":
            try:
                inverse_index = InvertedIndex()
                inverse_index.load()
            except Exception as e:
                print(f"[Error] loading inverted index: {e}")
                return
            query_tokens = process_query(args.query)
            results = []  # 存文档 id
            for token in query_tokens:
                for doc_id in inverse_index.get_documents(token):
                    if doc_id not in results:
                        results.append(doc_id)
                        if len(results) == 5:  # 满 5 条就停
                            break
                if len(results) == 5:
                    break
            result_str = ""
            for index, doc_id in enumerate(results, 1):
                movie = inverse_index.docmap[doc_id]
                result_str += f"{index}. {movie['title']} (id={movie['id']})\n"
            print(result_str)

        case "build":
            inverse_index = InvertedIndex()
            inverse_index.build()
            inverse_index.save()

        case "tf":
            try:
                inverse_index = InvertedIndex()
                inverse_index.load()
            except Exception as e:
                print(f"[Error] loading inverted index: {e}")
                return
            token = tokenize_term(args.term)
            print(inverse_index.get_tf(args.doc_id, token))

        case "idf":
            try:
                inverse_index = InvertedIndex()
                inverse_index.load()
            except Exception as e:
                print(f"[Error] loading inverted index: {e}")
                return
            token = tokenize_term(args.term)
            total_doc_count = len(inverse_index.docmap)
            term_match_doc_count = len(inverse_index.get_documents(token))
            idf = math.log((total_doc_count + 1) / (term_match_doc_count + 1))
            print(f"Inverse document frequency of '{args.term}': {idf:.2f}")

        case "tfidf":
            try:
                inverse_index = InvertedIndex()
                inverse_index.load()
            except Exception as e:
                print(f"[Error] loading inverted index: {e}")
                return
            token = tokenize_term(args.term)
            tf = inverse_index.get_tf(args.doc_id, token)
            idf = inverse_index.get_idf(token)
            tfidf = tf * idf
            print(f"Term frequency-inverse document frequency of '{args.term}': {tfidf:.2f}")

        case "bm25idf":
            try:
                inverse_index = InvertedIndex()
                inverse_index.load()
            except Exception as e:
                print(f"[Error] loading inverted index: {e}")
                return
            token = tokenize_term(args.term)
            bm25_idf = inverse_index.get_bm25_idf(token)
            print(f"BM25 IDF score of '{args.term}': {bm25_idf:.2f}")
    
        case "bm25tf":
            try:
                inverse_index = InvertedIndex()
                inverse_index.load()
            except Exception as e:
                print(f"[Error] loading inverted index: {e}")
                return
            token = tokenize_term(args.term)
            bm25_tf = inverse_index.get_bm25_tf(args.doc_id, token, args.k1,args.b)
            print(f"BM25 TF score of '{args.term}': {bm25_tf:.2f}")
        
        case "bm25search":
            try:
                inverse_index = InvertedIndex()
                inverse_index.load()
            except Exception as e:
                print(f"[Error] loading inverted index: {e}")
                return
            results = inverse_index.bm25_search(args.query, args.limit)
            # 1. (15) The Adventures of Mowgli - Score: 7.79
            for index, (doc_id, score) in enumerate(results, 1):
                print(f"{index}. ({doc_id}) {inverse_index.docmap[doc_id]['title']} - Score: {score:.2f}")



        
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
