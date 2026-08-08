NewsBot Intelligence System 2.0 — User Guide

Course: ITAI 2373 — Natural Language ProcessingStudent: Jose Moreno

Overview

NewsBot Intelligence System 2.0 is an end-to-end NLP project for analyzing BBC news articles. The completed system combines the original midterm pipeline with final-project extensions for topic modeling, summarization, semantic search, multilingual processing, and conversational interaction.

The main implementation is provided in the completed Jupyter notebook in the notebooks/ directory.

Dataset

The project uses BBC News Train.csv.

For the organized repository, the dataset is stored under:

data/raw/BBC News Train.csv

The completed notebook was originally designed for Google Colab and includes an upload step for BBC News Train.csv. When running the notebook in Colab, follow that upload step and select the CSV file when prompted.

Running the Project

Open the completed NewsBot .ipynb file from the notebooks/ directory in Google Colab.

Run the notebook cells in order from the beginning.

When the notebook requests the dataset, upload BBC News Train.csv.

Allow the notebook's setup cells to install or load the resources required by later sections.

Continue running the remaining cells sequentially.

The final notebook has been executed end-to-end and contains the outputs used to demonstrate the completed project.

Main NewsBot Features

The notebook demonstrates:

Text preprocessing and cleaning

TF-IDF feature extraction

Part-of-Speech tagging

Dependency parsing

VADER sentiment analysis

Named Entity Recognition

News classification

LDA topic modeling

NMF topic modeling

Article summarization

Semantic article search

Query expansion

Language detection

English-Spanish translation workflow

Cross-language search and comparison

Conversational natural-language queries

Integrated NewsBot 2.0 article analysis

Topic Modeling

The final-project extension uses both Latent Dirichlet Allocation (LDA) and Non-negative Matrix Factorization (NMF). The notebook displays topic terms, topic assignments, and comparisons with the known BBC news categories.

Because the BBC dataset used by the project does not provide authentic publication dates, the project does not claim genuine topic evolution over time.

Summarization and Semantic Search

NewsBot includes article summarization with a transformer-based option and an extractive fallback. The notebook reports which summarization backend is available.

Semantic search allows a user to enter a query and retrieve related BBC articles. The project uses sentence embeddings when available and provides a TF-IDF fallback.

Multilingual Features

The multilingual section demonstrates:

Automatic language detection

English-Spanish translation

Cross-language semantic search

Comparison of original and translated content

Translation quality may vary, so multilingual output should be treated as an automated aid rather than a perfect replacement for human translation.

Conversational NewsBot

The conversational interface accepts natural-language requests and routes them to the appropriate NewsBot capability.

Demonstrated queries include:

How many articles and categories are in the dataset?

Show me articles about mobile phones and software

Summarize article 1833

What is the sentiment of politics articles?

Which organizations appear most often in business news?

Show me the discovered topics

Translate article 1833 into Spanish

The conversation component supports requests involving dataset statistics, article search, summaries, sentiment, named entities, topics, and translation.

Integrated Article Analysis

The final NewsBotIntelligenceSystem2 integration combines multiple components into one workflow. For a supplied title and article body, the system can return:

Predicted news category

Classification confidence

Category probabilities

Sentiment analysis

Named entities

Topic identification

Article summary

Detected language

Optional translated summary

The integrated system also exposes semantic search and conversational query functionality.

Repository Code

Reusable versions of the main NewsBot components are organized under src/. These modules separate data processing, analysis, language-model functionality, multilingual processing, conversational processing, and utility functions.

The notebook remains the primary end-to-end demonstration of the project.

Testing

Automated tests are located in tests/ and cover preprocessing, classification, topic modeling, and basic integration behavior.

From a local environment with the project dependencies installed, the test suite can be run with:

pytest tests/

Limitations

Important limitations documented by the project include:

The dataset represents one publisher and a limited historical period.

VADER sentiment analysis may misinterpret irony or complex reporting.

Named Entity Recognition may miss or misclassify uncommon names.

Topic-model labels require human interpretation.

Translation may lose tone, idioms, or regional context.

Extractive summaries can omit context.

Transformer summaries may introduce unsupported wording.

The dataset does not support authentic time-based trend claims.

Human review remains important when using automated NLP output for high-impact decisions.

Recommended Demonstration

For the clearest demonstration of NewsBot 2.0, open the completed notebook and run the cells sequentially. The notebook contains the full progression from the original NLP foundation through the final advanced modules and integrated system.
