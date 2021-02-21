## <Speech_to_Text>

### [Architecture]
#### 1. File Upload(.mp4)
  * run.py

#### 2. Convert /.mp4 to /.wav
  * process_video.py
    - use moviepy
  
#### 3. Upload Google Cloud Storage
  * upload_to_gcloud.py
    - Files of 1 minute or longer play time should store in GCS bucket
    - Save to bucket(GCS), upload it
  
#### 4. Google Speech_to_Text API
  * goog.py  
  
#### 5. Write Text File
  * write_file.py(2 options)
    - Make Speech_to_Text + Speech Diarization file
    - Make only Speech_to_Text file
    
#### 6. Run
  * run.py



## Want to Use Google Speech-To-Text?
1. set up a Cloud Console Project
  - Create or select a **project**
  - Enable the **Speech-to-Text API** for that project
  - Create a **service account**
  - Download a **private key** as JSON
2.put your key file(.json) in path ```/static/key/```
3. Install and initialize the Cloud SDK
4. make Bucket in Cloud storage
5. Set your bucket_name, key in path ```/googleAPI.py``
```
In line 8,
BUCKET_NAME = "bucket_name"

In line 10,
MY_KEY = ".json"
```


Reference
https://cloud.google.com/speech-to-text/docs/quickstart-gcloud?hl=ko  
https://webnautes.tistory.com/1247  
https://cloud.google.com/speech-to-text/docs/async-recognize#speech_transcribe_async-python  
