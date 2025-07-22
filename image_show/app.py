import os
from werkzeug.utils import secure_filename
from flask import Flask, request, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1000

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_files():
    files = request.files.getlist('photos')

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

    flash('Files successfully uploaded!', 'success')
    return redirect(url_for('index'))


@app.route('/gallery')
def gallery():
    image_folder = app.config['UPLOAD_FOLDER']
    image_files = [f for f in os.listdir(image_folder) if allowed_file(f)]
    image_urls = [
        url_for('static', filename=f'uploads/{file}') for file in image_files]
    return render_template('gallery.html', images=image_urls)


if __name__ == '__main__':
    app.run(debug=True)
