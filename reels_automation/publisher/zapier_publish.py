import requests
from config import ZAPIER_WEBHOOK_URL

def publish_video(video_url: str, caption: str = ""):
    payload = {
        "video_url": video_url,
        "caption": caption
    }
    response = requests.post(ZAPIER_WEBHOOK_URL, json=payload)
    response.raise_for_status()
    return response.status_code == 200
