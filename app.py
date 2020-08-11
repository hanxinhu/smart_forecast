from flask import Flask
from flask import request, make_response, url_for, redirect, send_file, send_from_directory
import json
from flask_cors import CORS
import os
import sys
import subprocess
import logging

root_path = os.path.split(os.path.realpath(sys.argv[0]))[0]

app = Flask(__name__, static_folder=root_path + '/static')
CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/init')
def hello_world():
    f = open(root_path + '/config.json', encoding='utf-8')
    print('config path : ' + root_path + '/config.json')
    string = f.readlines()
    s = "".join([i.strip() for i in string])
    return s


@app.route('/file')
def get_file():
    return send_file(root_path + '/resource/img.png', mimetype='png')


@app.route('/file1')
def get_file1():
    return send_file(root_path + '/resource/img1.png', mimetype='png')


@app.route('/run', methods=['GET', 'POST'])
def run_script():
    #request.form. 默认是form-data格式 json格式需要用下面的代码
    s = request.get_data(as_text=True)
    obj = json.loads(s)
    subprocess.call('bash {} {}'.format(obj.get('name'), ",".join(obj.get('params'))), shell=True)
    return obj.get('name')

if __name__ == '__main__':
    app.run(debug=True)
