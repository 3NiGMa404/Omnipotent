class command:
    '''Command class;
    allows the user to make their own commands for the AI
    '''
    def __init__(self,inp,function,response=''):
        self.inp=inp          #List
        self.func=function    #Function
        self.response=response#String
commands=[]
#Example, shutdown command
import os

def shutdown():
    os.system('shutdown /s')

commands.append(command(['shutdown'],shutdown,'shutting down...'))

#Example, open browser
import webbrowser
def openbrowser():
    webbrowser.open('google.com')
commands.append(command(['open browser','browser'],openbrowser,'opening...'))
                
