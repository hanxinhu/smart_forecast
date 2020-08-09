from flask import Flask
from flask import request, make_response, url_for, redirect, send_file, send_from_directory
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/init')
def hello_world():
    f = open('./static/test.json')
    string = f.readlines()
    s = "".join([i.strip() for i in string])
    return s


@app.route('/file')
def get_file():
    return send_file('img.png')


@app.after_request
def cors(environ):
    environ = make_response(environ)
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)
