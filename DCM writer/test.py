from flask import g,Flask, render_template, send_from_directory, jsonify,request, send_file
import os
import json


app = Flask(__name__)
app.config['basedir'] = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_PATH']=os.path.join(app.root_path,'upload')
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/sendfile', methods=['POST'])
def returnfile():
    # requestedFile = request.get_json()
    # print(requestedFile)

#     with open(os.path.join('static', 'gpf.DCM'), 'w') as f:
#         newstr ='''
# FESTWERT PFltSig_StMacPBasdB1.tiEfcDurnMin_C 
# LANGNAME "" 
# FUNKTION PFltSig_Coorr 
# EINHEIT_W "s"
# WERT '''+str(requestedFile['TT11'])+'''
# END
# '''
#         f.write(newstr)
#         f.close()
    if os.path.isfile(os.path.join(app.config['UPLOAD_PATH'], 'gpf.txt')):
        print('文件存在')
        print(os.path.join(app.config['UPLOAD_PATH'], 'gpf.txt'))
    else:
        print('文件不存在')
      
    # print(os.path.join(app.config['basedir'],'upload'))
    # directory = os.path.join(os.getcwd(),'upload')
    dirpath = os.path.join(app.root_path,'upload')
    print("app.config['UPLOAD_PATH']=",app.config['UPLOAD_PATH'])
    return send_from_directory(dirpath,'gpf.txt', as_attachment=True)#, as_attachment=True

if __name__=='__main__':
    app.run(debug=True)
    