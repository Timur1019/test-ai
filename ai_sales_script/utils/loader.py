def load_successful_calls(path):
    """
    Загружает успешные звонки из .txt файла.
    Каждое взаимодействие должно быть разделено через "---"
    """
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    return [call.strip() for call in content.split('---') if call.strip()]
