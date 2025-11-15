---
# Data Preprocessing
----

## Overview

In this section, the focus of my notebooks is on data preprocessing. This involves:

1. Data Extraction (`01-data-loading.ipynb`)

2. Data Cleaning (`02-data-cleaning.ipynb`)

## Dataset

Sourced the Enron email dataset from a CSV file sourced from Kaggle [here](https://www.kaggle.com/datasets/wcukierski/enron-email-dataset)

## Notebook Summaries

The main goal of the preprocessing step is to load the dataset, extract relevant fields and clean the email content so it can be used to gather meaningful insights.

### 1.`01-data-loading.ipynb` 

- Load the dataset from CSV files.

- Extract key fields using an HTML parser:

    - Sender

    - Receiver

    - Subject

Email Content

### 2.`02-data-cleaning.ipynb` 

Real-world emails contain a lot of noise, such as HTML tags, disclaimers, signatures, and forwarded content. This notebook focuses on cleaning the data by:

- Removing unwanted whitespace and HTML tags

- Filtering out:

    -  Email disclaimers

    -  File paths and directory information

    - Phone numbers and email addresses

    - Forwarded/Original headers

    - Signatures and sign-offs

Tools used: BeautifulSoup and regular expressions (regex).











