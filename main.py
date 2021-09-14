from typing import runtime_checkable
from cv2 import sepFilter2D
import model 
import speach_model
import time 
text0='Hello , My name is BeME. I will assit you during my life time. First I want to know your name. Please  touch the device one time then say your name'
text1="nice to meet you Nurlan"
text2="I will call you friend"
text3="when you need my help, just touch device."
text_process="my friend ,  now I will explain my working principles  to understand me.when you  touch device i take  photo with camera of device then detect object on photo fro you."
text4="I am happy with you"
res=model.object_detector()

def setup_function():
    speach_model.speak(text0)
    time.sleep(1)
    time.sleep(1)
    speach_model.speak(text1)
    time.sleep(1)
    speach_model.speak(text2)
    time.sleep(1)
    speach_model.speak(text_process)
    time.sleep(1)
    speach_model.speak(text3)
    time.sleep(1)
    speach_model.speak(text4)
print(res)
time.sleep(1)


setup_function()

def RunApp():
    count=len(res)
    if count>1:
        speach_model.speak("My friend,")
        while count>1:
            
            for k , v in res.items():
                
                if count>1:
                    speach_model.speak(f"I have detected {v} {k}")
                if count==1:
                    speach_model.speak(f" and , {v} {k}")
                count-=1

    elif count==1:
        for k , v in res.items():
            speach_model.speak(f"I have detected {v} {k}")       
    else:
         speach_model.speak('Sorry ,my friend,I cant detect anything')

RunApp()