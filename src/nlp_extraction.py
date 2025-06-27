import re
import spacy

nlp = spacy.load("fr_core_news_sm")

def extract_metadata(text):
    date_pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    dates = re.findall(date_pattern, text)

    objet = ""
    objet_match = re.search(r"Objet\s*:\s*(.*)", text)
    if objet_match:
        objet = objet_match.group(1).strip()

    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        entities.setdefault(ent.label_, []).append(ent.text)

    return {
        "dates": dates,
        "subject": objet,
        "entities": entities
    }