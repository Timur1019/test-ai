import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_script(idea: str) -> str:
    prompt = f"Напиши сценарий для короткого Reels-видео по идее: '{idea}'"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )
    return response["choices"][0]["message"]["content"].strip()
