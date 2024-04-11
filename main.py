from flask import Flask, render_template, request
from werkzeug import exceptions
import config
import os


root_dir = config.locate_root_folder(__file__)
template_folder = config.locate_template_folder(root_dir, "template")

app = Flask(__name__, template_folder=template_folder)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    files = request.files
    return f"{files['file'].read()}"


@app.errorhandler(exceptions.BadRequestKeyError)
def handle_no_file_uploaded(e: exceptions.BadRequestKeyError):
    return f"Загрузите файл"

if __name__ == "__main__":
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.run(host="0.0.0.0", port=3000, debug=True)
