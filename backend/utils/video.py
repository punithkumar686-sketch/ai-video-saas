import os
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

def create_video(text: str, filename="video.mp4"):
    # ✅ ensure output folder exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_path = os.path.join(OUTPUT_DIR, filename)

    # 🟢 background
    bg = ColorClip(size=(1080, 1080), color=(0, 0, 0), duration=5)

    # 🟢 text
    txt = TextClip(
        text,
        fontsize=70,
        color="white",
        method="caption",
        size=(900, None)
    ).set_duration(5).set_position("center")

    # 🟢 combine
    video = CompositeVideoClip([bg, txt])

    # ⚠️ IMPORTANT: write file properly
    video.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio=False
    )

    video.close()

    return output_path
