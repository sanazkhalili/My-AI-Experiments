from database import crud
import re

def normalize_persian(text: str):
    text = text.replace('ي', 'ی').replace('ك', 'ک')
    text = re.sub(r'[\u064B-\u065F\u0670]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

client = crud.create_db()
collection = crud.create_collection(client, 'rules')
collection_info = crud.create_collection(client, 'rules_info')
