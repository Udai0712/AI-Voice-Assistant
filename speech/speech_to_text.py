import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper

# ---------------- SETTINGS ---------------- #

SAMPLE_RATE = 16000
CHANNELS = 1

CHUNK_DURATION = 0.5          # seconds
SILENCE_TIMEOUT = 5           # stop after 5 sec silence
SILENCE_THRESHOLD = 300       # microphone sensitivity

# ---------------- LOAD WHISPER ---------------- #

print("🔄 Loading Whisper model...")
model = whisper.load_model("small")
print("✅ Whisper model loaded!")

# ---------------- RECORD ---------------- #

def record_audio(filename="audio.wav"):

    print("🎤 Speak now...")

    frames = []

    silence = 0

    while True:

        chunk = sd.rec(
            int(CHUNK_DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="int16"
        )

        sd.wait()

        frames.append(chunk)

        volume = np.abs(chunk).mean()

        if volume < SILENCE_THRESHOLD:

            silence += CHUNK_DURATION

        else:

            silence = 0

        if silence >= SILENCE_TIMEOUT:

            break

    audio = np.concatenate(frames, axis=0)

    write(filename, SAMPLE_RATE, audio)

    print("✅ Recording Complete")

    return filename

# ---------------- SPEECH TO TEXT ---------------- #

def speech_to_text(filename):

    result = model.transcribe(
        filename,
        language="en",
        fp16=False
    )

    return result["text"].strip()