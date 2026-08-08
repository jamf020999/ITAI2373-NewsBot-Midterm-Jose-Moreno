"""VADER sentiment analysis used by NewsBot."""
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    try:
        scores = SentimentIntensityAnalyzer().polarity_scores(str(text))
    except LookupError as exc:
        raise RuntimeError("NLTK vader_lexicon is required.") from exc
    compound = scores["compound"]
    scores["label"] = "positive" if compound > 0.05 else "negative" if compound < -0.05 else "neutral"
    return scores
