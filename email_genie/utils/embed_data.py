import numpy as np
import pandas as pd
import re
from email.parser import Parser
from bs4 import BeautifulSoup
import spacy
from sentence_transformers import SentenceTransformer

class EmailEmbedder():
    def __init__(self, model=None):
        if model is None:
            self.model = SentenceTransformer("all-mpnet-base-v2")
        else:
            self.model = model

    def chunk_email(self, email, chunk_size=100, overlap=50):
        """Splits an email into chunks of a given size with a given overlap."""
        chunks = []
        words = email.split()
        step = chunk_size - overlap
        # Split email into chunks
        for i in range(0, len(words), step):
            chunk = words[i:i+chunk_size]
            chunked_email = ' '.join(chunk)
            chunks.append(chunked_email)

        return chunks

    def embed(self, cleaned_emails_df):
        chunked_emails = []
        original_email_index = []

        for index, email in enumerate(cleaned_emails_df['all_text']):
            chunks = self.chunk_email(email)
            chunked_emails.extend(chunks)
            original_email_index.extend([index] * len(chunks))
        
        embeddings = self.model.encode(
            chunked_emails,
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True
        )
        
        return embeddings, original_email_index
