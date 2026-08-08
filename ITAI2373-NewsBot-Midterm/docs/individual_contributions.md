Individual Contributions — NewsBot Intelligence System 2.0

Student: Jose MorenoCourse: ITAI 2373 — Natural Language ProcessingProject: NewsBot Intelligence System 2.0

Contribution Summary

This repository represents my individual implementation and documentation work for the NewsBot Intelligence System 2.0 final project. I developed the final project by extending the NewsBot foundation created for the midterm and integrating additional NLP capabilities required for the final system.

My work included the implementation, execution, testing, organization, analysis, and documentation of the project components described below.

Midterm Foundation

I developed the original NewsBot pipeline used as the foundation for the final project. This work included:

Loading and exploring the BBC News dataset

Cleaning and preprocessing article text

TF-IDF feature extraction

Part-of-Speech tagging

Dependency parsing

VADER sentiment analysis

Named Entity Recognition

News article classification

Evaluation of classification results

Integration of the original NewsBot analysis workflow

Final Project Extensions

For NewsBot Intelligence System 2.0, I expanded the original system with advanced NLP functionality.

Topic Modeling

I implemented and evaluated:

Latent Dirichlet Allocation (LDA)

Non-negative Matrix Factorization (NMF)

Topic-term inspection

Document-topic assignments

Comparison of discovered topics with known BBC news categories

I also documented the limitation that the available dataset does not provide authentic publication dates, so genuine time-based topic evolution cannot be claimed from this dataset.

Summarization

I implemented article summarization functionality that supports:

Transformer-based summarization when the required model is available

Extractive summarization as a fallback

Comparison and inspection of generated summaries

Semantic Search

I implemented semantic article retrieval functionality using:

Sentence embeddings when available

TF-IDF similarity as a fallback

Ranked article retrieval

Query expansion

Category-aware search behavior

Multilingual Processing

I added multilingual functionality including:

Language detection

English-Spanish translation

Cross-language semantic search

Comparison of original and translated text

Conversational Interface

I implemented a natural-language conversational layer that can interpret requests involving:

Dataset statistics

Article search

Article summarization

Sentiment analysis

Named entities

Topic discovery

Translation

The conversational component maintains simple context so that follow-up operations can reference previously selected articles.

Final System Integration

I integrated the major project components into NewsBot Intelligence System 2.0. The integrated workflow can combine:

Article classification

Classification confidence

Sentiment analysis

Named Entity Recognition

Topic identification

Summarization

Language detection

Translation

Semantic search

Conversational interaction

Repository Organization

I organized the final GitHub repository to provide a more professional project structure, including:

config/ for configuration-related files

data/ for the dataset and project data directories

notebooks/ for the completed end-to-end notebook

src/ for reusable Python modules

tests/ for automated testing

docs/ for project documentation

requirements.txt for project dependencies

README.md for the repository overview

The completed notebook remains the primary end-to-end demonstration of the NewsBot system, while the src/ directory provides modular versions of major components.

Testing and Validation

I ran the completed notebook from beginning to end and verified that its cells executed successfully.

The repository also includes automated tests covering areas such as:

Text preprocessing

Classification

Topic modeling

Semantic search

Intent detection

Basic component integration

Documentation and Deliverables

I prepared and organized the supporting project materials, including:

README documentation

Technical documentation

Executive summary

Reflective journal

Final presentation

User guide

API reference

Deployment guide

Individual contribution documentation

Individual Accountability

This submission is organized as my individual repository. The implementation and documentation included here represent the work I am submitting for evaluation in ITAI 2373.

The project demonstrates my progression from the midterm NewsBot foundation to a more complete NLP system that integrates traditional NLP techniques with topic modeling, language-model features, multilingual processing, semantic retrieval, and conversational interaction.
