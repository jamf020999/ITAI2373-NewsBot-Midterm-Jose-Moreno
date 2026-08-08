"""Evaluation utilities."""
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def classification_metrics(y_true, y_pred):
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "classification_report": classification_report(y_true, y_pred, output_dict=True),
        "confusion_matrix": confusion_matrix(y_true, y_pred),
    }
