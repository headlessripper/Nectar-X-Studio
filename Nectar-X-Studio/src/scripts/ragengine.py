
import os
from sentence_transformers import SentenceTransformer, util
import faiss
from scripts.SYS_Config.Config import TRANSFORMER_MODEL_PATH

class RAGEngine:
    def __init__(self, model_path=TRANSFORMER_MODEL_PATH):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Embedding model not found: {model_path}")

        self.embedder = SentenceTransformer(model_path)
        self.index = None
        self.docs = []

    def add_documents(self, texts):
        embeddings = self.embedder.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        self.docs.extend(texts)

        if self.index is None:
            self.index = faiss.IndexFlatIP(embeddings.shape[1])  # cosine similarity

        self.index.add(embeddings)

    def retrieve(self, query, top_k=3):
        if self.index is None or not self.docs:
            return []

        q_emb = self.embedder.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        scores, indices = self.index.search(q_emb, top_k)
        return [self.docs[i] for i in indices[0] if i < len(self.docs)]