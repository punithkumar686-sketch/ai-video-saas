import requests
from config import ELEVEN_API_KEY

def generate_voice(text, output_path="outputs/voice.mp3"):
    url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"

    headers = {
        "xi-api-key": ELEVEN_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}
    }

    res = requests.post(url, json=data, headers=headers)

    with open(output_path, "wb") as f:
        f.write(res.content)

    return output_path
