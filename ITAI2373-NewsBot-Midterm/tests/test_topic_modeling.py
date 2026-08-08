"""Tests for LDA and NMF topic modeling."""
from src.analysis.topic_modeler import TopicModeler


DOCUMENTS = [
    "football team league goal match player",
    "football player scores goal league match",
    "government election parliament minister policy",
    "government minister election parliament policy",
    "computer software internet technology company",
    "technology software computer internet company",
] * 2


def test_lda_topic_modeling():
    modeler = TopicModeler(n_topics=3, method="lda")
    distribution = modeler.fit_transform(DOCUMENTS)

    assert distribution.shape == (len(DOCUMENTS), 3)
    assert len(modeler.get_topic_words(0, n_words=5)) == 5


def test_nmf_topic_modeling():
    modeler = TopicModeler(n_topics=3, method="nmf")
    distribution = modeler.fit_transform(DOCUMENTS)

    assert distribution.shape == (len(DOCUMENTS), 3)
    assert len(modeler.get_topic_words(0, n_words=5)) == 5
