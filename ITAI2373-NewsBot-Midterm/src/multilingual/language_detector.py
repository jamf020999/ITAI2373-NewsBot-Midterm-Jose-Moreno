"""Language detection from the NewsBot multilingual extension."""
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 42

def detect_language(text):
    text = str(text).strip()
    if len(text) < 20:
        return "unknown"
    try:
        return detect(text)
    except Exception:
        return "unknown"
