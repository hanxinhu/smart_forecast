from flask import Flask
from flask import request, url_for, redirect
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/hello')
def hello_world():
    f = open('./static/test.json')
    string = f.readlines()
    s = "".join([i.strip() for i in string])
    return s


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)
