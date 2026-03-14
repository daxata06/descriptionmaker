import requests
from dotenv import load_dotenv
import os

load_dotenv()

def analyze_text(text):

    prompt = f"""
    Проанализируй текст и верни результат строго в формате:

    Короткое описание услуги: (2-3 предложения)  
    Ключевые слова: (5 слов через запятую)
    Категория: (одно слово)

    Текст:
    {text}
    """

    payload = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 200
    }

    headers = {
        "Authorization": f"Bearer {os.getenv('API_KEY')}",
        "Content-Type": "application/json"
    }

    response = requests.post(os.getenv("URL"), headers=headers, json=payload)

    result = response.json()["choices"][0]["message"]["content"]

    return result

text = input("Введите текст:\n")       

result = analyze_text(text)

print("\nРезультат:\n")
print(result)