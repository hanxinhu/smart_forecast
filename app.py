from flask import Flask
from flask import request, make_response, url_for, redirect, send_file, send_from_directory
import json
from flask_cors import CORS
import os
import sys
root_path = os.path.split(os.path.realpath(sys.argv[0]))[0];

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/init')
def hello_world():
    f = open(root_path+'/config.json')
    string = f.readlines()
    s = "".join([i.strip() for i in string])
    return s


@app.route('/file')
def get_file():
    return send_file('static/img.png', mimetype='png')


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()
