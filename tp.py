import speech_recognition as sr  
import os
from float import MainExe
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) #8 sec ke liye voice input lega woh
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")  #english me input ke liye en-US use hoga

    except:
        return ""    #kuch input nhi mila toh returns null
    
    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():
    queery = Listen().lower()
    
    if "wake up" in queery:
        print("Wake up detected.")
        MainExe()
        #os.startfile(r"C:\Users\preet\OneDrive\Desktop\Float\tp.py")
        
    else:
        pass
    
while True:
    WakeupDetected()