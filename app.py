import stat

from flask import Flask
from flask import request, make_response, url_for, redirect, send_file, send_from_directory
import json
from flask_cors import CORS
import os
import sys
import subprocess
import logging
import base64

root_path = os.path.split(os.path.realpath(sys.argv[0]))[0]
logging.info("root_path: " + root_path)
app = Flask(__name__, static_folder=root_path + '/static')
CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/init')
def hello_world():
    f = open(root_path + '/config/smart_forecast.json', encoding='utf-8')
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
    # request.form. 默认是form-data格式 json格式需要用下面的代码
    s = request.get_data(as_text=True)
    obj = json.loads(s)
    params = obj.get('params')
    target = obj.get('target')
    target_file = root_path + target.format(*params)
    temp_file = target_file + '.txt'


    print(target_file)
    print(temp_file)
    print(params)
    os.system('touch {}'.format(temp_file))
    print('sh {} {}'.format(obj.get('name'), " ".join(params)))
    subprocess.call('sh {} {}'.format(obj.get('name'), " ".join(params)), shell=True)
    return obj.get('name')


@app.route('/get_result', methods=['POST'])
def get_result():
    s = request.get_data(as_text=True)
    obj = json.loads(s)
    target = obj.get('target')
    params = obj.get('params')
    target_file = root_path + target.format(*params)
    print(target)
    print(target_file)
    temp_file = target_file + '.txt'
    if os.path.exists(target_file):
        f = open(target_file, 'rb')
        res = str(base64.b64encode(f.read()))
        return 'data:image/png;base64,' + res[2:-1]
    elif os.path.exists(temp_file):
        return '正在计算结果，请等待片刻再次尝试'
    else:
        return '请先点击确认'


if __name__ == '__main__':
    app.run(debug=True)
