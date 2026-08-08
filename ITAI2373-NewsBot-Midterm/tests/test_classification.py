"""Tests for the NewsBot classifier wrapper."""
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from src.analysis.classifier import NewsClassifier
from src.analysis import classifier as classifier_module


def test_classifier_returns_prediction(monkeypatch):
    # Avoid requiring the downloaded VADER lexicon during this unit test.
    monkeypatch.setattr(
        classifier_module,
        "analyze_sentiment",
        lambda text: {"compound": 0.0, "pos": 0.0, "neu": 1.0, "neg": 0.0},
    )

    documents = [
        "team wins football match",
        "government election parliament",
        "software computer technology",
        "team scores league goal",
        "minister government policy",
        "internet software computer",
    ]
    labels = ["sport", "politics", "tech", "sport", "politics", "tech"]

    vectorizer = TfidfVectorizer()
    text_features = vectorizer.fit_transform(documents).toarray()

    numeric = np.array([
        [0.0, 0.0, 1.0, 0.0, len(t), len(t.split()), 5]
        for t in documents
    ])
    X = np.hstack([text_features, numeric])

    model = LogisticRegression(max_iter=500, random_state=42)
    model.fit(X, labels)

    newsbot = NewsClassifier(model, vectorizer)
    prediction, probabilities = newsbot.predict(
        "Football result",
        "team wins football match"
    )

    assert prediction in {"sport", "politics", "tech"}
    assert isinstance(probabilities, dict)
    assert len(probabilities) == 3
