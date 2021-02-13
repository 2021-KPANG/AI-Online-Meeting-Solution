import warnings
import os
from flask import Flask, render_template
from ner import ner_visualize
warnings.filterwarnings("ignore")

app = Flask(__name__)


@app.route("/")
def start_page():
    file = 'templates/NERPage.html'
    if os.path.isfile(file):
        os.remove(file)
    return render_template('StartPage.html')


@app.route("/page1")
def html_page():
    return render_template('HTMLPage1.html')


@app.route("/OriginPage")
def origin():
    return render_template('OriginPage.html')


@app.route("/SummaryPage")
def summary():
    return render_template('SummaryPage.html')


@app.route("/NERPage")
def ner():
    ner_visualize()
    return render_template('NERPage.html')


if __name__ == "__main__":
    app.run()

