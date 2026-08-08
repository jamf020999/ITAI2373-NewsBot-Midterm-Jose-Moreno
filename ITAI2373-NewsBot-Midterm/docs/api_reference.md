NewsBot Intelligence System 2.0 — API Reference

Course: ITAI 2373 — Natural Language ProcessingStudent: Jose Moreno

Overview

This document describes the reusable Python modules organized under the src/ directory of NewsBot Intelligence System 2.0. The modules were separated from the completed notebook to provide a clearer, modular project structure.

src.data_processing

text_preprocessor.py

clean_text(text)

Cleans raw text before NLP processing.

Parameter

text — input text.

Returns

Cleaned lowercase string with HTML, URLs, email addresses, digits, special characters, and extra whitespace removed.

preprocess_text(text, remove_stopwords=True, lemmatize=True)

Runs the NewsBot preprocessing pipeline.

Parameters

text — input text.

remove_stopwords — whether English stop words should be removed.

lemmatize — whether WordNet lemmatization should be applied.

Returns

Preprocessed text as a string.

feature_extractor.py

NewsFeatureExtractor

Wrapper for NewsBot TF-IDF and numeric feature extraction.

NewsFeatureExtractor(max_features=5000)

Creates a TF-IDF vectorizer using unigram and bigram features.

fit_transform(texts)

Fits the TF-IDF vectorizer and transforms input documents.

Returns

TF-IDF feature matrix.

transform(texts)

Transforms new documents using the fitted vectorizer.

numeric_features(title, content, sentiment)

Creates numeric article features from sentiment scores and article length information.

data_validator.py

validate_news_dataframe(df)

Checks whether a DataFrame contains the expected NewsBot fields.

ReturnsA dictionary containing:

Validation status

Missing columns

Row count

Duplicate article count

Empty article count

src.analysis

sentiment_analyzer.py

analyze_sentiment(text)

Uses NLTK VADER to calculate sentiment scores.

ReturnsA dictionary containing:

compound

pos

neu

neg

label

The label is reported as positive, negative, or neutral.

ner_extractor.py

extract_entities(text)

Uses the spaCy English NLP model to extract named entities.

ReturnsA list of dictionaries containing:

text

label

Entity labels may include people, organizations, geographic locations, and other spaCy entity categories.

classifier.py

NewsClassifier

Wrapper for a trained NewsBot classification model and TF-IDF vectorizer.

NewsClassifier(classifier, vectorizer)

Parameters

classifier — trained classification model.

vectorizer — fitted text vectorizer.

predict(title, content)

Combines text and numeric features and predicts the news category.

Returns

Predicted category

Dictionary of category probabilities when supported by the classifier

topic_modeler.py

TopicModeler

Reusable topic-modeling interface supporting LDA and NMF.

TopicModeler(n_topics=5, method="lda")

Parameters

n_topics — number of topics.

method — "lda" or "nmf".

fit_transform(documents)

Fits the selected topic model and returns document-topic distributions.

get_topic_words(topic_id, n_words=10)

Returns the highest-weight terms for a selected topic.

topic_table(n_words=12)

Returns a pandas DataFrame summarizing discovered topics and their top terms.

src.language_models

summarizer.py

split_sentences(text)

Splits input text into sentences.

extractive_summary(text, max_sentences=3)

Produces an extractive summary using TF-IDF sentence representations and similarity to the document centroid.

summarize_article(text, method="auto", max_sentences=3)

Attempts transformer-based summarization using DistilBART when available.

If transformer summarization is unavailable and method="auto", the function falls back to extractive summarization.

Returns

Summary string.

embeddings.py

SemanticSearch

Provides semantic article retrieval.

SemanticSearch(dataframe)

Initializes the search system from a NewsBot DataFrame.

The module attempts to use the SentenceTransformers all-MiniLM-L6-v2 model. If unavailable, it falls back to TF-IDF similarity.

search(query, top_k=5, category=None)

Searches the article collection.

Parameters

query — natural-language search query.

top_k — maximum number of results.

category — optional category filter.

ReturnsA DataFrame containing matching articles and similarity scores.

generator.py

generate_insights(category, entities, sentiment, category_probabilities)

Generates short rule-based observations from classification confidence, sentiment, and important named entities.

Returns

List of insight strings.

src.multilingual

language_detector.py

detect_language(text)

Uses langdetect to identify the likely language of input text.

Returns

Language code such as en or es.

"unknown" when detection cannot be performed reliably.

translator.py

translate_text(text, source="auto", target="es")

Translates text using deep-translator and Google Translator when available.

Parameters

text — text to translate.

source — source language or "auto".

target — destination language.

Returns

Translated text or an explanatory fallback message if translation is unavailable.

cross_lingual_analyzer.py

cross_lingual_search(query, search_engine, source_language="auto", top_k=5)

Detects the query language, translates non-English queries into English when possible, and sends the resulting query to the NewsBot semantic-search engine.

ReturnsA dictionary containing:

Detected language

English query

Search results

src.conversation

intent_classifier.py

classify_query_intent(query)

Uses keyword matching to determine the likely intent of a natural-language NewsBot request.

Supported intents include:

summary

search

sentiment

entities

topics

translation

statistics

When no explicit intent is detected, the function defaults to search.

query_processor.py

QueryProcessor

Stateful conversational query processor.

QueryProcessor(dataframe, search_engine)

Parameters

dataframe — NewsBot article dataset.

search_engine — initialized semantic-search component.

The processor stores the most recently referenced article and conversation history.

process(query)

Processes a natural-language request.

Depending on the detected intent, the method can:

Return dataset statistics

Search articles

Summarize an article

Translate an article summary

ReturnsA dictionary containing:

Original query

Detected intent

Text response

Associated data

response_generator.py

response_message(intent, count=None)

Produces short conversational response messages for selected intents.

src.utils

evaluation.py

classification_metrics(y_true, y_pred)

Calculates classification evaluation information.

ReturnsA dictionary containing:

Accuracy

Classification report

Confusion matrix

visualization.py

plot_category_distribution(df)

Creates a bar chart showing the number of articles in each news category.

Returns

Matplotlib axes object.

export.py

export_dataframe(df, path)

Exports a pandas DataFrame.

Supported formats:

CSV

JSON

JSONL

The function creates parent directories when necessary.

Returns

Output Path.

Package Initialization Files

Each major src/ directory contains an __init__.py file. These files define the directories as Python packages and expose selected functions or classes for convenient importing.

Examples:

from src.analysis import analyze_sentiment
from src.analysis import TopicModeler
from src.language_models import SemanticSearch
from src.multilingual import detect_language

Notes

The src/ package provides modular versions of the major NewsBot components. The completed Jupyter notebook remains the primary end-to-end demonstration of the final system and contains additional exploratory code, visualizations, experiments, and integrated demonstrations.

Some components require external NLP resources or model downloads. The completed notebook contains the setup workflow used for the submitted project.
