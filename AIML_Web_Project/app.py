from flask import Flask, render_template, request
from utils.face_detect import detect_face
from utils.sentiment import analyze_sentiment
from utils.motion_tracking import motion_tracking
from utils.speech_to_text import speech_to_text
from utils.text_to_speech import text_to_audio
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/face', methods=['POST'])
def face():
    file = request.files['image']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    face_count = detect_face(path)
    return render_template('result.html', result=f"Faces Detected: {face_count}")

@app.route('/sentiment', methods=['POST'])
def sentiment():
    text = request.form['text']
    result = analyze_sentiment(text)
    return render_template('result.html', result=result)

@app.route('/speech')
def speech():
    text = speech_to_text()
    return render_template('result.html', result=text)

@app.route('/motion')
def motion():
    motion_tracking()
    return render_template('result.html', result="Motion Tracking Started (Press ESC to stop)")

@app.route('/text_to_audio', methods=['POST'])
def text_audio():
    text = request.form['audio_text']
    result = text_to_audio(text)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
