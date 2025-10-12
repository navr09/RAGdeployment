from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class Retriever:
    def __init__(self, docs, embedding_model="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(embedding_model)
        self.docs = docs
        self.embeddings = self.model.encode(docs, convert_to_numpy=True)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def retrieve(self, query, k=3):
        query_vec = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_vec, k)
        return [self.docs[i] for i in indices[0]]
