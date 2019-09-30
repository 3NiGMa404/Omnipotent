# Omnipotent
*A chatbot in the making*
---------------------------
Omnipotent is a machine learning retrieval-based chatbot made in python 3, currently supporting windows 10 running python 3.6+

Usage
-----------------------------
To run the chatbot, please make sure you install all of the required modules with `pip install -r requirements.txt`, then double click the 'run ai.cmd' command. A command window should pop up with a progress bar. Once all the files have loaded, it will ask you your name. Enter your name then click enter. If a yellow `>: ` comes up, you're good to go! Simply type in what you want to say the the AI, and it should respond!

------------------------------
**Note:**
In the early stages of conversing with the AI, it doesn't know anything, so it will simply repeat whatever you say back to you. When this happens, just have a conversation with yourself, the AI will learn off this. Be very patient, it takes many conversations and restarts of the program for the AI to make any sense, so spend plenty of time training it up.

------------------------------
## Make your own modifications
Modify the `ginput.py` and `routput.py` files to change the method of gaining input and output respectively. You may want to use a text to speech program like pyttsx3 to make omnipotent speak it's responses instead of type them out! Or you could use a speech recognition library to allow the user to speak to omnipotent. The possibilities are endless! You can also now edit the `commands.py` file to give the AI new commands that it can run when the user gives it specific inputs!
