"""Tests for NewsBot text preprocessing."""
from src.data_processing.text_preprocessor import clean_text, preprocess_text


def test_clean_text_removes_noise():
    result = clean_text("Hello WORLD! Visit https://example.com 123")
    assert "hello world" in result
    assert "http" not in result
    assert "123" not in result


def test_clean_text_handles_empty_input():
    assert clean_text("") == ""


def test_preprocess_text_returns_string():
    result = preprocess_text("The cats are running quickly.")
    assert isinstance(result, str)
    assert len(result) > 0
