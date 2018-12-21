from flask import Flask, render_template, send_from_directory, request, send_file
import os
import json


app = Flask(__name__)
app.config['basedir'] = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/sendfile', methods=['post'])
def returnfile():
    requestedFile = request.get_json()
    print(requestedFile)

    with open(os.path.join('static', 'gpf.DCM'), 'w') as f:
        newstr ='''
FESTWERT PFltSig_StMacPBasdB1.tiEfcDurnMin_C 
LANGNAME "" 
FUNKTION PFltSig_Coorr 
EINHEIT_W "s"
WERT '''+str(requestedFile['TT11'])+'''
END
'''
        f.write(newstr)
        f.close()
    if os.path.isfile(os.path.join('upload', 'gpf.DCM')):
        print('file exist~')
    print(os.path.join(app.config['basedir'],'upload'))
    directory = os.getcwd()
    return send_from_directory(directory,'gpf.DCM', as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)
    