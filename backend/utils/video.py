import os
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip

OUTPUT_DIR = "output"

def create_video(text: str, filename="video.mp4"):
    # Step 1: ensure output folder exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Step 2: background
    bg = ColorClip(size=(1080, 1080), color=(0, 0, 0), duration=5)

    # Step 3: text clip
    txt = TextClip(
        text,
        fontsize=60,
        color="white",
        size=(1000, None),
        method="caption"
    ).set_duration(5).set_position("center")

    # Step 4: combine
    video = CompositeVideoClip([bg, txt])

    # Step 5: output path
    output_path = os.path.join(OUTPUT_DIR, filename)

    # Step 6: write file (IMPORTANT)
    video.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio=False
    )

    return output_path
