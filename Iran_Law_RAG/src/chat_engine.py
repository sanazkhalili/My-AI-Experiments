import requests
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))
import src.config as config
from src.utils import collection, collection_info

def call_llm(user_message, system_message):
    payload = {
        "model": config.LLM_MODEL,
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(config.URL, headers=config.HEADER, json=payload)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code}\n{response.text}")

    result = response.json()
    return result["choices"][0]["message"]["content"]


def chat_with_model(user_message):
    from database.create_embeddings import get_similar_answer, get_similar_info

    class_question = get_classify(user_message)
    print(class_question)
    
    if class_question == "content_question":
        system_message= config.RAG_PROMPT +f"{user_message}"
        info_sim = get_similar_answer(collection, user_message)
        return call_llm(info_sim, system_message)
    
    elif class_question=="Iran_main_rule":
        system_message= config.RAG_PROMPT +f"{user_message}"
        info_sim = get_similar_info(collection_info, user_message)
        return call_llm(info_sim, system_message)
    
    else:
        return config.OUT_LIER_RESPONSE

        
def get_classify(user_question):
    return call_llm(user_question, config.CLASSIFY_PROMPT)
    

def get_summary_data(info):
    return call_llm(info, config.SUMMARY_PROMPT)



