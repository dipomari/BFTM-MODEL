# BFTM-MODEL

The BFTM (Budget-Focused Text Model) is an advanced NLP model specifically designed for extracting, processing, and analyzing budget-related information from unstructured text data. Leveraging cutting-edge unsupervised cross-lingual representation learning, as introduced by Conneau et al.[1], the model demonstrates exceptional performance in identifying and categorizing financial allocations, expenditures, and related data points across multiple languages.

## Model Access
The BFTM model is available for download and integration via Google Drive:

BFTM-MODEL -> AI-Application -> Models

[![Model Drive Link](https://github.com/dipomari/BFTM-MODEL/assets/119870921/551dc707-b455-408c-b5ce-79e3188d5415)](https://drive.google.com/drive/folders/1eIw7C_GlQA4H_OkhGXd-QHsrHeHXmf9E?usp=share_link)

Ensure that the model is placed in the same directory as the Notebooks and Datasets for optimal functionality. Download the whole Models folder.

## Installation
This project requires the setup of two separate environments to accommodate the different dependencies for notebook execution and model operations.

### PDF Scraper and Text Extraction
For notebooks related to PDF scraping and text extraction, please install dependencies from `pdf_related_requirements.txt`:

```bash
pip install -r pdf_related_requirements.txt
```

### Model Fine-tuning, Evaluation, and Application
For model fine-tuning, evaluation, and running the application, dependencies should be installed from model_requirements.txt:

```bash
pip install -r model_requirements.txt
```

### Usage

After setting up the required environments and dependencies, the notebooks can be executed to perform PDF scraping, text extraction, and further processing with the BFTM model.
