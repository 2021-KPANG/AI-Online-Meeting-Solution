import os
from google.cloud import speech
from google.cloud import storage
import moviepy.editor
# from write_file import make_diarization_file as md_file, make_raw_text_file as mr_file

def make_diarization_file(text_file_path,filename, operation):
    text_file_name = filename.replace(".mp4", "_drfile.txt")
    text_file_name = os.path.join(text_file_path , text_file_name)
    dr_file = open(text_file_name, 'w')

    response = operation.result(timeout=10000)
    result = response.results[-1]
    words_info = result.alternatives[0].words

    tag = 1
    speaker = ""

    for word_info in words_info:
        if word_info.speaker_tag == tag:
            speaker = speaker + " " + word_info.word
        else:
            transcript = "speaker {}: {}".format(tag, speaker)
            dr_file.write(transcript + '\n')
            tag = word_info.speaker_tag
            speaker = "" + word_info.word
    transcript = "speaker {}: {}".format(tag, speaker)
    dr_file.write(transcript + '\n')
    dr_file.close()


def make_raw_text_file(text_file_path, filename, operation):
    result = operation.result()
    results = result.results

    text_file_name = filename.replace(".mp4", ".txt")
    text_file_name = os.path.join(text_file_path, text_file_name)
    rt_file = open(text_file_name, 'w')
    for result in results:
        for alternative in result.alternatives:
            rt_file.write(alternative.transcript + '\n')
    rt_file.close()


# video -> audio
def vtoa(video_file):
    video = moviepy.editor.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(video_file.replace(".mp4",".wav"))

# uploads compressed audio to gcloud bucket
def upload_to_gcloud(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # storage_client = storage.Client()
    storage_client = storage.Client.from_service_account_json("./static/key/summer-avenue-303505-46ae2f2fd326.json")

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


def transcribe_gcs(mp4_file):
    filename = os.path.basename(mp4_file)
    file_path = 'static/upload_files'  # Create audio file
    vtoa(mp4_file)

    if file_path:
        bucket_name = 'bucket_stt'  # Your gcloud bucket name
        audio_file_name = filename.replace(".mp4", ".wav")
        upload_to_gcloud(bucket_name,
                         source_file_name=os.path.join(file_path, audio_file_name),
                         destination_blob_name=audio_file_name)

        """Asynchronously transcribes the audio file specified by the gcs_uri."""

        # client = speech.SpeechClient()
        client = speech.SpeechClient.from_service_account_json("./static/key/summer-avenue-303505-46ae2f2fd326.json")

        # bucket에서 오디오 파일가져오기 (파일형식 : gs://~)
        audio = speech.RecognitionAudio(
            uri="gs://" + bucket_name + "/" + audio_file_name)

        # diarization parameter(화자분할_베타)
        drz_config = speech.SpeakerDiarizationConfig(
            enable_speaker_diarization=True
            # min_speaker_count = 2,
            # max_speaker_count = 6
        )

        ''' 
        speech_context parameter(음성적응: 자주 인식해야 하는 단어 주의해서 변환)
        focus on 'TIME' phrase during speech to text
        '''
        # speech_context = speech.SpeechContext(phrases=["$TIME"])

        # config parameter
        config = speech.RecognitionConfig(
            # .WAV 지원 인코딩
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            # Select language
            language_code='en-US',
            audio_channel_count=2,
            enable_word_time_offsets=True,
            diarization_config=drz_config,
            model = "video",

            # automatic punctuation
            enable_automatic_punctuation=True,

            # speech_contexts=[speech_context],
        )

        operation = client.long_running_recognize(config=config, audio=audio)
        if not operation.done():
            print('Waiting for results...')

        text_file_path = './static/text_files'
        # make_diarization_file(text_file_path, filename, operation)
        make_raw_text_file(text_file_path, filename, operation)

    else:
        print("no audio file!")
        return