"""Text cleaning and preprocessing adapted from the completed NewsBot notebook."""
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def _stop_words():
    try:
        return set(stopwords.words("english"))
    except LookupError:
        return set()

def clean_text(text):
    """Remove HTML, URLs, email addresses, special characters, digits and extra spaces."""
    if pd.isna(text):
        return ""
    text = str(text).lower()
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"http\\S+|www\\S+|https\\S+", "", text)
    text = re.sub(r"\\S+@\\S+", "", text)
    text = re.sub(r"[^a-zA-Z\\s]", "", text)
    return re.sub(r"\\s+", " ", text).strip()

def preprocess_text(text, remove_stopwords=True, lemmatize=True):
    """Run the notebook's cleaning, stop-word removal and lemmatization pipeline."""
    text = clean_text(text)
    if not text:
        return ""
    tokens = text.split()
    if remove_stopwords:
        stops = _stop_words()
        tokens = [t for t in tokens if t not in stops]
    if lemmatize:
        try:
            tokens = [lemmatizer.lemmatize(t) for t in tokens]
        except LookupError:
            pass
    tokens = [t for t in tokens if len(t) > 2]
    return " ".join(tokens)
