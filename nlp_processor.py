import spacy
from textblob import TextBlob

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Returns float: -1 (negative) to 1 (positive)

def recognize_intent(text):
    # Very basic intent recognition via keyword matching
    text = text.lower()
    if "time" in text:
        return "get_time"
    elif "date" in text:
        return "get_date"
    elif "google" in text:
        return "search_google"
    elif "joke" in text:
        return "tell_joke"
    else:
        return "unknown"
