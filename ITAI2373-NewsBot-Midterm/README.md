# ITAI2373 NewsBot Intelligence System 2.0

## Student

Jose Moreno

## Course

ITAI 2373 – Natural Language Processing

---

## Project Overview

This project extends the original NewsBot Intelligence System developed during the midterm into a more comprehensive news analysis platform. It combines multiple Natural Language Processing (NLP) techniques into a complete pipeline capable of analyzing news articles from different perspectives.

The system performs text preprocessing, feature extraction, linguistic analysis, sentiment analysis, named entity recognition, topic modeling, text summarization, semantic search, multilingual processing, and conversational interaction. The objective of the project is to demonstrate how different NLP techniques can work together in a single intelligent system for real-world news analysis.

---

## Important

Before running the notebook:

The notebook is located on: https://github.com/jamf020999/ITAI2373-NewsBot-Final_Project-Jose-Moreno/blob/main/ITAI2373-NewsBot-Midterm/notebooks/NewsBot_Intelligence_System_2_Completed_Jose_Moreno_ITAI2373.ipynb

The dataset is located in: https://github.com/jamf020999/ITAI2373-NewsBot-Final_Project-Jose-Moreno/blob/main/ITAI2373-NewsBot-Midterm/data/raw/BBC%20News%20Train.csv

1. Open the Jupyter Notebook in Google Colab.
2. Run all cells from top to bottom.
3. When prompted, upload the dataset file **BBC News Train.csv**.
4. Wait until all cells finish executing.

An executed PDF version of the notebook is included in this repository so the outputs can be reviewed without running the notebook.

---

## Installation

To install the required Python packages in a local environment, run:

```bash
pip install -r requirements.txt
```

The completed notebook can also be run in Google Colab, where the required resources are installed or loaded by the notebook setup cells.

---

## Features

The NewsBot Intelligence System includes the following NLP components:

- Text preprocessing and cleaning
- TF-IDF feature extraction
- Part-of-Speech (POS) tagging
- Dependency parsing
- Sentiment analysis
- Named Entity Recognition (NER)
- News article classification
- Topic Modeling using LDA and NMF
- Extractive text summarization
- Transformer-based text summarization
- Semantic search using sentence embeddings
- Query expansion
- Multilingual language detection
- Automatic translation
- Cross-language search
- Interactive conversational NewsBot interface
- Integrated article analysis

---

## Dataset

Dataset used:

- `data/raw/BBC News Train.csv`

The dataset contains BBC news articles from several categories and is used for training, evaluating, and demonstrating the NLP components throughout the project.

The dataset does not provide authentic publication dates, so the project does not make claims about genuine topic evolution over time.

---

## Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- spaCy
- Scikit-learn
- Matplotlib
- Seaborn
- WordCloud
- Plotly
- Transformers
- Sentence Transformers
- LangDetect
- Deep Translator
- pytest

---

## Repository Structure

- `config/` – Project configuration and API key template
- `data/` – Raw dataset and directories for processed data, models, and results
- `docs/` – User guide, API reference, deployment guide, and individual contributions
- `notebooks/` – Completed NewsBot Intelligence System 2.0 Jupyter notebook
- `reports/` – Technical documentation, executive summary, reflective journal, presentation, and supporting reports
- `src/` – Modular Python source code for the NewsBot system
- `tests/` – Automated tests for major system components
- `README.md` – Project overview and usage information
- `requirements.txt` – Python dependencies required by the project

---

## Main System Components

### Data Processing

The project includes text cleaning, preprocessing, validation, and feature extraction components used to prepare BBC news articles for analysis.

### News Classification

NewsBot trains and evaluates supervised machine learning models for automatic news article classification. The project compares multiple classifiers and integrates the strongest trained model into the final system.

### Sentiment Analysis

VADER sentiment analysis is used to identify positive, negative, and neutral sentiment in news content.

### Named Entity Recognition

spaCy Named Entity Recognition is used to identify entities such as people, organizations, and locations appearing in news articles.

### Topic Modeling

NewsBot uses both Latent Dirichlet Allocation (LDA) and Non-negative Matrix Factorization (NMF) to discover latent themes within the BBC news corpus.

### Text Summarization

The system supports article summarization using transformer-based summarization when available and an extractive summarization method as a fallback.

### Semantic Search

Semantic search allows users to retrieve relevant articles based on meaning rather than relying only on exact keyword matches. Sentence embeddings are used when available, with TF-IDF similarity available as a fallback.

### Multilingual Processing

The multilingual components provide language detection, translation, and cross-language search capabilities.

### Conversational Interface

The conversational NewsBot allows users to interact with the system using natural-language queries. Supported requests include article search, summarization, sentiment analysis, entity extraction, topic exploration, translation, and dataset statistics.

---

## Testing

Automated tests are included in the `tests/` directory.

The test suite covers major areas including:

- Text preprocessing
- Classification
- Topic modeling
- Semantic search
- Intent detection
- Basic system integration

To run the tests from the project environment:

```bash
pytest tests/
```

---

## My Contributions

Since this is an individual submission, I completed all aspects of the project, including:

- Data preprocessing and cleaning
- Feature extraction using TF-IDF
- Part-of-Speech tagging
- Dependency parsing
- Sentiment analysis
- Named Entity Recognition
- News classification model training and evaluation
- Topic modeling implementation
- Text summarization
- Semantic search
- Query expansion
- Multilingual language processing
- Cross-language search
- Conversational NewsBot development
- Final system integration
- Testing and evaluation
- GitHub repository organization
- Technical documentation

Additional details are available in:

`docs/individual_contributions.md`

---

## Results

The completed NewsBot Intelligence System successfully performs:

- Automatic news classification
- Sentiment detection
- Named entity extraction
- Linguistic analysis
- Topic discovery
- Automatic text summarization
- Semantic similarity search
- Multilingual language detection and translation
- Cross-language information retrieval
- Interactive conversational news analysis

The final system integrates these capabilities into a single NewsBot 2.0 workflow rather than treating them only as separate NLP exercises.

The project demonstrates how multiple Natural Language Processing techniques can be integrated into an intelligent system capable of analyzing news articles from several different perspectives.

---

## Limitations

The project has several important limitations:

- The dataset represents a single news publisher and a limited historical collection.
- Sentiment analysis may misinterpret irony or complex reporting.
- Named Entity Recognition may miss or misclassify uncommon entities.
- Topic-model labels require human interpretation.
- Translation may lose tone, context, or idiomatic meaning.
- Automatic summaries may omit important context.
- The dataset does not contain authentic publication dates for reliable temporal trend analysis.

Human review remains important when automated NLP results are used for high-impact decisions.

---

## Documentation

Additional project documentation is available in the `docs/` directory:

- `user_guide.md`
- `api_reference.md`
- `deployment_guide.md`
- `individual_contributions.md`

Final project reports and presentation materials are available in the `reports/` directory.

---

## Repository

GitHub Repository:

https://github.com/jamf020999/ITAI2373-NewsBot-Final_Project-Jose-Moreno
