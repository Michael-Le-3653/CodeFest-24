import speech_recognition as sr
import pyaudio
from gptmodel import main


transcript = ""
init_rec = sr.Recognizer()
print("Let's speak!!")
with sr.Microphone() as source:
    audio_data = init_rec.record(source, duration=5)
    print("Recognizing your text.............")
    text = init_rec.recognize_google(audio_data)
    transcript = text

print(transcript)
main(transcript)