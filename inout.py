'''
import pyttsx3
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',190)
'''
def ret(text):
    '''
    engine.say(text) 
    engine.runAndWait()
    print(text)
    '''
    print(text)
import colorama
def git():                            #Replace contents of git with whatever you want!
    it=input(colorama.Fore.YELLOW+'>: ')  
    print(colorama.Style.RESET_ALL)
    return it
