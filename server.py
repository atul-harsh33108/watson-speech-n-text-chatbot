from flask import Flask, render_template, request
from flask_cors import CORS
import json
import base64
import os
from worker import speech_to_text, text_to_speech, gemini_process_message

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    print("processing speech-to-text")
    audio_binary = request.data
    text = speech_to_text(audio_binary)
    response = app.response_class(
        response=json.dumps({'text': text}),
        status=200,
        mimetype='application/json'
    )
    print(response.data)
    return response

@app.route('/process-message', methods=['POST'])
def process_message_route():
    user_message = request.json['userMessage']
    print('user_message', user_message)
    voice = request.json['voice']
    print('voice', voice)
    gemini_response_text = gemini_process_message(user_message)
    gemini_response_text = os.linesep.join([s for s in gemini_response_text.splitlines() if s])
    gemini_response_speech = text_to_speech(gemini_response_text, voice)
    gemini_response_speech = base64.b64encode(gemini_response_speech).decode('utf-8')
    response = app.response_class(
        response=json.dumps({"openaiResponseText": gemini_response_text, "openaiResponseSpeech": gemini_response_speech}),
        status=200,
        mimetype='application/json'
    )
    print(response)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)