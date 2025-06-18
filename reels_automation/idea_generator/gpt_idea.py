import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_idea(trend: str) -> str:
    prompt = f"Предложи идею для короткого видео (Reels), основываясь на тренде: '{trend}'."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=100
    )
    return response["choices"][0]["message"]["content"].strip()
