from pydub import AudioSegment
from pathlib import Path
import subprocess
from src.constants import AUDIO_DIR

def trim_audio(audio_file_path, start_time, duration):
    output_file = AUDIO_DIR + "trimmed_audio.mp3"
    command = f"""ffmpeg -i {audio_file_path} -ss {start_time} -t {duration} {output_file}"""
    subprocess.run(command, shell=True)
    print(f"Audio trimmed successfully! Saved to {output_file}")
    return output_file

def merge_audio_files(audio_file_paths):
    output_file = AUDIO_DIR + "merged_audio.mp3"
    path_str = "|".join([str(path) for path in audio_file_paths])
    command = f"""ffmpeg -i "concat:{path_str}" -c copy {output_file}"""
    subprocess.run(command, shell=True)
    print(f"Audio files merged. Saved to {output_file}")
    return output_file

def get_audio_duration(audio_file_path):
    audio = AudioSegment.from_mp3(audio_file_path)
    duration_in_seconds = len(audio) / 1000.0

    return duration_in_seconds

def generate_audio(text, index, client):
    audio_file_name = "speech-" + str(index) + ".mp3"
    output_file = AUDIO_DIR + audio_file_name

    response = client.audio.speech.create(
        model="tts-1",
        voice="coral",
        input=text,
    )

    with open(output_file, "wb") as audio_file:
        audio_file.write(response.content)

    print(f"Audio file '{audio_file_name}' created successfully!")
    return output_file