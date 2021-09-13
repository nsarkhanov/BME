from gtts import gTTS, lang
import playsound
import os

start_sound_text='Hello , My name is BeME. I will assit you during my life time. First I want to know your name. Please  touch the dive one time then say your name'

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "output.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)






















# engine = pyttsx3.init()

# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 110) 

# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id) 

# engine.say("I will speak this text")
# engine.runAndWait()
# engine.stop()
# # """ RATE"""
# #     # setting up new voice rate


# """VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()


# """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# # engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()