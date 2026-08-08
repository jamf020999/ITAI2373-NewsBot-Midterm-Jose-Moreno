"""Extractive summarization with optional DistilBART transformer summarization."""
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def split_sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\\s+", str(text).strip()) if s.strip()]

def extractive_summary(text, max_sentences=3):
    sentences = split_sentences(text)
    if len(sentences) <= max_sentences:
        return " ".join(sentences)
    vectorizer = TfidfVectorizer(stop_words="english", max_features=2000)
    matrix = vectorizer.fit_transform(sentences)
    centroid = np.asarray(matrix.mean(axis=0))
    scores = cosine_similarity(matrix, centroid).ravel()
    chosen = sorted(scores.argsort()[-max_sentences:])
    return " ".join(sentences[i] for i in chosen)

def summarize_article(text, method="auto", max_sentences=3):
    text = str(text).strip()
    if not text:
        return ""
    if method in {"auto", "transformer"}:
        try:
            from transformers import pipeline
            summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
            result = summarizer(text[:3500], max_length=130, min_length=35, do_sample=False)
            return result[0]["summary_text"]
        except Exception:
            if method == "transformer":
                raise
    return extractive_summary(text, max_sentences)
