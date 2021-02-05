<Speech_to_Text>

[Architecture]
1. File Upload(.mp4)
  * run.py

2. Convert /.mp4 to /.wav
  * process_video.py
    - use moviepy
  
3. Upload Google Cloud Storage
  * goog.py
    - Files of 1 minute or longer play time 
    - Save to Google Cloud Stoarge bucket, upload it
  
4. Google Speech_to_Text API
  * goog.py  
  
5. File Output
  * diarization.py
    - Make Speech_to_Text + Speech Diarization file
  * raw_text_file.py
    - Make only Speech_to_Text file
    
6. Run
  * run.py


[In Progress]
1. requirements.txt
  - 이것저것 깔아보면서 하느라 폴더안에 정리를 다 못했습니다..!!
  
2. Code comments
