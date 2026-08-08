"""Cross-language query translation and semantic retrieval."""
from .language_detector import detect_language
from .translator import translate_text

def cross_lingual_search(query, search_engine, source_language="auto", top_k=5):
    detected = detect_language(query)
    if detected == "en":
        english_query = query
    else:
        english_query = translate_text(query, source=source_language, target="en")
        if english_query.startswith("[Translation unavailable"):
            english_query = query
    return {
        "detected_language": detected,
        "english_query": english_query,
        "results": search_engine.search(english_query, top_k=top_k),
    }
