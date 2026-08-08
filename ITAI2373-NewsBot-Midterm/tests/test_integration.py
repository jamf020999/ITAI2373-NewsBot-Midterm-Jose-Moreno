"""Lightweight integration tests across multiple NewsBot components."""
import pandas as pd

from src.data_processing.text_preprocessor import clean_text
from src.analysis.topic_modeler import TopicModeler
from src.language_models.embeddings import SemanticSearch
from src.conversation.intent_classifier import classify_query_intent


def sample_dataframe():
    return pd.DataFrame({
        "article_id": [1, 2, 3, 4, 5, 6],
        "title": [
            "Football Final", "League Result",
            "Election News", "Government Policy",
            "Technology Update", "Software News"
        ],
        "content": [
            "football team wins league goal match",
            "football player scores goal in league match",
            "government election parliament minister policy",
            "government minister announces parliament policy",
            "computer software internet technology company",
            "technology company releases computer software",
        ],
        "category": [
            "sport", "sport", "politics",
            "politics", "tech", "tech"
        ],
    })


def test_preprocessing_and_topic_modeling_work_together():
    df = sample_dataframe()
    cleaned = [clean_text(text) for text in df["content"]]

    modeler = TopicModeler(n_topics=3, method="lda")
    topic_distribution = modeler.fit_transform(cleaned)

    assert topic_distribution.shape[0] == len(df)
    assert topic_distribution.shape[1] == 3


def test_semantic_search_returns_results():
    df = sample_dataframe()
    engine = SemanticSearch(df)
    results = engine.search("football league", top_k=2)

    assert not results.empty
    assert len(results) <= 2
    assert "similarity" in results.columns


def test_conversation_intent_detection():
    assert classify_query_intent("Summarize article 1") == "summary"
    assert classify_query_intent("Find articles about technology") == "search"
    assert classify_query_intent("Translate article 2 to Spanish") == "translation"
