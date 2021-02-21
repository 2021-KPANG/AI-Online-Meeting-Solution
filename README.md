#  Making MoM
![GitHub](https://img.shields.io/github/license/2021-KPANG/AI-Online-Meeting-Solution)
- ***Hire our 'Making MoM' solution as your third-party minute taking assistant!***  👩‍💻✔ 
![](https://github.com/2021-KPANG/AI-Online-Meeting-Solution/blob/main/image/MoM%20logo.JPG?raw=true)

![](https://github.com/2021-KPANG/AI-Online-Meeting-Solution/blob/main/image/Demo.gif?raw=true)

## Why should I use Making MoM?

![](https://github.com/2021-KPANG/AI-Online-Meeting-Solution/blob/main/image/why%20use.JPG?raw=true)

### We provide all-in-one service of :
- Professional Minute Taking ✒️
  - Objective, third-party minute taking for virtual and teleconference meetings.
- Transcriptional Services 📄
	- We provide not only the transcripts of whole meeting but also speaker diarized transcripts.
- Summarized Transcripts 🔆
   - Automatically summarized minutes into few sentences.
   - Beta version also provides speaker diarized summaries.
- Highlighted Minutes 📆
  - Visualize ```person's name```, ```organization```, ```time```, ```location```, ```number```, etc in your minutes and grasp essential information at once.
- Afterwards, everyone knows what was said, what was decided upon and who has to do what next!

## Requirements
```
pip install bert-extractive-summarizer
pip install spacy
pip install transformers==2.2.2
pip install neuralcoref
pip install googleAPI
pip install google.cloud.storage
pip install google.cloud.speech
python -m spacy download en_core_web_sm
pip install moviepy
pip install flask
pip install -U pip setuptools wheel
pip install -U spacy
```

- google ERROR
```
pip install --upgrade google.cloud.storage
pip install --upgrade google.cloud.speech
pip install google.cloud
python -m spacy download en_core_web_md

pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
pip install fastai==2.2.5
pip install ohmeow-blurr
pip install datasets

pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
```

## Environment
- Local Environment
  - If run in local environment, error may occur in *summarizer*
  - Edit ```sentence_handler.py``` in path ```../site-packages/summarizer``` as below

```
In line 10,
#self.nlp.add_pipe(self.nlp.create_pipe('sentencizer')) to
self.nlp.add_pipe("sentencizer")

In line 22,
#return [c.string.strip() for c in doc.sents if max_length > len(c.string.strip()) > min_length] to
return [c.text.strip() for c in doc.sents if max_length > len(c.text.strip()) > min_length]
```

## Contributors
Lim Sejin, Soyoung Cho, Hwaseung Jeon, Heeseung  An, Jiyeon Jang and  Jisuk Ryu

## License
```
Copyright 2021 KPANG.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
