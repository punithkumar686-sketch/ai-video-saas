from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip, ColorClip
import os

def create_video(script_text, audio_path, output_path="outputs/video.mp4"):

    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Load audio
    audio = AudioFileClip(audio_path)

    # Background (black screen)
    bg = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=audio.duration)

    # Text overlay
    txt = TextClip(
        script_text,
        fontsize=60,
        color='white',
        size=(1000, None),
        method='caption'
    ).set_duration(audio.duration).set_position('center')

    # Combine video layers
    video = CompositeVideoClip([bg, txt])

    # Add audio
    video = video.set_audio(audio)

    # Export video
    video.write_videofile(output_path, fps=24)

    return output_path
