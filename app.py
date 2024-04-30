from flask import Flask,request,jsonify,abort
import os
app = Flask(__name__)

UPLOAD_BUCKED = 'files_uploaded'
app.config['UPLOAD_FOLDER'] = UPLOAD_BUCKED

if not os.path.exists(UPLOAD_BUCKED):
    os.mkdir(UPLOAD_BUCKED)
    
@app.route('/upload',methods=['POST'])
def upload():
    try:
        if 'file' not in request.files or not request.files or request.files['file'] == '':
            print(f'---file sent {request.files}')
            return jsonify({"message":"No file was found in the previous request"}),401
        file = request.files['file']
        print(f"the file sent was ", file)
        return jsonify({"message":"successfully done"})
    except Exception as e : 
        return jsonify({"message":e})
    
if __name__ == "__main__":
    app.run(debug=True,port=7888)