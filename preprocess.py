import re

def clean_noisy_text(raw_text):
    text = re.sub(r'\n+', '\n', raw_text)
    text = re.sub(r'\s{2,}', ' ', text)
    text = re.sub(r"[^\w\s\.,;:!?'\"()\-\u0900-\u097F]", '', text)
    return text.strip()