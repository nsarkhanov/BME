import speech_recognition as sr
import pyttsx3 as pt
import pyaudio
recognizer=sr.Recognizer()
key=0
# audio=pyaudio.PyAudio()
# print([audio.get_device_info_by_index(i) for i in range(audio.get_device_count())])


while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration=0.5)
            audio=recognizer.listen(mic)
            text=recognizer.recognize_google(audio)
            print(text)
    except sr.UnknownValueError():
        recognizer=sr.Recognizer()
        continue
  

