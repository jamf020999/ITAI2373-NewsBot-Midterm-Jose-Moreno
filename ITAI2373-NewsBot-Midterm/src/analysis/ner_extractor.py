"""spaCy named-entity extraction."""
import spacy

_NLP = None

def _nlp():
    global _NLP
    if _NLP is None:
        _NLP = spacy.load("en_core_web_sm")
    return _NLP

def extract_entities(text):
    doc = _nlp()(str(text))
    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
