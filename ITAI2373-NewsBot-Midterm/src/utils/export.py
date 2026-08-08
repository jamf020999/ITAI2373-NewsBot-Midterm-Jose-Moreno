"""Simple report/data export helpers."""
from pathlib import Path

def export_dataframe(df, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix.lower() == ".csv":
        df.to_csv(path, index=False)
    elif path.suffix.lower() in {".json", ".jsonl"}:
        df.to_json(path, orient="records", indent=2)
    else:
        raise ValueError("Supported formats: .csv, .json, .jsonl")
    return path
