import moviepy.editor


def make_audio_path(video_file):
    def strip(text, suffix):  # Strip .mp4 suffix from file name
        if not text.endswith(suffix):
            return text
        # else
        return text[:len(text) - len(suffix)]

    stripped_name = strip(video_file, ".mp4")  # mp4없애기
    return stripped_name


# import moviepy.editor
def vtoa(video_file):
    video = moviepy.editor.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(make_audio_path(video_file) + ".wav")

# vtoa(speech_file)
