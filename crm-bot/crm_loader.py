import json

def load_crm_data(filepath: str, client_id: int = 1) -> dict:
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            clients = data.get("clients", [])
            return next((c for c in clients if c["id"] == client_id), {})
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"[Ошибка] Не удалось загрузить CRM-данные: {e}")
        return {}
