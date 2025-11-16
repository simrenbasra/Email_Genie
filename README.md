----
# Email Genie
----

### 🌟 Welcome to the Enron Email Explorer! 🌟

Curious about the emails behind Enron's infamous collapse? This app lets you search and explore the Enron email dataset!

Here is how to use it:

- Type your search query: a keyword, phrase, or term you want to find in the emails

- Choose how many results to see: pick the number of top emails to display (default= 5)

- Click “Search” and (hopefully) emails matching your query will appear below with:

    - Subject: The email’s subject line.

    - Summary: A quick snapshot of the email content.

    - Body: The full email text, formatted like an Outlook message for easy reading.
    
Not sure what to search? Here are some suggested search phrases: “bankruptcy”, “audit failure”, “Chapter 11”, “financial collapse”, “insolvency”.

### Check out my Demo!

[Watch my Demo](https://www.loom.com/share/e3fa5a746ec54072bb87189e5846548b)

## Project Set Up

### Clone the Repository

```bash
git clone https://github.com/simrenbasra/Email_Genie.git
cd Email_Genie
```

### Create & Activate a Virtual Environment

```bash
conda env create -f environment.yml -n email_genie
conda activate email_genie
```

A requirements.txt file is also included for deployment if Conda is not available.
To install dependencies via pip:


```bash
pip install -r requirements.txt
```

### Running the web app

Navigate to folder`email_genie` and run `python app/app.py`

To run this you need:

1). OpenAI key

    - create file `API_key.env` with Open AI key
    - add to folder `app`

2). Data files 

    - all uploaded to my Google Drive [here]()
    - add to folder `app`

## Project Directory

```text
Email_Genie
 ├── email_genie/         # Web application
 ├── notebooks/           # Exploratory research + findings
 ├── data/                # Processed Enron dataset + vector index (too large to commit)
 ├── requirements.txt
 └── README.md
 ```