from os import path
from process_video import make_audio_path, vtoa
from upload_to_gcloud import upload_to_gcloud
from google.cloud import speech
from write_file import make_diarization_file as md_file, make_raw_text_file as mr_file


def transcribe_gcs(mp4_file):
    audio_file_path = make_audio_path(mp4_file)  # Create audio file
    vtoa(mp4_file) # video to audio : .mp4 -> .wav

    if audio_file_path:
        bucket_name = '/bucket_name_in_google_cloud'  # Your gcloud bucket name
        audio_file_name = path.basename(audio_file_path) + '.wav'
        upload_to_gcloud(bucket_name, source_file_name=audio_file_path + ".wav", destination_blob_name=audio_file_name)

        """Asynchronously transcribes the audio file specified by the gcs_uri."""
        
        client = speech.SpeechClient()
        
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
        #speech_context = speech.SpeechContext(phrases=["$TIME"])
        
        #config parameter
        config = speech.RecognitionConfig(
            # .WAV 지원 인코딩
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            # Select language
            language_code='en-US',
            audio_channel_count=2,
            enable_word_time_offsets=True,
            diarization_config=drz_config,
            
            # automatic punctuation
            enable_automatic_punctuation=True,
       
            # speech_contexts=[speech_context],
        )
        
        
        operation = client.long_running_recognize(config=config, audio=audio)
        if not operation.done():
            print('Waiting for results...')

        md_file(audio_file_path, operation)
        mr_file(audio_file_path, operation)

    else:
        print("no audio file!")
        return 
