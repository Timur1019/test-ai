from idea_generator.gpt_idea import generate_idea
from script_writer.text_script import generate_script
from video_creator.runway_api import create_video
from publisher.zapier_publish import publish_video
from utils.logger import log_step

def run_pipeline(trend: str):
    log_step("1. Генерация идеи")
    idea = generate_idea(trend)
    print("🧠 Идея:", idea)

    log_step("2. Генерация сценария")
    script = generate_script(idea)
    print("📜 Сценарий:", script)

    log_step("3. Генерация видео")
    video_url = create_video(script)
    print("🎥 Видео создано:", video_url)

    log_step("4. Публикация")
    success = publish_video(video_url, caption=idea)
    print("✅ Опубликовано:", success)

if __name__ == "__main__":
    run_pipeline("тенденции в продуктивности")
