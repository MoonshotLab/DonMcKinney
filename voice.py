import pyttsx

ptx = pyttsx.init()
ptx.setProperty('rate', 170)
ptx.setProperty('voice', 'default')

def say(idea):
    ptx.say(idea)
    ptx.runAndWait()
