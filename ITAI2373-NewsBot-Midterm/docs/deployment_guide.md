NewsBot Intelligence System 2.0 — Deployment Guide

Course: ITAI 2373 — Natural Language ProcessingStudent: Jose Moreno

1. Purpose

This guide explains how to set up and run the submitted NewsBot Intelligence System 2.0 project. The primary end-to-end implementation is the completed Jupyter notebook stored in the notebooks/ directory.

2. Repository Requirements

The repository should contain the following main project components:

config/ — configuration files

data/ — raw data and output directories

notebooks/ — completed NewsBot notebook

src/ — reusable NewsBot Python modules

tests/ — automated tests

docs/ — project documentation

requirements.txt — Python dependencies

README.md — project overview

The BBC dataset should be available at:

data/raw/BBC News Train.csv

3. Recommended Environment

The completed NewsBot notebook was designed to run in Google Colab. Google Colab is therefore the recommended environment for reproducing the submitted notebook workflow.

A local Python/Jupyter environment can also be used, but package versions, NLP resources, and model availability may differ from Colab.

4. Google Colab Deployment

Open Google Colab.

Upload or open the completed .ipynb file from the repository's notebooks/ directory.

Run the notebook from the first cell downward.

Execute the setup and installation cells included in the notebook.

When prompted by the notebook, upload BBC News Train.csv.

Continue running the remaining cells sequentially.

Allow model or NLP-resource downloads to complete when required.

The notebook contains the complete workflow from data loading and preprocessing through the final NewsBot 2.0 integration.

5. Local Installation

To run the repository locally, first obtain the project using Git or download the repository as a ZIP archive.

From the repository root, install the listed dependencies:

pip install -r requirements.txt

A virtual environment is recommended but not required.

Example:

python -m venv .venv

Activate the environment using the command appropriate for the operating system, then install requirements.txt.

6. NLP Resources and Models

NewsBot uses multiple NLP libraries and may require resources that are not bundled directly with the repository.

The submitted notebook contains its own setup workflow for the resources it uses. When reproducing the project, run those setup cells before executing later NLP sections.

Depending on the environment, resources used by components may include:

NLTK corpora or sentiment resources

spaCy English-language resources

SentenceTransformer models

Transformer summarization models

Some of these resources are downloaded when the relevant component is initialized and therefore require internet access.

7. Data Placement

For the organized repository, place the original dataset at:

data/raw/BBC News Train.csv

The repository also contains:

data/processed/ — reserved for processed datasets

data/models/ — reserved for serialized models or model artifacts

data/results/ — reserved for exported results

These directories may remain empty if the notebook does not export persistent artifacts to them.

When running the submitted Colab notebook, follow its built-in file-upload step for the CSV dataset.

8. Running the Notebook

Open the completed notebook located in:

notebooks/

Run all cells sequentially. Later sections depend on variables, models, and data structures created earlier in the notebook.

The workflow includes:

Environment and dependency setup

Dataset loading and validation

Exploratory analysis

Text preprocessing

Feature extraction and classification

Sentiment and linguistic analysis

Topic modeling

Summarization

Semantic search

Multilingual processing

Conversational queries

Integrated NewsBot 2.0 analysis

9. Running the Automated Tests

The repository includes automated tests under:

tests/

From the repository root, run:

pytest tests/

The tests cover major reusable components including preprocessing, classification, topic modeling, semantic search, intent detection, and integration behavior.

The local environment must have the dependencies from requirements.txt installed before the tests are executed.

10. Using the src/ Package

The modular source code is stored in src/.

Example imports include:

from src.data_processing.text_preprocessor import preprocess_text
from src.analysis.sentiment_analyzer import analyze_sentiment
from src.analysis.topic_modeler import TopicModeler
from src.language_models.embeddings import SemanticSearch
from src.multilingual.language_detector import detect_language
from src.conversation.intent_classifier import classify_query_intent

Run Python commands from the repository root so that the src package can be resolved correctly.

11. External Connectivity

Some NewsBot features may depend on internet connectivity.

Examples include:

Downloading NLP models

Transformer summarization model loading

SentenceTransformer model loading

Translation services

If an external model is unavailable, some components include fallback behavior. For example, the summarization and semantic-search implementations can use simpler alternatives when their preferred model is unavailable.

12. API Keys and Credentials

The repository contains:

config/api_keys_template.txt

This is a template only. Real API keys, passwords, or other private credentials should never be committed to the public GitHub repository.

The submitted NewsBot workflow should be reproduced using the services and setup actually implemented in the notebook. Placeholder entries in the template do not mean that every listed service is required.

13. Troubleshooting

Dataset not found

Confirm that BBC News Train.csv is available. In Colab, upload it when the notebook requests it. For the repository structure, keep a copy under data/raw/.

Import error

Install the project dependencies:

pip install -r requirements.txt

Then restart the Python/Jupyter runtime if necessary.

NLP resource error

Run the notebook's setup cells again and confirm that required NLP resources downloaded successfully.

Transformer or embedding model unavailable

Confirm internet access and retry the model download. Where implemented, NewsBot can fall back to extractive summarization or TF-IDF-based search.

Translation unavailable

Translation functionality can depend on an external translation service and internet connectivity. Retry with an active connection.

Tests cannot import src

Run pytest from the repository root rather than from inside the tests/ directory.

14. Deployment Scope

This final project is delivered primarily as a Jupyter/Colab-based NLP system and modular Python repository. A standalone production web application is not required for the core submission; the assignment identifies a web frontend as a bonus opportunity.

The completed notebook is the primary executable demonstration of the submitted NewsBot Intelligence System 2.0.
