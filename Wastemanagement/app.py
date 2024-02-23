from flask import Flask, render_template, request, redirect, url_for

import os


# Create Flask app instance
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define route for the home page
@app.route('/home')
def home_page():
    render_template('index.html')

@app.route('/')
def home():
    return render_template('index.html')

# Define route for another page
@app.route('/guide')
def guide():
    return render_template('guide.html')


@app.route('/waste_classify')
def aiclassify():
    return redirect('http://localhost:8503/')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
