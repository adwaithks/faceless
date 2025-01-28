import subprocess
from src.constants import VIDEO_DIR, OTHER_DIR
import os

def burn_subtitle_to_video(video_path, subtitle_path):
    output_file = VIDEO_DIR + "video_with_subtitles.mp4"
    command = f"""ffmpeg -i {video_path} -vf "subtitles={subtitle_path}:force_style='Fontname=Arial Black,Fontsize=15,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=1,Shadow=1,MarginV=90,BorderStyle=1,BorderWidth=1'" {output_file}"""
    subprocess.run(command, shell=True)
    return output_file


def merge_videos(video_paths):
    output_file = VIDEO_DIR + "merged_video.mp4"
    file_list = OTHER_DIR + "file_list.txt"
    with open(file_list, "w") as f:
        for path in video_paths:
            f.write(f"file '../../{path}'\n")
    try:
        command = f"""ffmpeg -f concat -safe 0 -i {file_list} -c copy -v debug -y {output_file}"""
        subprocess.run(command, shell=True, check=True)
        print(f"Videos merged successfully. Saved to {output_file}")
        return output_file
    except Exception as e:
        print(e)
        raise "err"


def generate_vide_wo_bg_music(subtitled_video, merged_audio):
    output_file = VIDEO_DIR + "final_video_wo_music.mp4"
    command = f"""ffmpeg -i {subtitled_video} -i {merged_audio} -c:v copy -c:a aac -shortest {output_file}"""
    subprocess.run(command, shell=True)
    print(f"Final video created. Saved to {output_file}")
    return output_file

def add_background_music(video_file_path, background_music_path):
    output_file = VIDEO_DIR + "final_video_with_music.mp4"
    command = f"""ffmpeg -i {video_file_path} -i {background_music_path} -filter_complex "[1:a]volume=0.3[a1];[0:a][a1]amix=inputs=2:duration=first:dropout_transition=3[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k {output_file}"""
    subprocess.run(command, shell=True)
    print(f"Background music added. Saved to {output_file}")
    return output_file

def burn_subtitle_to_video(video_path, subtitle_path):
    output_file = VIDEO_DIR + "video_with_subtitles.mp4"
    command = f"""ffmpeg -i {video_path} -vf "subtitles={subtitle_path}:force_style='Fontname=Arial Black,Fontsize=15,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=1,Shadow=1,MarginV=90,BorderStyle=1,BorderWidth=1'" {output_file}"""
    subprocess.run(command, shell=True)
    print(f"Subtitles generated. Saved to {output_file}")
    return output_file

