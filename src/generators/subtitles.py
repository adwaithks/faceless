import pysrt
from src.constants import SUBTITLE_DIR

def create_subtitles(script, audio_durations):
    output_file = SUBTITLE_DIR + "subtitles.srt"
    subs = pysrt.SubRipFile()

    current_time = 0  # start at 0 seconds
    for idx, (text, duration) in enumerate(zip(script, audio_durations)):
        start_time = current_time
        end_time = current_time + duration

        # Convert seconds into SRT format
        start_srt = pysrt.SubRipTime(seconds=start_time)
        end_srt = pysrt.SubRipTime(seconds=end_time)

        sub = pysrt.SubRipItem(index=idx + 1, start=start_srt, end=end_srt, text=text)
        subs.append(sub)

        # Update current time for next subtitle
        current_time = end_time

    subs.save(output_file)
    return output_file

