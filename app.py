import warnings
from flask import Flask, render_template, request, send_file
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
        global FILENAME, TEXTFILENAME
        FILENAME = f.filename
        TEXTFILENAME = FILENAME.replace(".mp4", ".txt")

        # If file is not .mp4
        if ".mp4" not in FILENAME:
            return render_template('error.html')

        f.save('./static/upload_files/' + secure_filename(FILENAME))
        speech_file = os.path.join('static/upload_files', secure_filename(FILENAME))
        googleAPI.transcribe_gcs(speech_file)

    return render_template('HTMLPage1.html', file_name=FILENAME)


'''완료----------------------------------------------------------------------------------------------------'''


@app.route("/OriginPage")
def origin():
    text = open('./static/text_files/{}'.format(TEXTFILENAME), mode='rt', encoding='utf-8')
    text = text.read()

    return render_template('OriginPage.html', data=text)


@app.route('/originpage_download', methods=["GET", "POST"])
def origin_down():
    origin_file = "static/text_files/{}".format(TEXTFILENAME)
    return send_file(origin_file, attachment_filename=os.path.basename(origin_file),
                     as_attachment=True)


@app.route("/SummaryPage")
def summary():
    # 텍스트 변수에 받아오기
    text = open('./static/text_files/{}'.format(TEXTFILENAME), mode='rt', encoding='utf-8')
    text = text.read()
    model = Summarizer('distilbert-base-uncased')
    resp = model(text)

    # make summary txt
    with open('static/text_files/{}'.format(TEXTFILENAME.replace('.txt', '_summary.txt')), 'w') as txt_file:
        txt_file.write(resp)

    return render_template('SummaryPage.html', data=resp)


@app.route('/summarypage_download', methods=["GET", "POST"])
def summary_down():
    summary_file = "static/text_files/{}".format(TEXTFILENAME.replace('.txt', '_summary.txt'))
    return send_file(summary_file, attachment_filename=os.path.basename(summary_file),
                     as_attachment=True)


@app.route("/NERPage")
def ner():
    # 텍스트 변수에 받아오기
    text = open('./static/text_files/{}'.format(TEXTFILENAME), mode='rt', encoding='utf-8')
    ner_visualize(text)
    text.close()
    return render_template('SpacyPage.html')


if __name__ == "__main__":
    app.run()
