"""LDA/NMF topic modeling adapted from the final notebook."""
import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation, NMF
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

class TopicModeler:
    def __init__(self, n_topics=5, method="lda"):
        self.n_topics = n_topics
        self.method = method.lower()
        self.vectorizer = None
        self.model = None
        self.feature_names = None

    def fit_transform(self, documents):
        if self.method == "lda":
            self.vectorizer = CountVectorizer(max_features=3000, min_df=3, max_df=0.90, ngram_range=(1, 2))
            matrix = self.vectorizer.fit_transform(documents)
            self.model = LatentDirichletAllocation(
                n_components=self.n_topics, max_iter=20, learning_method="batch", random_state=42
            )
        elif self.method == "nmf":
            self.vectorizer = TfidfVectorizer(max_features=3000, min_df=3, max_df=0.90, ngram_range=(1, 2))
            matrix = self.vectorizer.fit_transform(documents)
            self.model = NMF(n_components=self.n_topics, init="nndsvda", random_state=42, max_iter=500)
        else:
            raise ValueError("method must be 'lda' or 'nmf'")
        self.feature_names = self.vectorizer.get_feature_names_out()
        return self.model.fit_transform(matrix)

    def get_topic_words(self, topic_id, n_words=10):
        weights = self.model.components_[topic_id]
        indices = weights.argsort()[-n_words:][::-1]
        return [self.feature_names[i] for i in indices]

    def topic_table(self, n_words=12):
        return pd.DataFrame([
            {"model": self.method.upper(), "topic": i,
             "top_terms": ", ".join(self.get_topic_words(i, n_words))}
            for i in range(self.n_topics)
        ])
