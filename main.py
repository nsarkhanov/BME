from cv2 import sepFilter2D
import model 
import speach_model
import time 
start_sound_text='Hello , My name is BeME. I will assit you during my life time. First I want to know your name. Please  touch the device one time then say your name'

res=model.object_detector()
speach_model.speak(start_sound_text)
print(res)
time.sleep(3)
# print("My friend,I have detected {} {} and ".format(**res)) 
# objcets=res.keys().to
# numb_object=res.values()
# print(objcets,numb_object)
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
         speach_model.speak('Sorry ,my friend, I cant detect anything')

RunApp()