# 🎤 AI Voice Assistant

An AI-powered Voice Assistant built using Streamlit and Google's Gemini API. The assistant supports speech-to-text, conversational AI, and text-to-speech for natural voice interactions.

## Features

- 🎙️ Speech-to-Text
- 🤖 Gemini AI Integration
- 🔊 Text-to-Speech
- 💬 Conversation Memory
- 🌐 Streamlit Web Interface

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- SpeechRecognition
- gTTS / pyttsx3
- python-dotenv

## Installation

```bash
git clone https://github.com/Udai0712/AI-Voice-Assistant.git
cd AI-Voice-Assistant

python -m venv venv

source venv/bin/activate   # macOS/Linux
# or
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

## Project Structure

```
Voice-AI-Assistant/
├── app.py
├── speech/
├── llm/
├── utils/
├── assets/
├── requirements.txt
└── README.md
```

## Author

**Udai Kiran**
