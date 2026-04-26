from moviepy.editor import *
import os

def create_video(script_text, audio_path, output_path="outputs/video.mp4"):
    
    audio = AudioFileClip(audio_path)
    
    # Simple background (can upgrade to AI images later)
    bg = ColorClip(size=(1080, 1920), color=(0,0,0), duration=audio.duration)

    txt = TextClip(
        script_text,
        fontsize=60,
        color='white',
        size=(1000, None),
        method='caption'
    ).set_duration(audio.duration).set_position('center')

    video = CompositeVideoClip([bg, txt])
    video = video.set_audio(audio)

    video.write_videofile(output_path, fps=24)

    return output_path
