"""Stateful NewsBot query processor based on NewsBotConversation."""
import re
from .intent_classifier import classify_query_intent
from src.language_models.summarizer import summarize_article
from src.multilingual.translator import translate_text

class QueryProcessor:
    def __init__(self, dataframe, search_engine):
        self.dataframe = dataframe
        self.search_engine = search_engine
        self.last_article_id = None
        self.history = []

    def _category(self, query):
        q = query.lower()
        for category in sorted(self.dataframe["category"].unique()):
            if category.lower() in q:
                return category
        return None

    def _article_id(self, query):
        match = re.search(r"(?:article|id)\\s*#?\\s*(\\d+)", query.lower())
        return int(match.group(1)) if match else None

    def process(self, query):
        intent = classify_query_intent(query)
        category = self._category(query)
        article_id = self._article_id(query)
        result = {"query": query, "intent": intent, "response": None, "data": None}

        if intent == "statistics":
            result["response"] = (
                f"The dataset contains {len(self.dataframe)} articles across "
                f"{self.dataframe['category'].nunique()} categories."
            )
            result["data"] = self.dataframe["category"].value_counts().to_frame("article_count")
        elif intent in {"summary", "translation"}:
            article_id = article_id or self.last_article_id
            if article_id is None:
                result["response"] = "Include an article ID, such as 'Summarize article 1833.'"
            else:
                match = self.dataframe[self.dataframe["article_id"] == article_id]
                if match.empty:
                    result["response"] = f"Article {article_id} was not found."
                else:
                    article = match.iloc[0]
                    self.last_article_id = article_id
                    summary = summarize_article(article["content"], method="auto")
                    result["response"] = translate_text(summary, source="en", target="es") if intent == "translation" else summary
                    result["data"] = {"article_id": article_id, "title": article["title"], "category": article["category"]}
        else:
            search_query = query
            for phrase in ["find", "search for", "show me", "articles about", "news about"]:
                search_query = re.sub(phrase, "", search_query, flags=re.IGNORECASE)
            found = self.search_engine.search(search_query, top_k=5, category=category)
            if not found.empty:
                self.last_article_id = int(found.iloc[0]["article_id"])
            result["response"] = f"Found {len(found)} relevant articles."
            result["data"] = found
        self.history.append(result)
        return result
