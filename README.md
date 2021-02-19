# AI Online Meeting Solution

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

In line 22
#return [c.string.strip() for c in doc.sents if max_length > len(c.string.strip()) > min_length] to
return [c.text.strip() for c in doc.sents if max_length > len(c.text.strip()) > min_length]
```

## Contributors
- To be updated

## License
```AI Online Meeting Solution``` project is licensed under the terms of the **Apache License 2.0.**  
Copyright KPANG. All Rights Reserved. 

## Feature
- To be updated

