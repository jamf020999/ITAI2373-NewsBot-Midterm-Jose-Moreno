"""Classification wrapper matching the integrated NewsBot feature layout."""
import numpy as np
from src.data_processing.text_preprocessor import preprocess_text
from .sentiment_analyzer import analyze_sentiment

class NewsClassifier:
    def __init__(self, classifier, vectorizer):
        self.classifier = classifier
        self.vectorizer = vectorizer

    def predict(self, title, content):
        full_text = f"{title} {content}"
        processed = preprocess_text(full_text)
        text_features = self.vectorizer.transform([processed]).toarray()
        s = analyze_sentiment(full_text)
        numeric = np.array([[s["compound"], s["pos"], s["neu"], s["neg"],
                             len(full_text), len(full_text.split()), len(title)]])
        combined = np.hstack([text_features, numeric])
        prediction = self.classifier.predict(combined)[0]
        if hasattr(self.classifier, "predict_proba"):
            probs = self.classifier.predict_proba(combined)[0]
            probabilities = dict(zip(self.classifier.classes_, probs))
        else:
            probabilities = {prediction: 1.0}
        return prediction, probabilities
