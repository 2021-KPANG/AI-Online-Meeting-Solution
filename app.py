# from ner import ner_visualize
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def start():
    return render_template("StartPage.html")


@app.route('/HTMLPage1.html')
def html_page():
    return render_template("HTMLPage1.html")
#

# @app.route('/ner')
# def ner():
#     return render_template("NERPage.html")
#
#

#
# @app.route('/ner')
# def ner():
#     ner_html = ner_visualize()
#     return ner_html


if __name__ == '__main__':
    app.run()