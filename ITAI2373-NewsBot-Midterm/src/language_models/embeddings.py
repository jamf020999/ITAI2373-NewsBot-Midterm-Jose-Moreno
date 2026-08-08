"""Semantic search using SentenceTransformers with TF-IDF fallback."""
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.data_processing.text_preprocessor import preprocess_text

class SemanticSearch:
    def __init__(self, dataframe):
        self.df = dataframe.reset_index(drop=True)
        self.sentence_model = None
        self.embeddings = None
        self.tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2), min_df=2, max_df=0.8)
        processed = [preprocess_text(t) for t in self.df["content"].astype(str)]
        self.tfidf_matrix = self.tfidf.fit_transform(processed)
        try:
            from sentence_transformers import SentenceTransformer
            self.sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
            self.embeddings = self.sentence_model.encode(
                self.df["content"].astype(str).tolist(), normalize_embeddings=True
            )
        except Exception:
            self.embeddings = self.tfidf_matrix

    def search(self, query, top_k=5, category=None):
        candidates = np.arange(len(self.df))
        if category is not None:
            candidates = np.where(self.df["category"].str.lower().eq(str(category).lower()).values)[0]
        if not len(candidates):
            return pd.DataFrame()
        if self.sentence_model is not None and not hasattr(self.embeddings, "tocsr"):
            q = self.sentence_model.encode([query], normalize_embeddings=True)[0]
            similarities = self.embeddings[candidates] @ q
        else:
            q = self.tfidf.transform([preprocess_text(query)])
            similarities = cosine_similarity(q, self.tfidf_matrix[candidates]).ravel()
        local = similarities.argsort()[::-1][:top_k]
        rows = candidates[local]
        result = self.df.iloc[rows][["article_id", "title", "category", "content"]].copy()
        result["similarity"] = similarities[local]
        return result.reset_index(drop=True)
