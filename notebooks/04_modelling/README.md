---
# Modelling
---

## Overview

This folder explores email classification using embeddings generated from the Enron dataset. 

The goal is to understand how different models perform on labelled email data and which model performs the best.

## Notebook Summaries

### 1. `01-labelling-data.ipynb`

- Labelled ~1,000 emails into six categories: Operations, Legal, Finance, Personal, Spam, Unknown.

- Used regex as a guide, followed by a 4-eyes manual check.

-  Quick and dirty approach to labelling data 

### 2. `02-create-embeddings.ipynb`

- Created embeddings for labelled emails using mini Sentence Transformer model.

- These embeddings serve as input features for classification models.

### 3. `03-classification-models.ipynb`

- Explored three classification models on the embedded emails:

- Dataset distribution:

    - Operations: 230

    - Legal: 212

    - Finance: 208

    - Personal: 185

    - Spam: 184

    - Unknown: 112

- Models tested:

    - Logistic Regression: Simple, fast, interpretable baseline.

    - Support Vector Machine (SVM): Handles high-dimensional embeddings and focuses on class boundaries.

    - Random Forest: Captures non-linear relationships through an ensemble of decision trees.

- Model results:

    - Performance across all three models was fairly similar.

    - Logistic Regression baseline was not outperformed by more complex models, suggesting limited labelled data (~1,300 emails) could be a constraint.

    - Single-label assignment per email may confuse models, as many emails contain multiple topics.

### 4. `04-fine-tuning-BERT.ipynb`

- Explored fine-tuning DistilBERT using the labelled dataset to improve classification performance.

- For the current dataset size, simpler models are sufficient and fine-tuning BERT is not justified unless more labelled data is added.


## Project Re-scope

Classification didn't perform as expected, this could be due to limited labelled data and the multi-topic nature of emails.

The project has been re-scoped to focus on semantic search, enabling users to explore and gain insights into the collapse of Enron through email retrieval.

