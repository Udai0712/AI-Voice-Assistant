# 🎙️ AI Voice Assistant

A real-time **Audio-In, Audio-Out Conversational AI Assistant** built using Python and Streamlit. The assistant accepts voice input, converts speech to text using Whisper, generates intelligent responses using the Groq API (Llama 3.3 70B Versatile), and responds with natural voice output using Piper Text-to-Speech.

---

## Features

- 🎤 Voice-based user interaction
- 📝 Speech-to-Text using Whisper
- 🤖 AI-powered conversation using Groq (Llama 3.3 70B Versatile)
- 🔊 Text-to-Speech using Piper
- 💬 Conversation memory
- ⏱️ Automatic silence detection for recording
- 📥 Download chat history
- 🎨 Interactive Streamlit interface with animations
- 🔄 Fallback responses during delays

---

## Tech Stack

- Python
- Streamlit
- OpenAI Whisper
- Groq API
- Llama 3.3 70B Versatile
- Piper Text-to-Speech
- NumPy
- SoundDevice
- SciPy
- python-dotenv

---

## 📂 Project Structure

```
Voice-AI-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── llm/
│   ├── gemini.py
│   └── memory.py
│
├── speech/
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── utils/
│
├── assets/
│   ├── listening.gif
│   ├── thinking.gif
│   └── speaking.gif
│
├── screenshots/
│
└── docs/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Voice-AI-Assistant.git
cd Voice-AI-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

### 5. Run the application

```bash
streamlit run app.py
```

---

## Workflow

```
User Voice
      │
      ▼
Speech Recording
      │
      ▼
Whisper Speech-to-Text
      │
      ▼
Conversation Memory
      │
      ▼
Groq (Llama 3.3 70B)
      │
      ▼
AI Response
      │
      ▼
Piper Text-to-Speech
      │
      ▼
Voice Output
```

---

## Key Features

- Fast conversational responses
- Natural voice interaction
- AI conversation memory
- Automatic silence detection
- Downloadable chat history
- User-friendly Streamlit interface

---

## 🤖 AI Usage

The following AI tools were used during the development of this project:

### ChatGPT

Used for:

- Code guidance
- Debugging
- Streamlit UI improvements
- Documentation
- README preparation
- Feature suggestions
- Project architecture

### Groq API

Used as the Large Language Model (LLM).

**Model**

- Llama 3.3 70B Versatile

Used for:

- Conversational AI
- Context-aware responses

### Whisper

Used for:

- Speech-to-Text conversion

### Piper

Used for:

- Text-to-Speech synthesis

---

## Future Enhancements

- Wake-word detection
- Offline speech recognition
- Multi-language support
- Emotion detection
- Calendar and email integration
- Smart home automation
- Web search capability

---

## Author

**Udai Kiran**


---

## License

This project was developed for educational and internship evaluation purposes.
