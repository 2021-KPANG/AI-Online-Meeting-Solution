# AI Online Meeting Solution

## Requirements
```
pip install bert-extractive-summarizer
pip install spacy
pip install transformers==2.2.2
pip install neuralcoref
pip install googleAPI
pip install google.cloud
python -m spacy download en_core_web_md
pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
pip install fastai==2.2.5
pip install ohmeow-blurr
pip install datasets
```
## Environment
- Local Environment
  - If run in local environment, error may occur in *summarizer*
  - Edit ```sentence_handler.py``` in path ```../site-packages/summarizer``` as below

```
In line 10,
#self.nlp.add_pipe(self.nlp.create_pipe('sentencizer')) to
self.nlp.add_pipe("sentencizer")

In line 22
#return [c.string.strip() for c in doc.sents if max_length > len(c.string.strip()) > min_length] to
return [c.text.strip() for c in doc.sents if max_length > len(c.text.strip()) > min_length]
```
## Contributors
- To be updated

## License
```AI Online Meeting Solution``` project is licensed under the terms of the **Apache License 2.0.**  
Copyright KPANG. All Rights Reserved. 
