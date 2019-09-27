import pyttsx3 
  
# initialisation 
engine = pyttsx3.init() 
def ret(text):
    engine.say(text) 
    engine.runAndWait()
