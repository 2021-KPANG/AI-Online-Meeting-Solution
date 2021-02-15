import warnings
from flask import Flask, render_template, request
from ner import ner_visualize
from werkzeug.utils import secure_filename
from summarizer import Summarizer
import os
import googleAPI

warnings.filterwarnings("ignore")
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def start_page():
    return render_template('StartPage.html')


@app.route("/page1", methods=['GET', 'POST'])
def html_page():
    if request.method == 'POST':
        f = request.files['file']
        global FILENAME
        FILENAME = f.filename

        # If file is not .mp4
        if ".mp4" not in FILENAME:
            return render_template('error.html')

        f.save('./static/upload_files/' + secure_filename(FILENAME))
        speech_file = os.path.join('static/upload_files', secure_filename(FILENAME))
        googleAPI.transcribe_gcs(speech_file)

    return render_template('HTMLPage1.html')

'''완료----------------------------------------------------------------------------------------------------'''

@app.route("/OriginPage")
def origin():
    text = open('./static/text_files/{}'.format(FILENAME.replace("mp4","txt")), mode='rt', encoding='utf-8')
    text = text.read()

    return render_template('OriginPage.html', data=text)


@app.route("/SummaryPage")
def summary():
    # 텍스트 변수에 받아오기
    text = open('./static/text_files/{}'.format(FILENAME.replace("mp4","txt")), mode='rt', encoding='utf-8')
    text = text.read()
    model = Summarizer('distilbert-base-uncased')
    resp = model(text)

    return render_template('SummaryPage.html', data=resp)



@app.route("/NERPage")
def ner():
    # 텍스트 변수에 받아오기
    text = open('./static/text_files/{}'.format(FILENAME.replace("mp4", "txt")), mode='rt', encoding='utf-8')
    ner_visualize(text)
    return render_template('NERPage.html')




if __name__ == "__main__":
    app.run()
