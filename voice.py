import subprocess

def say(idea):
    subprocess.call('espeak "' + idea + '" --stdout | aplay', shell=True)
