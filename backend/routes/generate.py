from fastapi import APIRouter
from services.llm import generate_script
from services.voice import generate_voice
from services.video import create_video

router = APIRouter()

@router.post("/generate")
def generate_video_api(topic: str):

    script = generate_script(topic)
    audio_path = generate_voice(script)
    video_path = create_video(script, audio_path)

    return {
        "status": "success",
        "script": script,
        "video": video_path
    }
