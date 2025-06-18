import openai
from config import OPENAI_API_KEY
from utils.loader import load_successful_calls
from utils.prompts import build_prompt

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_sales_script():
    call_transcripts = load_successful_calls("call_data/successful_calls.txt")
    prompt = build_prompt(call_transcripts)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1800
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    script = generate_sales_script()
    print(script)
