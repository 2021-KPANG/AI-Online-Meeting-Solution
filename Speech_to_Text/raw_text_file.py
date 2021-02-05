def make_raw_text_file(audio_file_path, operation):
    result = operation.result()
    results = result.results

    rt_file = open(audio_file_path + '_rtfile' + '.txt', 'w')
    for result in results:
        for alternative in result.alternatives:
            rt_file.write(alternative.transcript + '\n')
    rt_file.close()
