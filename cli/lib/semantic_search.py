import json
import os
import re
from sentence_transformers import SentenceTransformer
import numpy as np


class SemanticSearch:
    def __init__(self):
        model = SentenceTransformer("all-MiniLM-L6-v2")
        self.model = model
        self.embeddings = None
        self.documents = None
        self.document_map = {}
    
    def generate_embedding(self, text):
        if not text.strip():
            raise ValueError("Text must be provided")
        embedding = self.model.encode([text])
        return embedding[0]
    
    def build_embeddings(self, documents):
        self.documents = documents
        self.document_map = {d["id"]: d for d in documents}
        docs_str = [f"{d['title']}: {d['description']}" for d in documents]
        self.embeddings = self.model.encode(docs_str, show_progress_bar=True)
        np.save("cache/movie_embeddings.npy", self.embeddings)
        return self.embeddings

    def load_or_create_embeddings(self, documents):
        self.documents = documents
        self.document_map = {d["id"]: d for d in documents}
        if os.path.exists("cache/movie_embeddings.npy"):
            with open("cache/movie_embeddings.npy", "rb") as f:
                self.embeddings = np.load(f)
                if self.embeddings.shape[0] != len(documents):
                    self.embeddings = self.build_embeddings(documents)
        else:
            self.embeddings = self.build_embeddings(documents)
        return self.embeddings

    def search(self,query:str,limit:int):
        if self.embeddings is None:
            raise ValueError("No embeddings loaded. Call `load_or_create_embeddings` first.")
        query_embedding = self.generate_embedding(query)
        similarities = [cosine_similarity(query_embedding, doc_embedding) for doc_embedding in self.embeddings]
        
        results = []
        for sim, doc_id in zip(similarities, self.document_map.keys()):
            doc = self.document_map[doc_id]
            results.append({
                "score": sim,
                "title": doc["title"],
                "description": doc["description"],
            })

        results.sort(key=lambda r: r["score"], reverse=True)
        return results[:limit]


        

def verify_model():
    semantic_search = SemanticSearch()
    print(f"Model loaded: {semantic_search.model}")
    print(f"Max sequence length: {semantic_search.model.max_seq_length}")
    
def embed_text(text: str):
    semantic_search = SemanticSearch()
    embedding =  semantic_search.generate_embedding(text)
    print(f"Text: {text}")
    print(f"First 3 dimensions: {embedding[:3]}")
    print(f"Dimensions: {embedding.shape[0]}")

def verify_embeddings():
    with open("data/movies.json", "r") as f:
        documents = json.load(f)["movies"]
    semantic_search = SemanticSearch()
    semantic_search.load_or_create_embeddings(documents)
    print(f"Number of docs:   {len(documents)}")
    print(
        f"Embeddings shape: {semantic_search.embeddings.shape[0]} vectors in {semantic_search.embeddings.shape[1]} dimensions"
    )

def embed_query_text(query:str):
    semantic_search = SemanticSearch()
    embedding = semantic_search.generate_embedding(query)
    print(f"Query: {query}")
    print(f"First 3 dimensions: {embedding[:3]}")
    print(f"Shape: {embedding.shape}")

# 余弦相似度
def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot_product / (norm1 * norm2)


def semantic_chunk_text(text: str, max_chunk_size: int, overlap: int) -> list[str]:
    if overlap >= max_chunk_size:
        raise ValueError("overlap must be smaller than max_chunk_size")
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks = []
    i = 0
    while i < len(sentences):
        chunks.append(" ".join(sentences[i:i + max_chunk_size]))
        if i + max_chunk_size >= len(sentences):
            break
        i += max_chunk_size - overlap
    return chunks


class ChunkedSemanticSearch(SemanticSearch):
    def __init__(self):
        super().__init__()
        self.chunk_embeddings = None
        self.chunk_metadata = None
    
    def build_chunk_embeddings(self, documents: list[dict]) -> np.ndarray:
        self.documents = documents
        self.document_map = {d["id"]: d for d in documents}

        all_chunks: list[str] = []
        chunk_metadata: list[dict] = []

        for movie_idx, doc in enumerate(documents):
            desc = doc.get("description") or ""
            if not desc.strip():
                continue

            desc_chunks = semantic_chunk_text(desc, 4, 1)
            total_chunks = len(desc_chunks)

            for chunk_idx, chunk in enumerate(desc_chunks):
                all_chunks.append(chunk)
                chunk_metadata.append({
                    "movie_idx": movie_idx,
                    "chunk_idx": chunk_idx,
                    "total_chunks": total_chunks,
                })

        self.chunk_embeddings = self.model.encode(all_chunks, show_progress_bar=True)
        self.chunk_metadata = chunk_metadata

        os.makedirs("cache", exist_ok=True)
        np.save("cache/chunk_embeddings.npy", self.chunk_embeddings)
        with open("cache/chunk_metadata.json", "w", encoding="utf-8") as f:
            json.dump({"chunks": chunk_metadata, "total_chunks": len(all_chunks)}, f, indent=2)

        return self.chunk_embeddings

    def load_or_create_embeddings(self, documents):
        super().load_or_create_embeddings(documents)
        if os.path.exists("cache/chunk_embeddings.npy"):
            self.chunk_embeddings = np.load("cache/chunk_embeddings.npy")
            self.chunk_metadata = json.load(open("cache/chunk_metadata.json", "r", encoding="utf-8"))["chunks"]
        else:
            self.chunk_embeddings = self.build_chunk_embeddings(documents)