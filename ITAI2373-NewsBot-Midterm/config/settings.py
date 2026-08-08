"""
Configuration settings for NewsBot Intelligence System 2.0
ITAI 2373 - Natural Language Processing
Jose Moreno
"""

# -------------------------
# DATA SETTINGS
# -------------------------

DATASET_FILE = "data/raw/BBC News Train.csv"

TEXT_COLUMN = "Text"
CATEGORY_COLUMN = "Category"

# -------------------------
# MODEL SETTINGS
# -------------------------

RANDOM_STATE = 42
TEST_SIZE = 0.20

# TF-IDF
MAX_TFIDF_FEATURES = 5000

# Topic Modeling
N_TOPICS = 5
TOP_WORDS = 10

# -------------------------
# NLP SETTINGS
# -------------------------

SPACY_MODEL = "en_core_web_sm"

# Default language used by the system
DEFAULT_LANGUAGE = "en"

# Default translation language
DEFAULT_TRANSLATION_TARGET = "es"

# -------------------------
# SEARCH SETTINGS
# -------------------------

DEFAULT_SEARCH_RESULTS = 5

# -------------------------
# SUMMARIZATION SETTINGS
# -------------------------

DEFAULT_SUMMARY_SENTENCES = 3

# -------------------------
# PROJECT INFORMATION
# -------------------------

PROJECT_NAME = "NewsBot Intelligence System 2.0"
COURSE = "ITAI 2373 - Natural Language Processing"
AUTHOR = "Jose Moreno"
