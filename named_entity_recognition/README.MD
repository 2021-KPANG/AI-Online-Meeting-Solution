# Named Entity Recognition

![](https://blog.kakaocdn.net/dn/bXkbEO/btqzI4OQGLW/aORTJck8tI2ADkwDUGdWfk/img.png)

## What is NER?
- NER is a task of identifying and categorizing key information (entities) in text
- entity can be any word or series of words that consistently refers to the same thing
- Every detected entity is classified into a predetermined category

## Model
![](https://spacy.io/pipeline-fde48da9b43661abcdf62ab70a546d71.svg)
- This project utilizes current state-of-the-art transformer-based pipelines provided by ```spaCy```.
- ```spaCy``` features an extremely fast statistical entity recognition system, that assigns labels to contiguous spans of tokens.
- The default trained pipelines can indentify a variety of named and numeric entities, including companies, locations, organizations and products.
- Adding arbitrary classes to the entity recognition system and training with new examples are available, making this **AI Online Meeting Solution** service trainable for specific domainss

## Usage
```
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("KPMG International is the third-largest accounting firm in the world.
Headquartered in the Netherlands, KPMG provides accounting, consulting, tax and legal, financial advisory, and assurance services from more than 820 locations.
KPMG's member firms are located in more than 159 countries across the globe.")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
```

![](https://github.com/2021-KPANG/AI-Online-Meeting-Solution/blob/main/image/ner_example.JPG?raw=true)

## Model Performance
![](https://github.com/2021-KPANG/AI-Online-Meeting-Solution/blob/main/image/ner_performance_compare.JPG?raw=true)
- spaCy v3.0 introduces transformer-based pipelines that bring spaCy’s accuracy right up to current state-of-the-art.

![](https://github.com/2021-KPANG/AI-Online-Meeting-Solution/blob/main/image/ner_performance.JPG?raw=true)

## Reference
- [Performance Reference](https://spacy.io/usage/facts-figures)
- [Model Reference](https://spacy.io/usage/linguistic-features#named-entities)
- [Document Reference](https://medium.com/mysuperai/what-is-named-entity-recognition-ner-and-how-can-i-use-it-2b68cf6f545d)
