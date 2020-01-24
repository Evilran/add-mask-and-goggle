#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Name: server.py
Author: Evi1ran
Date Created: November 06, 2019
Description: None
'''

# built-in imports
import os
import re
import requests

# third-party imports
from flask import Flask
from flask import request
from flask import render_template
from datetime import timedelta
from add import add

app = Flask(__name__)
# Cancel image caching
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
ALLOWED_EXTENSIONS = set(['bmp', 'png', 'jpg', 'jpeg'])
UPLOAD_FOLDER=r'./cache/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/url', methods=['GET', 'POST'])
def url():
    if request.method == 'POST':
        url = request.form['url']
        mode = (int)(request.form['mask'])
        isGoggle = request.form.get('goggle')
        if re.match(r'^https?:/{2}\w.+$', url): 
            if allowed_file(url):
                filename = url.split('/')[-1]
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename) 
                r = requests.get(url)
                if r.status_code == 200:
                    c = r.content
                    if not c.startswith(b'<!DOCTYPE html>'):
                        with open(path, 'wb') as f:
                            f.write(c)
                        output = add(path, filename, mode, isGoggle)
                        return render_template('index.html', output = output)
                    else:
                        return render_template('index.html', alert = 'URL地址无法识别！')
                else:
                    return render_template('index.html', alert = 'URL地址不能访问！')
            else:
                return render_template('index.html', alert = 'URL地址不是图片！')
        else:
            return render_template('index.html', alert = 'URL格式错误！')

    else:
        return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        file = request.files['image']
        mode = (int)(request.form['mask'])
        isGoggle = request.form.get('goggle')
        if file and allowed_file(file.filename):
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            output = add(path, file.filename, mode, isGoggle)
            return render_template('index.html', output = output)
        else:
            return render_template('index.html', alert = '文件类型必须是图片！')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()