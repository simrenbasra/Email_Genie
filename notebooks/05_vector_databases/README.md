---
# Modelling
---

## Overview

Notebooks in this folder explore vector databases and different indexing methods for semantic search.

Expanded the dataset to ~30,000 emails.

Re-ran the embedding creation in Google Colab to use GPU resources and a larger embedding model.

The embeddings and vector indices created here are used in the Email_Genie web app see folder (`email-genie`).

## Notebook Summaries

### 1. `01-setting_up_FAISS.ipynb`

- Used FAISS for vector search.

- Experimented with different indexing methods on the labelßled dataset to assess retrieval accuracy.

### 2. `02-extending-to-all-emails.ipynb`

- Expanded to the full dataset (~30,000 emails).

- Ran on Google Colab for GPU access and to handle larger embedding models.

- Created vector embeddings and indices for the full dataset.

- These embeddings and vector indices are used in the Email_Genie web app (located in the data folder)

