---
# Preliminary Data Insights
---

## Overview

This section focuses on gaining preliminary insights into the Enron email dataset using exploratory analysis and topic modelling.

## Notebook Summaries

### 1. `01-using-TF-IDF.ipynb`

This notebook performs tokenisation and topic modeling using TF-IDF and Latent Dirichlet Allocation (LDA) to uncover the context and themes within emails.

For efficiency, only the first 15,000 rows of the dataset were used.

The notebook is divided into the following sections:

1. **Data Loading:** Load the cleaned data from the data folder.

2. **Preparing Text:** Preprocess the text for tokenisation, handling stopwords, and using SpaCy to remove irrelevant words.

3. **Vectorising Text:** Apply TF-IDF with a custom tokeniser to convert text into numerical form.

4. **Topic Modelling with LDA:** Group the data into topics and analyse groupings.

### Key Insights

1. Legal Terms

-	Terms such as `privileged material`, `binding enforceable`, `distribution disclosure`, `evidence binding`,`affiliate privileged`

-	Suggests many emails seem to focus on confidentiality and legal compliance/agreements.

2. Risk and Financial Terms

-	Terms like `operational risk`,`risk operation`, `risk book`, `buy sell`.

-	Suggests many emails discuss risk management and financial transactions.

After reading more on Enron and its downfall, these findings seem to align. The company faced issues in risky trading, compliance issues and even dodgy affiliations to hide losses. 


### Findings

TF-IDF captures general business topics but struggles with the high noise in email data.

Some topics reflect everyday operations, further refinement is needed before moving to clustering.

The noise suggests that more advanced vectorisation methods, such as word embeddings, may better capture context.

Preliminary results indicate the project could also provide insight into Enron’s downfall, beyond classifying work emails.

Next steps: explore word embeddings for richer representations and deeper understanding of email content.