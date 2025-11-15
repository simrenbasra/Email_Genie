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
conda create -n email_genie python=3.10 -y
conda activate email_genie
```

### Install dependencies

`pip install -r requirements.txt`

### Running the web app

Navigate to folder`email_genie` and run `python app.py`

## Project Directory

Email_Genie
 ├── email_genie/         # Main application
 ├── notebooks/           # Exploratory research + findings
 ├── data/                # Processed Enron dataset + vector index
 ├── requirements.txt
 └── README.md