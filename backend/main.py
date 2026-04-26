import os
from moviepy.editor import ColorClip

def create_video(text: str, filename="video.mp4"):
    print("🔥 create_video() STARTED")

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, "output")

    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, filename)

    print("📁 Saving to:", output_path)

    clip = ColorClip(size=(1080, 1080), color=(255, 0, 0), duration=3)

    clip.write_videofile(output_path, fps=24)

    clip.close()

    print("✅ VIDEO CREATED SUCCESSFULLY")

    return output_path
