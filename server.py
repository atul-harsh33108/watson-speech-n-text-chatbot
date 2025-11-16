from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import base64
import os
from worker import gemini_process_message

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# ------------------------------------------------------------------
# NEW TEXT-CHAT ENDPOINT – this is what the front-end calls when you type
# ------------------------------------------------------------------
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('userMessage', '').strip()
    voice = data.get('voice', 'default')

    if not user_message:
        return jsonify({"openaiResponseText": "", "openaiResponseSpeech": ""})

    # 1. Get Gemini answer
    gemini_text = gemini_process_message(user_message)

    # 2. **DO NOT CALL text_to_speech** – we are in text mode
    audio_base64 = ""   # empty → front-end will not play audio

    return jsonify({
        "openaiResponseText": gemini_text,
        "openaiResponseSpeech": audio_base64
    })

# ------------------------------------------------------------------
# Keep the old routes (voice) – they will be used later when you enable STT/TTS
# ------------------------------------------------------------------
@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    print("processing speech-to-text")
    audio_binary = request.data
    from worker import speech_to_text
    text = speech_to_text(audio_binary)
    return jsonify({'text': text})

@app.route('/process-message', methods=['POST'])
def process_message_route():
    user_message = request.json['userMessage']
    voice = request.json.get('voice', 'default')
    gemini_response_text = gemini_process_message(user_message)
    gemini_response_text = os.linesep.join([s for s in gemini_response_text.splitlines() if s])

    # Only run TTS if voice input was provided (i.e. audio file exists)
    audio_base64 = ""
    if request.files.get('audio'):
        from worker import text_to_speech
        speech_bytes = text_to_speech(gemini_response_text, voice)
        audio_base64 = base64.b64encode(speech_bytes).decode('utf-8')

    return jsonify({
        "openaiResponseText": gemini_response_text,
        "openaiResponseSpeech": audio_base64
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)