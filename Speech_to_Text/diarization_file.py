def make_diarization_file(audio_file_path, operation):
    dr_file = open(audio_file_path + '_drfile' + '.txt', 'w')
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
