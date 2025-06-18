import requests
from config import RUNWAY_API_KEY

def create_video(script: str) -> str:
    # Пример запроса — структура зависит от Runway API
    payload = {
        "prompt": script,
        "motion": "slow zoom",
        "duration": 10
    }
    headers = {
        "Authorization": f"Bearer {RUNWAY_API_KEY}"
    }
    response = requests.post("https://api.runwayml.com/v1/video", json=payload, headers=headers)
    response.raise_for_status()
    return response.json().get("video_url")
