import subprocess

def say(idea):
    subprocess.call(['espeak', idea])
