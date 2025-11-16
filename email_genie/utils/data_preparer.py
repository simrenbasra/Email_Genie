import numpy as np
import pandas as pd
import re
import email
from email.parser import Parser
from bs4 import BeautifulSoup
import spacy
import re


class DataPreparer():
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_data_from_row(self, row):
        raw_email = row['message']
        parser = Parser()

        my_email = parser.parsestr(raw_email)

        # dict to hold email info
        email_info = {}

        # extracing info from email header
        email_info['from'] = my_email.get('From')

        if my_email.get('To'):
            email_info['to'] = my_email.get('To')
        else:
            email_info['to'] = my_email.get('X-To')

        email_info['subject']= my_email.get('Subject')
        
        # Extracting body of email (main content)
        if my_email.is_multipart():
            # if email has multiple parts, body of the email can be in any one of these parts.
            body = ""
            # iterate over a list of parts in the email
            for part in my_email.get_payload():
                # to extract content of each part
                body += part.get_payload()
            # using strip to remvoe whitespaces
            email_info['body'] = body.strip()
        else:
            # else retrieve content
            email_info['body'] = my_email.get_payload().strip()

        return email_info

    def clean_email_with_soup(self, text):
        """
        Description: 
            Clean email data to address noise such as HTML tags, email addresses, phone numbers, files, etc.

        Input:
            Raw email data for a single email.

        Output:
            Cleaned email data for a single email.
        """
        # Use BeautifulSoup to remove all HTML tags
        if '>' in text or  '<' in text:
            soup = BeautifulSoup(text, 'html.parser')
            text = soup.get_text()

        # Remove text headers (forwarded by/original message, from, to, subject, sent)
        text = re.sub(r'[-\s]?(Forwarded by|Original Message)(\s*.*?)?[-\s]+', '', text)
        text = re.sub(r'From:.*?(\n|$)', '', text)
        text = re.sub(r'To:.*?(\n|$)', '', text)
        text = re.sub(r'Subject:.*?(\n|$)', '', text)
        text = re.sub(r'Sent:.*?(\n|$)', '', text)

        # Remove text addresses and phone numbers 
        text = re.sub(r'\S+@\S+', '', text)
        text = re.sub(r'(\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}', '', text)

        # Remove files and filepaths
        text = re.sub(r'\b[\w.-]+(?:\.(?:docx?|xlsx?|pdf|txt|html|zip|rar|png|jpe?g|gif))\b', '', text)
        text = re.sub(r'[\w]*FilePath\S*', '', text)   
        
        # Remove web addresses
        text = re.sub(r'http[s]?://\S+|www\.\S+', '', text)

        # Remove disclaimer patterns
        disclaimer_patterns = [
            r"This e-mail message may contain legally privileged.*",
            r"If you are not the intended recipient.*",
            r"Any dissemination, distribution or copying.*",
            r"CONFIDENTIALITY NOTICE:.*",
            r"VIRUS WARNING:.*",
            r"This e-mail is the property of.*",
            r"<<depsum\d+>>"  # placeholders like <<depsum11.28>>
        ]
        for p in disclaimer_patterns:
            text = re.sub(p, '', text, flags=re.DOTALL|re.IGNORECASE)

        # Remove promotional and ad language
        promo_patterns = [
            r'(?i)(unsubscribe|opt-out|sent from|advertisement|sponsored by).*',
            r'(?i)(free\s+(trial|issue|gift|offer|camera|subscription)|limited\s+time\s+offer|act\s+now|subscribe\s+now|you\s+have\s+been\s+selected).*',
            r'(?i)(save\s+up\s+to|absolutely\s+free|most\s+authoritative|exclusive\s+offer).*',
            r'(?i)(click\s+here|call\s+now|follow\s+the\s+link|order\s+now|subscribe\s+today).*',
            r'(?i)(this\s+email\s+was\s+sent\s+to|view\s+in\s+browser|privacy\s+policy).*',
            r'(?i)\b(image|img)\b.*'
        ]
        for pattern in promo_patterns:
            text = re.sub(pattern, '', text)


        # Remove non-alphanumeric symbols except for spaces
        text = re.sub(r'[^\w\s]|_', '', text)
    
        # Remove non-ASCII characters
        text = re.sub(r'[^\x00-\x7F]+', '', text)

        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text

    def remove_names(self,text):
        nlp = spacy.load('en_core_web_sm')
        text = str(text)
        doc = nlp(text)
        for e in reversed(doc.ents):
            if e.label_ in ("PERSON", "ORG", "DATE",): 
                text = text[:e.start_char] + text[e.start_char + len(e.text):]

        return text
    
    def normalize_text(self, text):
        """
        Lowercase and remove punctuation
        """
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text


    def is_risky(self, email_text):
        """
        Check if email contains risky/explicit words
        """
        risky_words = [
            "porn", "xxx", "sex", "nude", "erotic", "fetish", "adult", 
            "nsfw", "hardcore", "escort", "explicit", "18+", "sexual"
        ]
        text = self.normalize_text(email_text)
        for word in risky_words:
            if word in text:
                return True
        return False