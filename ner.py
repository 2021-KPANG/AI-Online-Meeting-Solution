import os
import spacy
from spacy import displacy
import warnings
warnings.filterwarnings("ignore")


def ner_visualize(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    html = displacy.render(doc, style="ent", page=False)

    with open('templates/SpacyPage.html', 'a') as html_file:
        html_file.write(html)
    return doc

