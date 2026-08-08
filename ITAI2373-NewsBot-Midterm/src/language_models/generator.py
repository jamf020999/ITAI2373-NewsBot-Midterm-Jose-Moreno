"""Rule-based insight generation used by the integrated notebook system."""
def generate_insights(category, entities, sentiment, category_probabilities):
    insights = []
    confidence = max(category_probabilities.values())
    insights.append(
        f"High confidence {category} classification ({confidence:.2%})"
        if confidence > 0.8 else "Uncertain classification - consider manual review"
    )
    compound = sentiment["compound"]
    if compound > 0.1:
        insights.append(f"Positive sentiment detected ({compound:.3f})")
    elif compound < -0.1:
        insights.append(f"Negative sentiment detected ({compound:.3f})")
    else:
        insights.append(f"Neutral sentiment ({compound:.3f})")
    important = [e["text"] for e in entities if e["label"] in {"PERSON", "ORG", "GPE"}]
    if important:
        insights.append("Key entities: " + ", ".join(important[:3]))
    return insights
