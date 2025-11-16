# import os
# import requests
# import base64
# from dotenv import load_dotenv
# import google.generativeai as genai  # Correct import for google-generativeai package

# load_dotenv()

# # Configure Gemini API
# genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# def speech_to_text(audio_binary):
#     base_url = os.getenv('WATSON_STT_URL')
#     api_url = f"{base_url}/v1/recognize"
#     params = {'model': 'en-US_Multimedia'}
    
#     # Basic Auth for IBM Watson
#     apikey = os.getenv('WATSON_STT_API_KEY')
#     auth_header = 'Basic ' + base64.b64encode(f"apikey:{apikey}".encode('utf-8')).decode('utf-8')
#     headers = {'Authorization': auth_header}
    
#     response = requests.post(api_url, params=params, data=audio_binary, headers=headers).json()
#     text = 'null'
#     if response.get('results'):
#         print('speech to text response:', response)
#         text = response['results'].pop()['alternatives'].pop()['transcript']
#         print('recognised text: ', text)
#     return text

# def text_to_speech(text, voice=""):
#     base_url = os.getenv('WATSON_TTS_URL')
#     api_url = f"{base_url}/v1/synthesize"
#     if voice and voice != "default":
#         api_url += f"?voice={voice}"
    
#     # Basic Auth for IBM Watson
#     apikey = os.getenv('WATSON_TTS_API_KEY')
#     auth_header = 'Basic ' + base64.b64encode(f"apikey:{apikey}".encode('utf-8')).decode('utf-8')
    
#     headers = {
#         'Accept': 'audio/wav',
#         'Content-Type': 'application/json',
#         'Authorization': auth_header
#     }
#     json_data = {'text': text}
#     response = requests.post(api_url, headers=headers, json=json_data)
#     print('text to speech response:', response)
#     return response.content

# def gemini_process_message(user_message):
#     # Initialize Gemini model
#     model = genai.GenerativeModel('gemini-1.5-flash')
#     prompt = "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations."
#     try:
#         response = model.generate_content(prompt + "\n\n" + user_message)
#         print("gemini response:", response.text)
#         return response.text
#     except Exception as e:
#         print(f"Gemini error: {e}")
#         return "Error processing message with Gemini API."


import os
import requests
import base64
import google.generativeai as genai
from dotenv import load_dotenv

# CRITICAL FIX: Tell dotenv exactly where .env is
load_dotenv(dotenv_path='/opt/chatbot/.env')

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def gemini_process_message(user_message):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations."
    try:
        response = model.generate_content(prompt + "\n\n" + user_message)
        return response.text.strip()
    except Exception as e:
        print(f"Gemini error: {e}")
        return "Sorry, I couldn't process that."

def speech_to_text(audio_binary):
    # STUB – voice not enabled yet
    return ""

def text_to_speech(text, voice=""):
    # STUB – voice not enabled yet
    return b''   # empty bytes

def gemini_process_message(user_message):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations."
    try:
        response = model.generate_content(prompt + "\n\n" + user_message)
        return response.text.strip()
    except Exception as e:
        print(f"Gemini error: {e}")
        return "Sorry, I couldn't process that."