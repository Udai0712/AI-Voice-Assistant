import time
import streamlit as st

from speech.speech_to_text import record_audio, speech_to_text
from speech.text_to_speech import speak
from llm.gemini import get_gemini_response, clear_memory

# ---------------------- PAGE CONFIG ----------------------

st.set_page_config(
    page_title="AI Voice Assistant",
    page_icon="🎤",
    layout="wide"
)

# ---------------------- CUSTOM CSS ----------------------

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#4CAF50;
}

.sub-title{
    text-align:center;
    color:gray;
    font-size:18px;
    margin-bottom:25px;
}

.stButton>button{
    width:100%;
    height:55px;
    font-size:18px;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------- SESSION ----------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------- SIDEBAR ----------------------

with st.sidebar:

    st.title("⚙️ Settings")
    st.info("🎤 Auto-stop after 5 seconds of silence")
    st.divider()

    st.success("✅ Groq Connected")
    st.success("✅ Whisper Loaded")

    st.metric("🎤 Speech Model", "Whisper Small")
    st.metric("🤖 LLM", "Llama 3.3 70B")
    st.metric("⚡ Status", "Online")
    st.metric("💬 Messages", len(st.session_state.messages))

    st.divider()

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages.clear()

        clear_memory()

        st.success("Conversation Cleared!")

        st.rerun()

# ---------------------- HEADER ----------------------

st.markdown(
    '<p class="main-title">🤖 AI Voice Assistant</p>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="sub-title">
    🎤 Speak Naturally • 🤖 AI Thinks • 🔊 Voice Responds
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------------- EMPTY STATE ----------------------

if len(st.session_state.messages) == 0:

    st.info(
        "👋 Welcome! Click **🎤 Start Recording** and ask me anything."
    )

# ---------------------- CHAT HISTORY ----------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# ---------------------- RECORD BUTTON ----------------------

if st.button("🎤 Start Recording", use_container_width=True):

    try:

        # ---------------------- LISTENING ----------------------

        listening = st.empty()

        listening.image(
            "assets/listening.gif",
            width=180
        )

        audio_file = record_audio()

        listening.empty()
        # ---------------------- SPEECH TO TEXT ----------------------

        user_text = speech_to_text(audio_file)

        if user_text.strip() == "":

            st.warning("No speech detected.")

            st.stop()

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_text
            }
        )

        with st.chat_message("user"):

            st.markdown(user_text)

        # ---------------------- THINKING ----------------------

        thinking = st.empty()

        thinking.image(
            "assets/thinking.gif",
            width=180
        )

        start = time.time()

        answer = get_gemini_response(user_text)

        elapsed = round(time.time() - start, 2)

        thinking.empty()

        # ---------------------- SPEAKING ----------------------

        speaking = st.empty()

        speaking.image(
            "assets/speaking.gif",
            width=180
        )

        speak(answer)

        speaking.empty()

        # ---------------------- STREAM RESPONSE ----------------------

        with st.chat_message("assistant"):

            placeholder = st.empty()

            streamed = ""

            for word in answer.split():

                streamed += word + " "

                placeholder.markdown(streamed + "▌")

                time.sleep(0.03)

            placeholder.markdown(streamed)

            st.caption(f"⚡ Response Time : {elapsed} sec")

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:

        st.error(f"❌ Error : {e}")

# ---------------------- DOWNLOAD CHAT ----------------------

chat = ""

for msg in st.session_state.messages:

    chat += f"{msg['role'].upper()}:\n"

    chat += msg["content"]

    chat += "\n\n"

st.sidebar.download_button(
    "📄 Download Chat",
    chat,
    file_name="conversation.txt",
    mime="text/plain"
)

# ---------------------- FOOTER ----------------------

st.divider()

st.markdown(
    """
    <center>

    ❤️ Built with Streamlit • Whisper • Groq • Llama 3.3

    </center>
    """,
    unsafe_allow_html=True
)