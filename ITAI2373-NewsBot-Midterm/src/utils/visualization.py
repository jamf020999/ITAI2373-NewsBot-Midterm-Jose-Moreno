"""Reusable plotting helpers."""
import matplotlib.pyplot as plt

def plot_category_distribution(df):
    ax = df["category"].value_counts().plot(kind="bar", title="News Category Distribution")
    ax.set_xlabel("Category")
    ax.set_ylabel("Articles")
    plt.tight_layout()
    return ax
