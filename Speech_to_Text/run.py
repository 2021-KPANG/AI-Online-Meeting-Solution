from goog import transcribe_gcs

# File Upload (connect with backend)
PATH_mp4 = "/path/"
speech_file = PATH_mp4 + "/.mp4"
#speech_file = PATH_mp4 + "meeting_text.mp4"


# Runs transcription for each file inside the specified directory
def run(mp4_file):
    transcribe_gcs(mp4_file)


run(speech_file)
