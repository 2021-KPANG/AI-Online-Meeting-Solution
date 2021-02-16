import os
import spacy
from spacy import displacy
import warnings

warnings.filterwarnings("ignore")


def ner_visualize(text):
    nlp = spacy.load("en_core_web_sm")
    text = text.read()
    doc = nlp(text)
    html = displacy.render(doc, style="ent", page=False)

    # DOWNLOAD
    # # make spacy.txt
    # with open('static/text_files/{}'.format(FILENAME.replace('.txt', '_spacy.txt')), 'w') as txt_file:
    #     txt_file.write(html)

    # make SpacyPage.html
    with open('templates/SpacyPage.html', 'w') as html_file:
        html_file.write('''{% extends "NERPage.html" %}{% block content %}''')
        html_file.write(html)
        html_file.write("{% endblock %}")
    return
