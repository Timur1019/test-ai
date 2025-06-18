def analyze_call(transcript: str) -> str:
    positive_signals = [
        "удобно говорить", "можно попробовать", "давайте", "интересно", "готов", "назначим встречу"
    ]
    negative_signals = [
        "не интересно", "нет времени", "не подходит", "дорого", "уже пользуемся"
    ]

    positives = [line for line in transcript.lower().splitlines() if any(p in line for p in positive_signals)]
    negatives = [line for line in transcript.lower().splitlines() if any(n in line for n in negative_signals)]

    result = []

    result.append(f"👍 Найдено позитивных сигналов: {len(positives)}")
    for p in positives:
        result.append(f"   ✅ {p.strip()}")

    result.append(f"\n⚠️ Найдено негативных сигналов: {len(negatives)}")
    for n in negatives:
        result.append(f"   ❌ {n.strip()}")


    recommendations = []
    if len(negatives) > 0:
        recommendations.append("Уточняйте возражения клиента, предложите альтернативу.")
    if len(positives) == 0:
        recommendations.append("Попробуйте добавить больше вовлечения и вопросов.")
    if "вручную" in transcript.lower():
        recommendations.append("Предложите преимущества автоматизации более конкретно.")

    result.append("\n📌 Рекомендации:")
    for r in recommendations or ["Диалог выглядит хорошо, рекомендаций нет."]:
        result.append(f"   💡 {r}")

    return "\n".join(result)
