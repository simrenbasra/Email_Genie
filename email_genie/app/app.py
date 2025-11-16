from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import joblib
import faiss
import html
import re
from sentence_transformers import SentenceTransformer, CrossEncoder
import nltk
from nltk.corpus import wordnet, stopwords
import quopri
from openai import OpenAI
from dotenv import load_dotenv
import os

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = set(stopwords.words('english'))
email_stop_words = {
    "e-mail", "email", "subject", "re", "fwd", "fw", 
    "hi", "hello", "thanks", "thank", "regard", "regards", 
    "cc", "bcc", "from", "to"
}
stop_words.update(email_stop_words)

app = Flask(__name__)

## Load env vars (api key)
load_dotenv(dotenv_path="API_key.env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# load data and embeddings
emails = pd.read_csv('cleaned_emails.csv')
embeddings = joblib.load('EXT_embeddings_chunked.pkl')
original_email_index = joblib.load('EXT_original_email_index.pkl')

# set up vector db
embedding_dim = embeddings.shape[1]
IVF_index = faiss.IndexIVFFlat(faiss.IndexFlatIP(embedding_dim), embedding_dim, 50, faiss.METRIC_INNER_PRODUCT)
IVF_index.train(embeddings)
IVF_index.add(embeddings)

# load embedding model
embedding_model = SentenceTransformer("all-mpnet-base-v2")

# functions
def embed_query(query):
    return embedding_model.encode([query], convert_to_numpy=True, normalize_embeddings=True)

def get_related_words(term):
    related = set()
    for syn in wordnet.synsets(term):
        for lemma in syn.lemmas():
            related.add(lemma.name().replace("_", " "))
    return related

def clean_email_text(raw_text):
    if not raw_text:
        return ""
    if isinstance(raw_text, str):
        raw_text = raw_text.encode('utf-8', errors='ignore')
    decoded = quopri.decodestring(raw_text).decode('utf-8', errors='ignore')
    decoded = decoded.replace('\r\n', '\n').replace('\r', '\n')
    cleaned = re.sub(r'\n{3,}', '\n\n', decoded)
    return cleaned.strip()

def llm_enhance_query(query):
    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt = f"""
    You are a helpful assistant that expands search queries for email retrieval. 
    Take the user's query and rewrite it to include related terms, synonyms, and context that would help find all relevant emails.
    Focus strictly on terms semantically related to the original query.
    Original query: "{query}"
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a search query enhancement assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return query

def llm_summarise_email(email_text, query):
    client = OpenAI(api_key=OPENAI_API_KEY)
    email_text = email_text or ""
    prompt = f"""
    Summarise this email in 3-5 concise bullet points, highlighting only information relevant to the search query: {query}
    Keep each bullet short (1-2 sentences max).

    Email text:
    {email_text}
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes emails into concise bullet points."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "Summary unavailable."

# flask 
@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    query = ""

    if request.method == "POST":
        query = request.form.get("query", "")
        top_n = int(request.form.get("top_n", 5))
        rerank_n = int(request.form.get("rerank_n", 50))

        enhanced_query = llm_enhance_query(query)

        # Embed query & search FAISS
        query_vec = embed_query(enhanced_query)
        distances, indices = IVF_index.search(query_vec, rerank_n)

        # De-duplicate and collect candidates
        candidate_emails = []
        seen_ids = set()
        if indices.size > 0:
            for idx in indices[0]:
                if idx < len(original_email_index):
                    email_id = original_email_index[idx]
                    if email_id not in seen_ids:
                        candidate_emails.append(emails.iloc[email_id])
                        seen_ids.add(email_id)

        if len(distances[0]) > 0:
            scores = distances[0]
            if scores.max() != scores.min():
                norm_scores = (scores - scores.min()) / (scores.max() - scores.min())
            else:
                norm_scores = np.ones_like(scores)
        else:
            norm_scores = []

        sorted_emails = [
            row for _, row in sorted(zip(norm_scores, candidate_emails), key=lambda x: x[0], reverse=True)
        ]
        sorted_scores = sorted(norm_scores, reverse=True)

        for row, score in zip(sorted_emails[:top_n], sorted_scores[:top_n]):
            body_text = row['body'] if pd.notna(row['body']) else ""
            summary = llm_summarise_email(body_text, enhanced_query).replace('\n', '<br>')
            results.append({
                "subject": row['subject'],
                "summary": summary,
                "body": body_text.replace('\n', '<br>'),
                "score": float(score)
            })

    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
