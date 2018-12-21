from flask import Flask,render_template, request, url_for, jsonify,send_from_directory
import os
import json
import sys
import subprocess
from subprocess import call
from pprint import pprint
sys.path.append(r'C:\Users\li.gao\Desktop\手风琴')

sys.setrecursionlimit(5000)


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('1.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    
    # combine into a reasonable file
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(basedir, 'uploads')
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)  # if folder not existed, create one

    uploaded_files = request.files.getlist('myfile')     # 从表单的file字段获取文件，myfile为该表单的name值
    filenames = []

    #读取了mdf文件位置
    for f in uploaded_files:
        filename = f.filename
        f.save(os.path.join(file_dir, filename))    #保存文件到upload目录中
        filenames.append(os.path.join(file_dir, filename))
    jsdata = {
        'filelist': filenames
    }
    json_str = json.dumps(jsdata, indent=4)
    
    with open('filelist.json', 'w') as f:
        f.write(json_str)
    f.close()
    return render_template('1.html')

@app.route('/calc/read_cali_func',methods=['POST'])
def simu():
    aa=request.get_json()
    pprint(aa)
    return jsonify(aa)

@app.route('/calc/create_dcm',methods=['POST'])
def DCM_create():
    a=request.get_json()
    pprint(a)
    return render_template('1.html')
    









if __name__=='__main__':
    app.run(debug=True)