from os import path
from process_video import make_audio_path, vtoa
from upload_to_gcloud import upload_to_gcloud
from google.cloud import speech
from diarization_file import make_diarization_file as md_file
from raw_text_file import make_raw_text_file as mr_file


def transcribe_gcs(mp4_file):
    audio_file_path = make_audio_path(mp4_file)  # Create audio file
    vtoa(mp4_file)

    if audio_file_path:
        bucket_name = 'bucket_stt'  # Your gcloud bucket name
        audio_file_name = path.basename(audio_file_path) + '.wav'
        upload_to_gcloud(bucket_name, source_file_name=audio_file_path + ".wav", destination_blob_name=audio_file_name)

        """Asynchronously transcribes the audio file specified by the gcs_uri."""

        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(
            uri="gs://" + bucket_name + "/" + audio_file_name)

        drz_config = speech.SpeakerDiarizationConfig(
            enable_speaker_diarization=True
            # min_speaker_count = 2,
            # max_speaker_count = 6
        )

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code='en-US',
            audio_channel_count=2,
            enable_word_time_offsets=True,
            diarization_config=drz_config
        )
        operation = client.long_running_recognize(config=config, audio=audio)

        if not operation.done():
            print('Waiting for results...')

        md_file(audio_file_path, operation)
        mr_file(audio_file_path, operation)

    else:
        return
