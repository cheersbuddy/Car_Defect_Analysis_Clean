from flask import Flask, flash, render_template, request, redirect, send_file, url_for, send_from_directory, Response, jsonify
from werkzeug.utils import secure_filename
from app import app, allowed_file
import os
import subprocess

@app.route('/')
@app.route('/home')
def home():
    return render_template('./home.html')


# image--------------------------------------------------------------------------------

@app.route('/image', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            process_uploaded_image(filename)
            detected_image_url = url_for('display', filename=filename)
            return jsonify({'success': True, 'detected_image_url': detected_image_url})
        else:
            flash('Allowed image types are -> jpg, jpeg, png, gif')
            return redirect(request.url)
    return render_template('image.html')

@app.route('/display/<filename>')
def display(filename):
    folder_path = 'runs/detect'
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    latest_subfolder = max(subfolders, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
    directory = os.path.join(folder_path, latest_subfolder)
    return send_from_directory(directory, filename)

def process_uploaded_image(filename):
    file_extension = filename.rsplit('.', 1)[1].lower()
    if file_extension in {'jpg', 'jpeg'}:
        process = subprocess.Popen(["python", "detect.py", '--source', os.path.join(app.config['UPLOAD_FOLDER'], filename), "--weights", "best.pt", "--class", "1",  "2"], shell=True)
        process.wait()
    elif file_extension == 'mp4':
        process = subprocess.Popen(["python", "detect.py", '--source', os.path.join(app.config['UPLOAD_FOLDER'], filename), "--weights", "best.pt", "--class", "1", "2"], shell=True)
        process.wait()


# analysis-----------------------------------------------------------------------------------

img = os.path.join('static', 'image')

@app.route('/analysis')
def analysis():
    file = os.path.join(img, 'Default.jpeg')
    return render_template('./analysis.html', image=file)

if __name__ == "__main__":
    app.run(debug=True)
     # debug=True causes Restarting with stat