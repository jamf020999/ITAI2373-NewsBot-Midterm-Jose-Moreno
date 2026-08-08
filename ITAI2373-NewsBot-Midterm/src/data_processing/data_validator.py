"""Dataset validation helpers."""
REQUIRED_COLUMNS = {"article_id", "title", "content", "category"}

def validate_news_dataframe(df):
    missing = REQUIRED_COLUMNS.difference(df.columns)
    return {
        "valid": not missing,
        "missing_columns": sorted(missing),
        "rows": len(df),
        "duplicate_articles": int(df.duplicated(subset=["content"]).sum()) if "content" in df else None,
        "empty_articles": int(df["content"].fillna("").str.len().eq(0).sum()) if "content" in df else None,
    }
