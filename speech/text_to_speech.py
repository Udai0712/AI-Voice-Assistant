from gtts import gTTS
import pygame
import os
import time


def speak(text):
    filename = "response.mp3"

    tts = gTTS(text=text, lang="en")
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()

    if os.path.exists(filename):
        os.remove(filename)