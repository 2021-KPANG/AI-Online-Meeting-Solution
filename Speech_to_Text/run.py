from goog import transcribe_gcs

# File Upload (connect with backend)
PATH_mp4 = "C:\\Users\\cofls\\Desktop\\2021\\음성인식\\mp4\\"
PATH_mp3 = "C:\\Users\\cofls\\Desktop\\2021\\음성인식\\mp3\\"
speech_file = PATH_mp4 + "The_Expert__Progress_Meeting_(Short_Comedy_Sketch).mp4"


# speech_file = "/"

# Runs transcription for each file inside the specified directory
def run(mp4_file):
    transcribe_gcs(mp4_file)


run(speech_file)
