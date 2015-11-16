from flask import Flask, render_template, request, session, redirect, url_for
import utils

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        line = request.form["line"]
        meme = request.form["meme"]
        final = utils.generate(line, meme)
        return render_template("response.html", image = final)
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.debug = True
    app.secret_key = utils.secret_key
    app.run('0.0.0.0', port=8000)
