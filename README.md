# Watson Speech and Text Chatbot  
  
A voice-enabled chatbot built with Flask, Google Gemini API, and IBM Watson Speech-to-Text (STT) and Text-to-Speech (TTS) services. Based on the Coursera guided project *Building a Voice Assistant with OpenAI and IBM Watson Speech Libraries*, modified to use Gemini instead of OpenAI.  
  
## Features  
- **Voice Input**: Converts spoken input to text using IBM Watson STT.  
- **Text Processing**: Generates responses using Google Gemini API (gemini-1.5-flash).  
- **Voice Output**: Converts responses to audio using IBM Watson TTS.  
- **Web Interface**: Interactive UI with text input, voice recording, and theme toggle (light/dark mode).  
- **Customizable**: Supports different Watson TTS voices (e.g., en-GB_CharlotteV3Voice).  
  
## Prerequisites  
- Python 3.13.3  
- Git  
- API keys for Google Gemini and IBM Watson (STT and TTS)  
- A modern web browser (e.g., Chrome, Firefox)  
  
## Setup  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/atul-harsh33108/watson-speech-n-text-chatbot.git  
   cd watson-speech-n-text-chatbot  
   ```  
2. **Create a Virtual Environment**:  
   ```bash  
   python -m venv venv  
   venv\Scripts\activate  # On Windows  
   ```  
3. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  
4. **Set Up Environment Variables**: Create a `.env` file in the project root with:  
   ```  
   GEMINI_API_KEY=your-gemini-api-key  
   WATSON_STT_API_KEY=your-watson-stt-key  
   WATSON_STT_URL=https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/your-instance-id  
   WATSON_TTS_API_KEY=your-watson-tts-key  
   WATSON_TTS_URL=https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/your-instance-id  
   ```  
   Replace `your-*-key` and `your-instance-id` with your actual API keys and instance IDs from Google AI Studio and IBM Cloud.  
5. **Run the Application**:  
   ```bash  
   python server.py  
   ```  
   Open `http://localhost:8000` in a browser.  
  
## Usage  
- **Text Input**: Type a question (e.g., "What is AI?") in the text box and press Enter.  
- **Voice Input**: Click the microphone button, speak clearly, and stop recording to see the transcribed text and hear the response.  
- **Voice Selection**: Choose a Watson TTS voice from the dropdown (e.g., en-GB_CharlotteV3Voice).  
- **Theme Toggle**: Switch between light and dark mode using the toggle button.  
  
## License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  
  
## Acknowledgments  
- Based on the Coursera guided project by IBM Developer Skills Network.  
- Uses Google Gemini API and IBM Watson STT/TTS services. 
