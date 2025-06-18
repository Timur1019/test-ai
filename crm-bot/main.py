from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME
from crm_loader import load_crm_data
from prompts import build_prompt

client = OpenAI(api_key=OPENAI_API_KEY)

def get_ai_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

def main():
    try:
        client_id = int(input("Введите ID клиента (1–5): "))
    except ValueError:
        print("⚠️ Введите корректный ID (целое число).")
        return

    crm = load_crm_data("crm_data.json", client_id)
    if not crm:
        print("[Ошибка] Нет CRM-данных. Завершение.")
        return

    print(f"🤖 Добро пожаловать, {crm.get('name')}! Чем могу помочь?")
    while True:
        user_input = input("Клиент: ").strip()
        if user_input.lower() in {"выход", "exit", "quit"}:
            print("🤖 Завершение сессии.")
            break

        prompt = build_prompt(crm, user_input)
        reply = get_ai_response(prompt)
        print(f"ИИ-продажник: {reply}\n")

if __name__ == "__main__":
    main()
