class command:
    '''Command class;
    allows the user to make their own commands for the AI
    '''
    def __init__(self,inp,function,response,description,name):
        self.inp=inp          #List of inputs that will trigger this command
        self.func=function    #Function that the command will run
        self.name=name
        self.description=description
        self.response=response#List of potential outputs for the AI to say once the command has been completed
commands=[]
#Example, shutdown command
import os

def shutdown():
    os.system('shutdown /s')

commands.append(command(['shutdown'],shutdown,['shutting down...','shutting down the system...'],"This will shutdown the user's computer","shutdown"))

#Example, open browser
import webbrowser
def openbrowser():
    webbrowser.open('google.com')
commands.append(command(['open browser','browser'],openbrowser,['opening...','opening browser...'],"This will open the user's browser","browser"))          
