---
# Embeddings
---

## Overview

This folder explores different embedding methods to determine which produces the most informative embeddings for the Enron dataset.

Good embeddings are critical for both classification and vector search tasks: the richer the embeddings, the better the results!

## Notebook Summaries

### 1. `01-using-word2vec.ipynb`

- Explored Word2Vec embeddings.

- Prepared text by tokenisation, stopword removal, and filtering irrelevant words using SpaCy.

- Applied Word2Vec to convert words into embeddings and explored semantic relationships.

- Evaluated embeddings to see how well they captured semantic relationships between selected words.

### 2. `02-using-BERT.ipynb`

- Explored DistilBERT embeddings (a lighter BERT model).

- Preprocessed text by chunking emails to avoid model truncation and tokenised using `DistilBertTokenizer`.

- Created email embeddings with DistilBERT.

- Applied clustering algorithms (e.g., K-Means, HDBSCAN) on the DistilBERT embeddings.

    - Clusters were not well-separated, likely due to noisy, short, and fragmented email text.

    - Some emails with different topics grouped together.

    - Confirms that while BERT captures context, pretrained embeddings alone may not produce strong groupings without fine-tuning.


### 3. `03-using-sentence-transformers.ipynb`

- Explored SentenceTransformer (mini) embeddings.

- Sentence Transformers are optimised for sentence-level semantic similarity and lightweight, reducing resource usage.

- Again, applied clustering algorithms (e.g., K-Means, HDBSCAN) on the embeddings.

    - Clusters show some overlap, as many emails cover multiple topics (Operations, Legal, Finance).

    - Cluster patterns align with TF-IDF results, indicating that the embeddings capture meaningful semantic structure.

    - Generic emails are grouped into larger “noise” clusters, especially in HDBSCAN.

### Findings

Overall, Sentence Transformer embeddings are more semantically coherent than the others, making them suitable for further tasks like classification and vector search.
