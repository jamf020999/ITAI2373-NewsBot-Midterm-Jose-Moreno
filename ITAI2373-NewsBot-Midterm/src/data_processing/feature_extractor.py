"""TF-IDF and numeric feature extraction for NewsBot."""
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from .text_preprocessor import preprocess_text

class NewsFeatureExtractor:
    def __init__(self, max_features=5000):
        self.vectorizer = TfidfVectorizer(
            max_features=max_features, ngram_range=(1, 2), min_df=2, max_df=0.8
        )

    def fit_transform(self, texts):
        processed = [preprocess_text(t) for t in texts]
        return self.vectorizer.fit_transform(processed)

    def transform(self, texts):
        processed = [preprocess_text(t) for t in texts]
        return self.vectorizer.transform(processed)

    @staticmethod
    def numeric_features(title, content, sentiment):
        full_text = f"{title} {content}"
        return np.array([[
            sentiment["compound"], sentiment["pos"], sentiment["neu"], sentiment["neg"],
            len(full_text), len(full_text.split()), len(title)
        ]])
