from fastapi import FastAPI
from utils.video import create_video

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Video SaaS Running"}

@app.post("/generate-video")
def generate_video(text: str):
    path = create_video(text)

    return {
        "status": "success",
        "video_path": path
    }
