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

### 1.`01-data-loading.ipynb` 

- Load the dataset from the CSV files
- Expand out the raw dataset by extracting the following using a HTML parser:

    - Sender
    - Receiver
    - Subject
    - Email Content

### 2.`02-data-cleaning.ipynb` 

- Emails are notoriously messy real-life data, they contain a lot of whitespace, html tagging, and noise which needs to be removed to derive valuable insights from the data.

- I use `BeautifulSoup` and some regex to filter out noise like:\
    - email disclaimers
    - files and directory paths
    - phone numbers, email addresses
    - Forwarded/Original headers
    - signatures and sign offs

The mian aim for `01-data-processing` is to load the dataset, extract necessary information and remove enough of the nosie from useful email content.









