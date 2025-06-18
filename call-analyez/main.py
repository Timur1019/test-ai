from transcriber import transcribe_audio
from analyzer import analyze_call

def main():
    print("📞 AI Sales Call Analyzer\n")

    choice = input("Выберите режим (1 - анализ текста, 2 - анализ .mp3): ")

    if choice == "1":
        print("\nВведите или вставьте текст звонка (Enter + Ctrl+D для завершения):\n")
        text = ""
        try:
            while True:
                line = input()
                text += line + "\n"
        except EOFError:
            pass
    elif choice == "2":
        file_path = input("Введите путь к .mp3 файлу (например: call.mp3): ").strip()
        text = transcribe_audio(file_path)
        print("\n🎙️ Распознанный текст:\n", text)
    else:
        print("❌ Неверный выбор.")
        return

    print("\n🧠 Анализ звонка:")
    analysis = analyze_call(text)
    print(analysis)


if __name__ == "__main__":
    main()
