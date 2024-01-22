from flask import Flask,redirect,render_template,request
from regression_model import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)