import subprocess
from pathlib import Path
import requests
from src.constants import IMAGE_DIR, VIDEO_DIR

def generate_image(text, index, script, client):
    script_str = "".join(script)
    prompt = f"""story: {script_str}. Now Generate an image that resonates with the sentence: '{text}'. The image should be realistic and look very close to real day to day life."""
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url

    # Save the image to a file
    image_file_name = f"image-{index}.png"
    image_file_path = IMAGE_DIR + image_file_name
    image_data = requests.get(image_url).content

    with open(image_file_path, "wb") as image_file:
        image_file.write(image_data)

    print(f"Image file '{image_file_name}' created successfully!")
    return image_file_path


def create_video_from_image(image_path, duration, index=1):
    output_file = VIDEO_DIR + f"image_video-{index}.mp4"
    command = f"""ffmpeg -loop 1 -i {image_path} -c:v libx264 -t {duration} -vf \
"zoompan=z='zoom+0.00025':s=1080x1920:d=360,scale=1080x1920:force_original_aspect_ratio=increase,crop=1080:1920" \
-pix_fmt yuv420p -r 30 {output_file}"""
    subprocess.run(command, shell=True)
    print(f"Video created for {image_path}. Saved to {output_file}")
    return output_file


def get_images_duration_in_video(script, subtitles, audio_durations):
        subtitle_index = 0
        script_index = 0
        duration = 0
        prev_duration = 0
        image_durations_in_video = []

        while subtitle_index < len(subtitles) and script_index < len(script):
            if subtitles[subtitle_index].lower() in script[script_index].lower():
                duration += audio_durations[subtitle_index]
                subtitle_index += 1
            else:
                image_durations_in_video.append(duration)
                duration = 0
                script_index += 1

        if duration > 0:
            image_durations_in_video.append(duration)

        return image_durations_in_video