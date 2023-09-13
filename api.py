import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/admin/Desktop/upload'
ALLOWED_EXTENSIONS = set(['png'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/media/upload', methods=['POST'])
def upload_media():
        if 'file' not in request.files:
            return jsonify({'Erro': 'Media não fornecida'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'Erro': 'Nem um arquivo selecionado'}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'Mensagem': 'Media enviada'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)