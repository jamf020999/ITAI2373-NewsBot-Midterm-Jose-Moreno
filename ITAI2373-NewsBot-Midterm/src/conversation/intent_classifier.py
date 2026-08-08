"""Keyword-based intent classifier from the final notebook."""
def classify_query_intent(query):
    q = str(query).lower()
    keywords = {
        "summary": ["summarize", "summary", "shorten"],
        "search": ["find", "search", "show me", "articles about", "news about"],
        "sentiment": ["sentiment", "positive", "negative", "neutral", "tone"],
        "entities": ["entity", "entities", "person", "people", "organization", "company", "location"],
        "topics": ["topic", "topics", "theme", "themes"],
        "translation": ["translate", "translation", "spanish", "english"],
        "statistics": ["how many", "count", "distribution", "dataset", "categories"],
    }
    scores = {intent: sum(k in q for k in words) for intent, words in keywords.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "search"
