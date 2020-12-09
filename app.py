#!/usr/bin/python

import time
from flask import Flask,render_template
app = Flask(__name__)

START = time.time()


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080)
