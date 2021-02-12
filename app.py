from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def startpage():
    return render_template('StartPage.html')

@app.route("/page1")
def HTMLPage() :
    return render_template('HTMLPage1.html')

if __name__ == "__main__":
    app.run()