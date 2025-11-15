import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

try:
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("Test message")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")