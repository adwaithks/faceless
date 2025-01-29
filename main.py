from src.generators.audio import (
    trim_audio,
    generate_audio,
    get_audio_duration,
    merge_audio_files,
)
from src.generators.subtitles import create_subtitles, generate_subtitles_from_script
from src.generators.image import (
    create_video_from_image,
    generate_image,
    get_images_duration_in_video,
)
from src.generators.video import (
    add_background_music,
    merge_videos,
    burn_subtitle_to_video,
    generate_vide_wo_bg_music,
)
from src.constants import (
    OUTPUT_DIR,
    AUDIO_DIR,
    IMAGE_DIR,
    VIDEO_DIR,
    SUBTITLE_DIR,
    OTHER_DIR,
    ASSETS_DIR,
)
from dotenv import load_dotenv
from openai import OpenAI
import requests
from pydub import AudioSegment
import pysrt
import time
from io import BytesIO
from pathlib import Path
import subprocess
import os
import shutil

load_dotenv()


def create_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    return OpenAI(api_key=api_key)


def create_directories():
    directories = [AUDIO_DIR, IMAGE_DIR, VIDEO_DIR, SUBTITLE_DIR, OTHER_DIR]

    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory)


def get_script_and_subtitles():
    script_path = ASSETS_DIR + "script.txt"
    subtitle_path = ASSETS_DIR + "subtitles.txt"
    with open(script_path, "r") as script:
        script_lines = [
            line.strip().lower() for line in script.readlines() if line.strip()
        ]

    with open(subtitle_path, "r") as subtitles:
        subtitles = [
            line.strip().lower() for line in subtitles.readlines() if line.strip()
        ]

    return [script_lines, subtitles]


def main():
    client = create_openai_client()
    [script, subtitles] = get_script_and_subtitles()
    print(script)
    print(subtitles)
    create_directories()

    audio_durations = []
    audio_file_paths = []
    image_paths = []
    image_in_video_paths = []

    for index, text in enumerate(subtitles):
        audio_file_path = generate_audio(text, index + 1, client)
        duration = get_audio_duration(audio_file_path)
        audio_durations.append(duration)
        audio_file_paths.append(audio_file_path)

    subtitle_path = create_subtitles(subtitles, audio_durations)

    merged_audio_path = merge_audio_files(audio_file_paths)

    for index, text in enumerate(script):
        image_path = generate_image(text, index + 1, script, client)
        image_paths.append(str(image_path))

    image_durations = get_images_duration_in_video(script, subtitles, audio_durations)
    for index, image_path in enumerate(image_paths):
        image_in_video_path = create_video_from_image(
            image_path, image_durations[index], index + 1
        )
        image_in_video_paths.append(image_in_video_path)

    merged_video_path = merge_videos(image_in_video_paths)

    subtitled_video_path = burn_subtitle_to_video(merged_video_path, subtitle_path)

    final_out_wo_music = generate_vide_wo_bg_music(
        subtitled_video_path, merged_audio_path
    )

    start_time = input("Enter the start time (HH:MM:SS): ")
    duration = sum(audio_durations)

    trimmed_audio = trim_audio(start_time, duration)

    final_out_w_music = add_background_music(final_out_wo_music, trimmed_audio)

    print(f"Final video created successfully! Check the {final_out_w_music} file.")


if __name__ == "__main__":
    main()
