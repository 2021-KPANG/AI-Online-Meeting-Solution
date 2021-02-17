# AI Online Meeting Solution

## Requirements
```
pip install bert-extractive-summarizer
pip install spacy
pip install transformers==2.2.2
pip install neuralcoref
python -m spacy download en_core_web_md
```
## Environment
- Local Environment
  - If run in local environment, error may occur in *summarizer*
  - Edit ```sentence_handler.py``` in path ```../site-packages/summarizer``` as below

```
#self.nlp.add_pipe(self.nlp.create_pipe('sentencizer')) to
self.nlp.add_pipe("sentencizer")

#return [c.string.strip() for c in doc.sents if max_length > len(c.string.strip()) > min_length] to
return [c.text.strip() for c in doc.sents if max_length > len(c.text.strip()) > min_length]
```
